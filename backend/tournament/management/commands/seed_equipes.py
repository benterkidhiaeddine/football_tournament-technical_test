from django.core.management.base import BaseCommand
from tournament.models import Equipe
from faker import Faker


class Command(BaseCommand):
    help = "Seed the database with random Equipes."

    def add_arguments(self, parser):
        parser.add_argument(
            "--count", type=int, default=10, help="Number of equipes to create"
        )

    def handle(self, *args, **options):
        fake = Faker()
        count = options["count"]
        for _ in range(count):
            nom = fake.unique.company()
            ville = fake.city()
            Equipe.objects.get_or_create(nom=nom, ville=ville)
        self.stdout.write(self.style.SUCCESS(f"{count} equipes created!"))
