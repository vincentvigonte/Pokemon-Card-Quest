from django.urls import path
from .views import HomePageView, TrainerList, PokemonCardList, CollectionList, TrainerCreateView, TrainerUpdateView, TrainerDeleteView, PokemonCardCreateView, PokemonCardUpdateView, PokemonCardDeleteView, CollectionCreateView, CollectionUpdateView, CollectionDeleteView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('trainer_list', TrainerList.as_view(), name='trainer-list'),
    path('trainer_list/add', TrainerCreateView.as_view(), name='trainer-add'),
    path('trainer_list/<pk>', TrainerUpdateView.as_view(), name='trainer-update'),
    path('trainer_list/<pk>/delete', TrainerDeleteView.as_view(), name='trainer-delete'),

    path('pokemon-card', PokemonCardList.as_view(), name='pokemon-card'),
    path('pokemon_card/add', PokemonCardCreateView.as_view(), name='pokemon-card-add'),
    path('pokemon_card/<pk>', PokemonCardUpdateView.as_view(), name='pokemon-card-update'),
    path('pokemon_card/<pk>/delete', PokemonCardDeleteView.as_view(), name='pokemon-card-delete'),

    path('collection', CollectionList.as_view(), name='collection'),
    path('collection/add', CollectionCreateView.as_view(), name='collection-add'),
    path('collection/<pk>', CollectionUpdateView.as_view(), name='collection-update'),
    path('collection/<pk>/delete', CollectionDeleteView.as_view(), name='collection-delete'),
]