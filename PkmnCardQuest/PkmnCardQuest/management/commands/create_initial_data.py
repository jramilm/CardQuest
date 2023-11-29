from django.core.management.base import BaseCommand
from PkmnCardQuest.models import PokemonCard, Trainer

class Command(BaseCommand):
    help = 'Creates initial data for the application'

    def handle(self, *args, **kwargs):
        self.create_pokemon_cards()
        # self.create_trainers()

    def create_pokemon_cards(self):
        # Create Pokemon Card instances
        card1 = PokemonCard(name='Pikachu', rarity="Rare", hp=60, card_type='Electric', attack="Thunder Shock",
                            description="A mouse-like pokemon that can generate electricity.", weakness='Ground',
                            card_number=25, release_date='1999-01-09', evolution_stage="Basic", abilities="Static")
        card1.save()
        self.stdout.write(self.style.SUCCESS('Successfully created Pokemon Cards.'))

    def create_trainers(self):
        pass