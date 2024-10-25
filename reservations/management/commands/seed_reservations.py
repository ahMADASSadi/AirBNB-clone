from rooms.models import Room
from django.contrib.auth import get_user_model
import random
from django.core.management.base import BaseCommand, CommandParser
from django_seed import Seed

from reservations.models import Reservation

User = get_user_model()


class Command(BaseCommand):
    help = 'This command generates reservations'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('--number', type=int, default=1,
                            help='Number of reservations to create')

    def handle(self, *args, **options):
        seeder = Seed.seeder()
        number = options.get('number', 1)
        seeder.add_entity(Reservation, number, {
            'status': lambda x: random.choice([Reservation.STATUS_PENDING, Reservation.STATUS_CANCELED, Reservation.STATUS_CONFIRM,]),
            'guest': lambda x: random.choice(list(User.objects.all())),
            'room': lambda x: random.choice(list(Room.objects.all())),
            'check_in': lambda x: seeder.faker.date_between('-30d', 'now'),
            'check_out': lambda x: seeder.faker.date_between('now', '+30d'),
        })

        try:
            seeder.execute()
            self.stdout.write(self.style.SUCCESS(
                f'Successfully created {number} reservations'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(
                f'Error creating reservations: {e}'))
