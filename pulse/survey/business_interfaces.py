from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db.models import Avg

from survey import error_status
from survey.models import UserResponse, HappinessLevel


class SurveySubmissionInterface(object):
    def __init__(self, username, happiness_value):
        """
        Args:
            username: username of the user who is trying to add rating
            happiness_value: rating the user has given
        """
        self.user = User.objects.filter(username=username).first()
        self.happiness_value = happiness_value

    def save(self):
        """

        Returns: A tuple with 2 elements, first one is the status, second one is created instance in case it succeed.

        Error Codes:
            1: User trying to add rating again for the same day
            2: User has given the non existent happiness level

        """
        happiness_level = HappinessLevel.objects.filter(value=self.happiness_value).first()
        if happiness_level is not None:
            try:
                return error_status.SUCCESS, UserResponse.objects.create(happiness_level=happiness_level,
                                                                         user=self.user)
            except IntegrityError as e:
                return error_status.INTEGRITY_ERROR, None
        else:
            return error_status.HAPPINESS_LEVEL_DOES_NOT_EXIST, None


class StatisticSummaryInterface(object):
    def __init__(self, username, interested_date):
        """
        Args:
            username: username of the user who is trying to get the statistic, empty string in case of AnonymousUser
            interested_date: date for which statistics are requested
        """
        self.user = User.objects.filter(username=username).first()
        self.analytics_date = interested_date
        self.stats = None

    def calculate_frequency_distribution(self):
        """
        Returns: a dictionary with keys as happiness level names and value as the count of each rating
                empty dictionary in case there are no happiness level exists in the system

        """
        happiness_level = HappinessLevel.objects.all()
        result = {}
        for level in happiness_level:
            level_count = level.responses.filter(input_date=self.analytics_date).count()
            result[level.name] = level_count
        return result

    def calculate_average_happiness_of_team(self):
        """
        Returns: a dictionary with keys as groups name the user belong to and value as the average group happiness.
            if user is not present it gives the happiness of the whole team

        """
        groups = []
        if self.user is not None:
            groups = self.user.groups.all()
        result = {}
        for group in groups:
            teammates = group.users.all()
            team_average = UserResponse.objects.filter(user__in=teammates, input_date=self.analytics_date).annotate(
                average_happiness=Avg('happiness_level__value'))
            if team_average.exists():
                result[group.name] = team_average.first().average_happiness
        else:
            team_average = UserResponse.objects.filter(input_date=self.analytics_date).annotate(
                average_happiness=Avg('happiness_level__value'))
            if team_average.exists():
                result["all"] = team_average.first().average_happiness
        return result

    def calculate_summary(self):
        """
        Returns: a dictionary containing the combined summary of statistic.

        """
        self.stats = {"frequency": self.calculate_frequency_distribution(),
                      "average": self.calculate_average_happiness_of_team(), }
        return self.stats
