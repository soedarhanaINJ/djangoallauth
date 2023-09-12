from movies import views
from django.urls import path
from allauth.account.views import LoginView

urlpatterns = [
    path('', views.index, name='index'),
    path('movie-type/<slug:slug>/', views.type_movie_view, name='type_movie_view'),
    path('movie/<slug:slug>/', views.MovieDetails.as_view(), name='moviedetails'),
#    path('create-review/', views.create_review, name='create_review'),
]