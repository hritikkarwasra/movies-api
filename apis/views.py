from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from movies.models import Movie
from movies.serializers import MovieSerializer

class MovieListPagination(PageNumberPagination):
    page_size = 20  # Number of items to be included on each page
    page_size_query_param = 'page_size'  # Parameter to control the page size
    max_page_size = 100  # Maximum allowed page size

class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = MovieListPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        genre = self.request.query_params.get('genre')
        director = self.request.query_params.get('director')

        if genre:
            queryset = queryset.filter(genre__title=genre)

        if director:
            queryset = queryset.filter(director__icontains=director)

        return queryset


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_detail(self):
        movie_id = self.kwargs["pk"]

        movie = Movie.objects.get(id=movie_id)
        genres = movie.genre.all()
        genres_list = [gen.title for gen in genres]
        print('hi')
        print (genres)
        return {
            "movie_detail": movie,
            "genres": genres_list
            }


