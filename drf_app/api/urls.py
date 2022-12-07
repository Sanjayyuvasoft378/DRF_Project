from django.urls import path,include
from drf_app.api.views import *
from drf_app.api import views
urlpatterns = [
    path('movies/',MovieListView.as_view(),name='movies'),
    path('movie_detail/<int:pk>/',MovieDetailView.as_view(),name='movies'),
]
