from django.core.management.base import BaseCommand
from tournament.models import Joueur, Equipe
from faker import Faker
import random


class Command(BaseCommand):
    help = "Seed the database with random Joueurs."

    def add_arguments(self, parser):
        parser.add_argument(
            "--count", type=int, default=20, help="Number of joueurs to create"
        )

    def handle(self, *args, **options):
        fake = Faker()
        count = options["count"]
        equipes = list(Equipe.objects.all())
        if not equipes:
            self.stdout.write(
                self.style.ERROR("No equipes found. Please seed equipes first.")
            )
            return
        posts = [choice[0] for choice in Joueur.Post.choices]
        for _ in range(count):
            nom = fake.unique.first_name()
            poste = random.choice(posts)
            equipe = random.choice(equipes)
            Joueur.objects.get_or_create(nom=nom, poste=poste, equipe=equipe)
        self.stdout.write(self.style.SUCCESS(f"{count} joueurs created!"))
