# from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_app.models import Movie
from drf_app.api.serializers import MovieSerializer
from rest_framework import status     
from rest_framework.views import APIView

class MovieListView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)

    def post(self, request):
        Serializer = MovieSerializer(data=request.data)
        if Serializer.is_valid():
            Serializer.save()
            return Response(Serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class MovieDetailView(APIView):
    def get(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)        
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self, request, pk):
            movie = Movie.objects.get(pk=pk)
            Serializer = MovieSerializer(movie,data=request.data)
            if Serializer.is_valid():
                Serializer.save()
                return Response(Serializer.data)
            else:
                return Response(Serializer.errors,status = status.HTTP_400_BAD_REQUEST)
            
    def delete(self, request,pk):
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    






# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer =MovieSerializer(movies,many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         Serializer = MovieSerializer(data=request.data)
#         if Serializer.is_valid():
#             Serializer.save()
#             return Response(Serializer.data,status=201)
#         else:
#             return Response(Serializer.errors,status=302)
        
        
# @api_view(['GET','PUT','DELETE'])
# def movie_detail(request, pk):
#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(pk = pk)
#         except Movie.DoesNotExist:
#             return Response({"error":"Movie not found"},status=status.HTTP_404_NOT_FOUND)
#         Serializer = MovieSerializer(movie)
#         return Response(Serializer.data)
    
#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk = pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         Serializer = MovieSerializer(movie,data=request.data)
#         if Serializer.is_valid():
#             Serializer.save()
#             return Response(Serializer.data)
#         else:
#             return Response(Serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        