# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 12:44:42 2025

@author: caitl
"""

import pandas as pd


# Sample data for the holiday movies dataset
holiday_movies_data = {
    'tconst': ['tt0106687', 'tt0151791', 'tt0108002', 'tt0088794', 'tt0367594'],
    'title_type': ['movie', 'movie', 'movie', 'movie', 'tvMovie'],
    'primary_title': ['Home Alone', 'The Grinch', 'Elf', 'Love Actually', 'The Polar Express'],
    'simple_title': ['home alone', 'the grinch', 'elf', 'love actually', 'the polar express'],
    'year': [1990, 2000, 2003, 2003, 2004],
    'runtime_minutes': [103, 86, 97, 135, 100],
    'average_rating': [7.6, 8.0, 7.0, 6.8, 6.6],
    'num_votes': [168, 235, 345, 567, 123]
}

# Sample data for the holiday movie genres dataset
holiday_movie_genres_data = {
    'tconst': ['tt0106687', 'tt0151791', 'tt0108002', 'tt0088794', 'tt0367594'],
    'genre_1': ['Comedy', 'Animation', 'Comedy', 'Romance', 'Animation'],
    'genre_2': ['Family', 'Adventure', 'Family', 'Drama', 'Fantasy'],
    'genre_3': [None, 'Comedy', 'Fantasy', None, None]
}

# Create DataFrames
holiday_movies = pd.DataFrame(holiday_movies_data)
holiday_movie_genres = pd.DataFrame(holiday_movie_genres_data)



# Stack genre columns and count occurrences
genres = pd.concat([holiday_movie_genres['genre_1'], holiday_movie_genres['genre_2'], holiday_movie_genres['genre_3']]).dropna()
genre_counts = genres.value_counts()

genre_counts


# Merge the holiday_movies DataFrame with the holiday_movie_genres DataFrame on 'tconst'
merged_movies = pd.merge(holiday_movies, holiday_movie_genres, on='tconst')

# Sort movies by 'average_rating' in descending order
sorted_movies = merged_movies.sort_values(by='average_rating', ascending=False)

sorted_movies[['primary_title', 'average_rating']]

# We can filter the movies to show only those released after the year 2000
recent_movies = holiday_movies[holiday_movies['year'] > 2000]
recent_movies[['primary_title', 'year']]

#We will calculate the average runtime for the movies in our dataset.
average_runtime = holiday_movies['runtime_minutes'].mean()
average_runtime



#We can combine the holiday_movies and holiday_movie_genres DataFrames to have a complete dataset with movie details and genres. We’ll join the two DataFrames on the tconst column.
combined_df = pd.merge(holiday_movies, holiday_movie_genres, on='tconst')
combined_df.head()














































