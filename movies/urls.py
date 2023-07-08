from django.urls import path
from .views import movie_page, delete_movie, movie_detail_page

urlpatterns = [
    path('', movie_page, name = 'movies_page'),
    path('delete/<int:movie_id>', delete_movie, name = 'delete-movie'),
    path('<int:movie_id>/', movie_detail_page, name='movie-detail'),
]