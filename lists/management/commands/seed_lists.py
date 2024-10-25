import random
from django_seed import Seed
from lists.models import List
from rooms.models import Room
from django.core.management.base import BaseCommand, CommandParser
from django.contrib.auth import get_user_model
from typing import Any

User = get_user_model()

class Command(BaseCommand):
    help = 'This command generates wish lists'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('--number', type=int, default=1,
                            help='Number of wish lists to create')

    def handle(self, *args: Any, **options: Any) -> str | None:
        users = list(User.objects.all())
        rooms = list(Room.objects.all())
        number = options.get('number')

        try:
            seeder = Seed.seeder()
            
            # Seed List instances without Many-to-Many assignment
            seeder.add_entity(List, number, {
                'user': lambda x: random.choice(users),
            })
            
            created_lists = seeder.execute()
            list_pks = created_lists[List]

            # Assign Many-to-Many relationships
            for list_pk in list_pks:
                wishlist = List.objects.get(pk=list_pk)
                wishlist.room.set(random.sample(rooms, random.randint(1, 5)))  # Use set() to assign rooms

            self.stdout.write(self.style.SUCCESS(
                f'Successfully created {number} wish lists.'))

        except Exception as e:
            self.stderr.write(self.style.ERROR(
                f'Error creating wish lists: {e}'))
