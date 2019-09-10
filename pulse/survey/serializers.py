from rest_framework import serializers
from datetime import datetime

from survey.business_interfaces import SurveySubmissionInterface, StatisticSummaryInterface


class UserResponseSerializer(serializers.Serializer):
    """
        Serializer for submitting happiness for a user
    """
    username = serializers.CharField(max_length=200)
    happiness_value = serializers.IntegerField()

    def create(self, validated_data):
        """
        override abstract `create`

        """
        survey = SurveySubmissionInterface(**validated_data)
        status, instance = survey.save()
        if status != 0:
            return status
        else:
            return instance


class StatisticSerializer(serializers.Serializer):
    """
        Serializer for getting the Statistics of the team/group
    """
    frequency = serializers.SerializerMethodField()
    average = serializers.SerializerMethodField()

    def get_frequency(self, obj):
        stats = StatisticSummaryInterface(username=obj.username, interested_date=datetime.today().date())
        return stats.calculate_frequency_distribution()

    def get_average(self, obj):
        stats = StatisticSummaryInterface(username=obj.username, interested_date=datetime.today().date())
        return stats.calculate_average_happiness_of_team()


