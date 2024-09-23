import json
import os

MOVIES_JSON_PATH = os.path.join('src', 'knowledge_base', 'movies.json')

def load_knowledge_base():
    with open(MOVIES_JSON_PATH, 'r', encoding='utf-8') as file:
        return json.load(file)
    
def search_movies_by_iterable_parameter(value, movies, key):
    filtered_movies = []
    for movie in movies:
        if key in movie['props'] and any(value == g for g in movie['props'][key]):
            filtered_movies.append(movie)
    return filtered_movies

def search_movies_by_range_parameter(value, movies, key):
    filtered_movies = []
    for movie in movies:
        if key in movie['props']:
            movie_value = movie['props'][key]
            if key == 'year' and abs(movie_value - value) <= 5:
                filtered_movies.append(movie)
            elif key == 'duration' and abs(movie_value - value) <= 30:
                filtered_movies.append(movie)
    return filtered_movies
    
def inference_engine(params):
    movies = load_knowledge_base()
    filtered_movies = []
    genre = params.get('genre')
    mood = params.get('mood')
    year = params.get('year')
    duration = params.get('duration')    
    
    # Comparando género de la película
    filtered_movies = search_movies_by_iterable_parameter(genre, movies, 'genre')
    
    # Comparando estado de ánimo
    filtered_movies = search_movies_by_iterable_parameter(mood, filtered_movies, 'mood')
    
    # Comparando año de lanzamiento con un rango de 5 años más y menos
    filtered_movies = search_movies_by_range_parameter(year, filtered_movies, 'year')
    
    # Comparando duración de la película con un rango de 30 minutos más y menos
    filtered_movies = search_movies_by_range_parameter(duration, filtered_movies, 'duration')
    
    response = [movie['response'] for movie in filtered_movies]
    
    return response
    
    
