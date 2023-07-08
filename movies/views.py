from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Movie, Genre
# Create your views here.
from django.core.paginator import Paginator
import requests

base_url = "http://localhost:8000/"

def movie_detail_page(request, movie_id):
    url = base_url + f"api/movies/{movie_id}" 
    response = requests.get(url)
    movie_data = response.json()
    print(movie_data)
    
    genres = movie_data['genre']
    print(genres)
    genre_title = []
    for genre in genres:
        genre_title.append(Genre.objects.get(id = genre))

    return render(request, 'movie/movie_detail.html', {
        'movie': movie_data,
        'genre': genre_title
        })

def movie_page(request):
    movies_list = Movie.objects.all()
    # Set up Pagination

    p = Paginator(Movie.objects.all(), 20)
    page = request.GET.get('page')
    movies = p.get_page(page)
    nums = "a" * movies.paginator.num_pages
    context = {
        'movies_list' : movies_list,
        'movies' : movies,
        'nums' : nums 

    }
    return render(request, 'movie/movie.html', context)

def delete_movie(request, movie_id):
    url = base_url + f"api/movies/{movie_id}"  
    response = requests.delete(url)
    if response.status_code == 204:
        messages.success(request, ("Movie deleted successfully."))	
        return redirect("/movies")
    else:
        messages.success(request, ("There was some error in deleting the movie"))	
    return redirect("/movies")
