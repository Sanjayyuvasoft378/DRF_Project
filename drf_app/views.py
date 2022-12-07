# from django.shortcuts import render
# from drf_app.models import *  # NOQA
# from django.http import JsonResponse
# # Create your views here.
# def movies_list(request):
#     movies = Movie.objects.all()
#     data = {
#     "movies":list(movies.values())
#     }
#     return JsonResponse(data)

# def movie_detail(request, id):
#     movie = Movie.objects.get(id=id)
#     data = {
#     "name":movie.name,
#     "description": movie.description,
#     "active": movie.active
#     }
#     return JsonResponse(data)