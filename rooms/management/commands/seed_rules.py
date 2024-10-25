from django.core.management.base import BaseCommand
from rooms.models import Rule


class Command(BaseCommand):
    help = 'This command seed the database with new Rules'

    def handle(self, *args, **kwargs):
        rules = [
            'No Smoking',
            'No Pets',
            'No Parties or Events',
            'Quiet Hours from 10 PM to 7 AM',
            'Check-in after 3 PM, Check-out before 11 AM',
            'Max Occupancy of 2 People',
            'No Unregistered Guests',
            'Respect for Neighbors',
            'Clean Up Before Leaving',
            'Guests Responsible for Damage',
        ]

        try:
            Rule.objects.bulk_create(
                [Rule(name=rule) for rule in rules])
            self.stdout.write(self.style.SUCCESS(
                'Rules seeded successfully'))

        except Exception as e:
            self.stderr.write(self.style.ERROR(
                f'Error seeding Rules: {e}'))
