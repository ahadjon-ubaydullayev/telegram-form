from django.urls import path
from form.views import index


urlpatterns = [
    path('api/', index, name='handler'),
  
   
]
