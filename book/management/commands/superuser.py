from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings
import os

User = get_user_model()

class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username='test taro').exists():
            User.objects.create_superuser(
                username=os.environ.get('SUPERUSER_USERNAME'),
                email='',
                password=os.environ.get('SUPERUSER_PASS')
            )
            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
        else:
            self.stdout.write(self.style.SUCCESS('Superuser already exists'))