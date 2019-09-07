from django.contrib import admin

from survey.models import HappinessLevel


@admin.register(HappinessLevel)
class HappinessLevelAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', )
    search_fields = ('name', )
