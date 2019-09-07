from rest_framework import serializers

from survey.models import UserResponse


class UserResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserResponse
        fields = ('happiness_level', 'user', )
