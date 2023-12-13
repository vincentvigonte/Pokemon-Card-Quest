from django.contrib import admin
from .models import Trainer, PokemonCard, Collection

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthdate', 'location', 'email', 'created_at', 'updated_at')
    search_fields = ('name', 'location')

@admin.register(PokemonCard)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('name', 'rarity', 'hp', 'card_type', 'attack', 'description', 'weakness', 'card_number', 'release_date', 'evolution_stage', 'abilities', 'created_at', 'updated_at')
    search_fields = ('name',)

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('trainer', 'card', 'collection_date', 'created_at', 'updated_at')
    search_fields = ('trainer', 'card')