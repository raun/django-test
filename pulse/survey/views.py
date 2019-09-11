from copy import deepcopy

from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.response import Response
from rest_framework.views import APIView

from survey import error_status
from survey.serializers import UserResponseSerializer, StatisticSerializer


class SubmitPulseSurveyView(APIView):
    serializer_class = UserResponseSerializer
    stat_serializer_class = StatisticSerializer

    def post(self, request, format=None):
        status = HTTP_201_CREATED
        data = deepcopy(request.data)
        username = request.user.username
        if username is not '':
            data.update(username=username)
            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                instance = serializer.save()
                if instance == error_status.INTEGRITY_ERROR or instance == error_status.HAPPINESS_LEVEL_DOES_NOT_EXIST:
                    return Response({"error_code": instance}, status=HTTP_400_BAD_REQUEST)
            else:
                return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        else:
            status = HTTP_200_OK
        stat_serializer = self.stat_serializer_class(request.user)
        return Response(stat_serializer.data, status=status)

