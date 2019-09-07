from copy import deepcopy

from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from survey.serializers import UserResponseSerializer


class SubmitPulseSurvey(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserResponseSerializer

    def post(self, request, format=None):
        data = deepcopy(request.data)
        data.update(user=request.user.id)
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
