from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import SubmitPulseSurveyView, HappinessLevelView, StatisticView

urlpatterns = [
    path('api/submit', SubmitPulseSurveyView.as_view()),
    path('api/get-levels', HappinessLevelView.as_view()),
    path('api/get-stastics', StatisticView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
