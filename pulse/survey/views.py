from copy import deepcopy

from rest_framework.generics import ListAPIView
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.response import Response
from rest_framework.views import APIView

from survey import error_status
from survey.business_interfaces import HappinessLevelInterface
from survey.serializers import UserResponseSerializer, StatisticSerializer, HappinessLevelSerializer


class SubmitPulseSurveyView(APIView):
    serializer_class = UserResponseSerializer
    stat_serializer_class = StatisticSerializer

    def post(self, request, format=None):
        status = HTTP_200_OK
        data = deepcopy(request.data)
        username = request.user.username
        if username is not '':
            # Flow for authenticated user
            data.update(username=username)
            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                instance = serializer.save()
                status = HTTP_201_CREATED
                if instance == error_status.INTEGRITY_ERROR or instance == error_status.HAPPINESS_LEVEL_DOES_NOT_EXIST:
                    return Response({"error_code": instance}, status=HTTP_400_BAD_REQUEST)
            else:
                return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

        stat_serializer = self.stat_serializer_class(request.user)
        return Response(stat_serializer.data, status=status)


class HappinessLevelView(ListAPIView):
    serializer_class = HappinessLevelSerializer

    def get_queryset(self):
        return HappinessLevelInterface().get_all_active_level()


class StatisticView(APIView):
    serializer_class = StatisticSerializer

    def get(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=HTTP_200_OK)
