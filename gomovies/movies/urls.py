from django.conf.urls import url
from .views import movie_list, city_movie_detail
 
urlpatterns = [ 
    url(r'^api/movies$', movie_list),
    url(r'^api/movies_list$', city_movie_detail)
]