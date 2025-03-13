from django.core.management.base import BaseCommand
from django.contrib.auth.models import get_user_model
from django.conf import settings

User = get_user_model()

class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username='test taro').exists():
            User.objects.create_superuser(
                username='test taro',
                email='',
                password='P@ssword0123'
            )
            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
        else:
            self.stdout.write(self.style.SUCCESS('Superuser already exists'))