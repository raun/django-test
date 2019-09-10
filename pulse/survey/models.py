from django.contrib.auth.models import User
from django.db import models


class HappinessLevel(models.Model):
    """
    Table to store the happiness level, associated values and image to show against the option
    """
    name = models.CharField(max_length=150)
    value = models.IntegerField(unique=True, default=0)

    class Meta:
        db_table = 'HAPPINESS_LEVEL'

    def __str__(self):
        return '{} {}'.format(self.name, self.value)


class UserResponse(models.Model):
    """
    Table to store the user response on daily basis.
    Unique together constraint so a user can not submit a response twice in a day.
    """
    happiness_level = models.ForeignKey(to=HappinessLevel, on_delete=models.PROTECT, related_name="responses")
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, related_name="responses")
    input_date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'input_date')
        db_table = 'USER_RESPONSE'

    def __str__(self):
        return '{} {}'.format(self.user, self.input_date)

