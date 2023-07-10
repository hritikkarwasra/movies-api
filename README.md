# Movie API
This API provides endpoints to manage movies. It allows users to retrieve, create, update, and delete movies. The movies have attributes such as title, genre, release date, and director.

### How to run this project
#### Run Following commmands

```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Endpoints
```
Retrieve a List of All Movies
URL: /api/movies
Method: GET
Description: Retrieve a list of all movies.
```

## Retrieve a Specific Movie
```
URL: /api/movies/{id}
Method: GET
Description: Retrieve a specific movie by its ID.
```

## Create a New Movie
```
URL: /api/movies
Method: POST
Description: Create a new movie.
```

## Update an Existing Movie
```
URL: /api/movies/{id}
Method: PUT/PATCH
Description: Update an existing movie.
```

## Delete a Movie
```
URL: /api/movies/{id}
Method: DELETE
Description: Delete a movie.
```

## Movie Attributes
```
The movie should have the following attributes:

title (string): The title of the movie. It is required and should be a maximum of 255 characters.
genre (string): The genre of the movie. It is required and should be a maximum of 100 characters.
release_date (date): The release date of the movie. It is required and should be a valid date in the format YYYY-MM-DD.
director (string): The director of the movie. It is required and should be a maximum of 100 characters.
Validation Rules
The backend implements the following validation rules for movie creation and update:

The title field is required and should be a maximum of 255 characters.
The genre field is required and should be a maximum of 100 characters.
The release_date field is required and should be a valid date in the format YYYY-MM-DD.
The director field is required and should be a maximum of 100 characters.
```

## Pagination
```
The /api/movies endpoint supports pagination. 20 movies per page and retrieve the desired page.
```

## Filtering
```
The /api/movies endpoint allows users to filter movies based on genre or director. Users can include the following query parameters to apply the desired filters:

genre: Filter movies by genre.
director: Filter movies by director.
Please note that the query parameter values are case-sensitive.

Feel free to explore and interact with the Movie API!
```
