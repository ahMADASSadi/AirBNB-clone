from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):
    help = 'This command seed the database with new Amenities'

    def handle(self, *args, **kwargs):
        facilities = [
            'Air Conditioning',
            'Breakfast',
            'Cable TV',
            'Kitchen',
            'Heating',
            'Smoking Allowed',
            'Pets Allowed',
            'Family Friendly',
        ]

        try:
            Facility.objects.bulk_create(
                [Facility(name=facility) for facility in facilities])
            self.stdout.write(self.style.SUCCESS(
                'Facilities seeded successfully'))

        except Exception as e:
            self.stderr.write(self.style.ERROR(
                f'Error seeding Facilities: {e}'))
