import json
import os

MOVIES_JSON_PATH = os.path.join('src', 'knowledge_base', 'movies.json')

# Cargo la base de conocimiento
def load_knowledge_base():
    with open(MOVIES_JSON_PATH, 'r', encoding='utf-8') as file:
        return json.load(file)
    
# Reglas de inferencia
def filtered_movies_by_genre(genre, movies):
    filtered_movies = []
    for movie in movies:
        if any(g in movie['props']['genre'] for g in genre):
            filtered_movies.append(movie)
    return filtered_movies

def filtered_movies_by_mood(mood, movies):
    filtered_movies = []
    for movie in movies:
        if any(m in movie['props']['mood'] for m in mood):
            filtered_movies.append(movie)
    return filtered_movies

def filtered_movies_by_year(year, movies):
    filtered_movies = []
    for movie in movies:
        if any(movie['props']['year'] >= y & movie['props']['year'] < (y + 10) for y in year):
            filtered_movies.append(movie)
    return filtered_movies

def filtered_movies_by_duration(duration, movies):
    filtered_movies = []
    for movie in movies:
        for d in duration:
            if d > 150 & movie['props']['duration'] > d:
                filtered_movies.append(movie)
            else:
                if (d - 30) <= movie['props']['duration'] & movie['props']['duration'] <= (d + 30):
                    filtered_movies.append(movie) 
    return filtered_movies

# Motor de inferencia
def inference_engine(params):
    movies = load_knowledge_base()
    filtered_movies = []
    genre = params.get('genre')
    mood = params.get('mood')
    year = params.get('year')
    duration = params.get('duration')    

    # Comparando los generos de las películas con lo que el usuario quiere
    filtered_movies = filtered_movies_by_genre(genre, movies)
    
    # Comparando los estados de ánimo de las películas con lo que el usuario quiere
    filtered_movies = filtered_movies_by_mood(mood, filtered_movies)
    
    # Comparando los años de las películas con lo que el usuario quiere
    filtered_movies = filtered_movies_by_year(year, filtered_movies)
    
    # Comparando las duraciones de las películas con lo que el usuario quiere
    filtered_movies = filtered_movies_by_duration(duration, filtered_movies)
        
    response = [movie['response'] for movie in filtered_movies]
    
    return response
    
    
