from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):
    help = 'This command seed the database with new Amenities'

    def handle(self, *args, **kwargs):
        amenities = [
            'Air Conditioning',
            'Breakfast',
            'Cable TV',
            'Kitchen',
            'Heating',
            'Smoking Allowed',
            'Pets Allowed',
            'Family Friendly',
            'Pool',
            'Indoor Seating',
            'Fitness Center',
            'Gym',
            '24-Hour Reception',
            'Wheelchair Accessible',
            'Private Bathroom',
            'Smoke Detector',
            'Fire Extinguisher',
            'Shampoo',
            'Body Soap',
            'Essentials',
            'Washer',
            'Dryer',
            'Iron',
            'Free Parking',
            'Suitable for Events',
            'Pets Allowed',
            'Pets Allowed',
            'Indoor Seating',
            'Outdoor Seating',
            'Room-darkened',
            'Buzzer/Wireless Intercom',
            'Heating',
            'Kitchen',
            'Washer',
            'Dryer',
            'Indoor Pool',
            'Outdoor Pool',
            'Smoke Detector',
            'Fire Extinguisher',
            'Essentials',
            'Private Bathroom',
            'Shampoo',
            'Body Soap',
            'Free Parking',
            'Suitable for Events',
            'Pets Allowed',
            'Pets Allowed',
            'Indoor Seating',
            'Outdoor Seating',
            'Room-darkened',
            'Buzzer/Wireless Intercom',
            'Heating',
        ]

        try:
            Amenity.objects.bulk_create(
                [Amenity(name=amenity) for amenity in amenities])
            self.stdout.write(self.style.SUCCESS(
                'Amenities seeded successfully'))

        except Exception as e:
            self.stderr.write(self.style.ERROR(
                f'Error seeding Amenities: {e}'))
