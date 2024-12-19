from django.urls import path
from . import views

urlpatterns = [
    path('generate_table/', views.generate_table, name='generate_table'),
    path('quiz/', views.quiz, name='quiz'),
    path('puzzle/', views.puzzle, name='puzzle'),
    path('feedback/', views.feedback, name='feedback'),
    path('game/', views.game, name='game'),
    path('get_matching_game/', views.get_matching_game, name='get_matching_game'),
    path('get_timed_challenge/', views.get_timed_challenge, name='get_timed_challenge'),
    path('get_puzzle_game/', views.get_puzzle_game, name='get_puzzle_game'),
]
