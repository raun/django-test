from django.core.management import BaseCommand
from django.db import IntegrityError

from survey.models import HappinessLevel


class Command(BaseCommand):
    """
    Management command to populate happiness levels in the application
    Usage: python manage.py populate_happiness_level
    """
    def _create_happiness_level(self):
        try:
            HappinessLevel.objects.create(value=1, name="Unhappy")
            HappinessLevel.objects.create(value=3, name="Neutral")
            HappinessLevel.objects.create(value=5, name="Very Happy")
            self.stdout.write(self.style.SUCCESS("HappinessLevel table is populated"))
        except IntegrityError:
            self.stderr.write(self.style.ERROR("HappinessLevel table is already populated"))

    def handle(self, *args, **options):
        self._create_happiness_level()
