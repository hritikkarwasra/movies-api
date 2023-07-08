import csv, json, ast, os, sys, django
import pandas as pd
import django
module_dir = os.path.abspath('/Users/hritikkarwasra/GitHub/movies-api')

# Append the module directory to sys.path
sys.path.append(module_dir)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')

# Initialize Django
django.setup()

from movies.models import Movie, Genre

def queries():
    movie = Movie.objects.get(title = 'Toy Story')
    genres = movie.genre.all()
    print('movie :', movie.title, movie.director, movie.release_date)
    print([genre.title for genre in genres])

def export_to_db():
    print('export')
    data = 'movies_metadata.csv'
    data_1 = 'credits.csv'
    with open(data, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader) #skip header
        for row in csv_reader:
            
            try:
                genres, id, name, director_name, release_date = row[3], row[5], row[8], None, row[14]
                genre_list = ast.literal_eval(genres)
                genre_objs = []
                for _ in genre_list:
                    genre_name = _['name']
                    genre = Genre.objects.get_or_create(title = genre_name)
                    genre_objs.append(genre)
                print(genre_objs)
                print('name :', name)
                print('release_date :', release_date)
                df = pd.read_csv(data_1)

                # Filter the DataFrame to find rows with the target ID
                filtered_df = df[df['id'] == int(id)]

                if not filtered_df.empty:
                    crew = filtered_df['crew'].iloc[0]
                    print('ID:', id)

                    # Filter rows where 'department' is 'Directing' in the crew section
                    crew_list = ast.literal_eval(crew)  # Convert crew string to a list of dictionaries

                    directing_crew = [member for member in crew_list if member['department'] == 'Directing']

                    if directing_crew:
                        director_name = directing_crew[0]['name']
                        print('Director:', director_name)
                    else:
                        print('No director found for the ID:', id)
                
                else:
                    print('ID not found:', id)

                movie = Movie.objects.get_or_create(title = name, director = director_name, release_date = release_date)
                print(movie[0])
                movie[0].genre.set([genre[0].id for genre in genre_objs])

if __name__ == "__main__":
    # export_to_db()
    queries()