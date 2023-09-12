import json
from typing import Any, Dict
from django.shortcuts import render, get_object_or_404
from movies.models import *
from django.views.generic import ListView, View, DetailView
from movies.filtersearch import movie_filter
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

# Homepage
def index(request):
    return render(request, 'pages/index.html')

# Filter search, include filtersearch.py file
def type_movie_view(request, slug):
    filter_string = movie_filter(request)

    movie_type = MovieType.objects.get(slug=slug)
    movies = Movie.objects.filter(movie_type=movie_type, **filter_string)
    context = {
        'movies': movies,
        'movie_type': movie_type
    }

    return render(request, 'pages/typemovieview.html', context)


# DetailMovie views
class MovieDetails(DetailView):
    template_name = 'pages/moviedetail.html'
    queryset = Movie.objects.all()
    context_object_name = 'movie'

    def get_context_data(self, *args, **kwargs):
        context = super(MovieDetails, self).get_context_data(*args, **kwargs)

        return context
    
# Login account for user here to give review for movie
#@login_required(login_url='/account/login')
#def create_review(request):
#    if request.method == 'POST':
#        data = json.loads(request.body)
#
#        movie_id = data.get('movie_id')
#        movie = get_object_or_404(Movie, id=movie_id)
#        user = request.user
#        rating = data.get('rating', 1)
#        message = data.get('message', '')
#
#        review, created = Review.objects.update_or_create(
#            user = user,
#            movie = movie,
#            defaults = {
#                'rating': rating,
#                'message': message
#            }
#        )
#
#        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
#    
#    return JsonResponse({'succes': False})