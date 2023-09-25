from django.shortcuts import render
from movie.models import Movie
from .movie_recommendations import recommendMovie
import numpy as np


def recommendations(request):
    prompt = request.GET.get('prompt')
    movies, sim = recommendMovie(prompt)
    if prompt:
        sorted_sim = np.sort(sim)
        newMovies = []
        newSortedSim = sorted_sim[::-1]
        for i in range(len(movies)):
            idx = np.argmax(sim)
            sim = np.delete(sim, np.where(sim == newSortedSim[i]))
            newMovies.append(movies[idx])    
        return render(request, 'recommendations.html', {'prompt': prompt, 'movies': newMovies})
    return render(request, 'recommendations.html', {'prompt': prompt, 'movies': movies})
