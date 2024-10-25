from django.core.management.base import BaseCommand, CommandParser
from django.contrib.auth import get_user_model
from django_seed import Seed
from rooms.models import Room, RoomType, Amenity, Facility, Rule
import random

User = get_user_model()


class Command(BaseCommand):
    help = 'This command creates rooms'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('--number', type=int, default=1,
                            help='How many rooms to create')

    def handle(self, *args, **options):
        try:
            number = options.get('number', 1)
            seeder = Seed.seeder()

            # Collect all possible related objects
            users = list(User.objects.all())
            amenities = list(Amenity.objects.all())
            facilities = list(Facility.objects.all())
            rules = list(Rule.objects.all())
            room_types = list(RoomType.objects.all())

            # Create rooms without Many-to-Many relationships first
            seeder.add_entity(Room, number, {
                'host': lambda x: random.choice(users),
                'price': lambda x: random.randint(100, 10_000),
                'guest': lambda x: random.randint(1, 10),
                'bed': lambda x: random.randint(1, 5),
                'bedroom': lambda x: random.randint(1, 5),
                'bath': lambda x: random.randint(1, 5),
                'room_type': lambda x: random.choice(room_types),
            })

            # Execute initial seeding to create Room instances
            created_rooms = seeder.execute()
            room_pks = created_rooms[Room]

            # Set Many-to-Many relationships
            for room_pk in room_pks:
                room = Room.objects.get(pk=room_pk)

                # Randomly assign amenities, facilities, and rules using `.set()`
                room.room_amenity.set(random.sample(
                    amenities, random.randint(1, len(amenities))))
                room.room_facility.set(random.sample(
                    facilities, random.randint(1, len(facilities))))
                room.house_rule.set(random.sample(
                    rules, random.randint(1, len(rules))))

            self.stdout.write(self.style.SUCCESS(
                f'Successfully created {number} rooms'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creating rooms: {e}'))
