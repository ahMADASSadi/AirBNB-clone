import random
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django_seed import Seed
User = get_user_model()


class Command(BaseCommand):
    help = 'This command creates many users'

    def add_arguments(self, parser):
        parser.add_argument('--number', type=int, default=1,
                            help='Number of users to create')

    def handle(self, *args, **options):
        try:
            number = options.get('number', 1)
            if number <= 0:
                self.stdout.write(self.style.ERROR(
                    "The number of users must be greater than 0."))
                return

            seeder = Seed.seeder()
            seeder.add_entity(User, number, {
                'is_staff': False,
                'superhost': False,
                'is_superuser': False,
                'avatar': lambda x: f'userprofile/avatar-images/avatar_{x}.png',
                'gender': lambda x: random.choice([User.GENDER_MALE, User.GENDER_FEMALE, User.GENDER_OTHER]),
                'language': lambda x: random.choice([User.LANGUAGE_ENGLISH, User.LANGUAGE_PERSIAN]),
                'currency': lambda x: random.choice([User.CURRENCY_USD, User.CURRENCY_KRW, User.CURRENCY_IRR]),
            })

            seeder.execute()  # This line executes the seeder
            self.stdout.write(self.style.SUCCESS(
                f'Successfully created {number} users'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"The Error: {e} appears"))
