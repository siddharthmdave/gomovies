from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import Movie, Cinema, Screens, Show
from .serializers import MovieSerializer
from rest_framework.decorators import api_view

import uuid


@api_view(['GET', 'POST','PUT'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            movies = movies.filter(title__icontains=title)

        movies_serializer = MovieSerializer(movies, many=True)
        return JsonResponse(movies_serializer.data, safe=False)

    elif request.method == 'POST':
        movie_data = JSONParser().parse(request)
        movie_serializer = MovieSerializer(data=movie_data)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return JsonResponse(movie_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(movie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        movie_data = JSONParser().parse(request)
        movie = Movie.objects.filter(movieId__icontains=movie_data.get('movieId','')).first()
        movie_serializer = MovieSerializer(movie,data=movie_data)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return JsonResponse(movie_serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(movie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def city_movie_detail(request):
    resp = {}
    city = request.query_params.get('City',None)
    if city is not None:
        try:
            movies = []
            show_details = Show.objects.select_related('movieId','hallId__cinemaId').filter(hallId__cinemaId__city=city) 
            for show_detail in show_details:
                movie = show_detail.movieId.title
                if movie not in movies:
                    movies.append(movie)

            if len(movies) == 0:
                return JsonResponse({'message': 'No shows available in city'}, status=status.HTTP_404_NOT_FOUND)
            else:
                resp['Movies'] = movies
                print(type(resp))
                return JsonResponse(resp)
        except:
            return JsonResponse({'message': 'No shows available in city'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return JsonResponse({"City" : [ "This field is required."]}, status=status.HTTP_400_BAD_REQUEST)
