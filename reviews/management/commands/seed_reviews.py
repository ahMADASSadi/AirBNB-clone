from django.core.management.base import BaseCommand, CommandParser
from django.contrib.auth import get_user_model
from django_seed import Seed
from reviews.models import Review
from rooms.models import Room
import random

User = get_user_model()


class Command(BaseCommand):
    help = 'This command creates reviews'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('--number', type=int, default=1,
                            help='Number of reviews to create')

    def handle(self, *args, **options):
        seeder = Seed.seeder()
        number = options.get('number', 1)
        customers = list(User.objects.all())
        rooms = list(Room.objects.all())

        try:
            seeder.add_entity(Review, number, {  # Use the Review model directly
                "accuracy": lambda x: random.randint(1, 5),
                "communication": lambda x: random.randint(1, 5),
                "cleanliness": lambda x: random.randint(1, 5),
                "location": lambda x: random.randint(1, 5),
                "check_in": lambda x: random.randint(1, 5),
                "value": lambda x: random.randint(1, 5),
                "customer": lambda x: random.choice(customers),
                "room": lambda x: random.choice(rooms),
            })
            seeder.execute()
            self.stdout.write(self.style.SUCCESS(
                f'Successfully created {number} reviews.'))

        except Exception as e:
            self.stderr.write(self.style.ERROR(
                f'Error creating reviews: {e}'))
