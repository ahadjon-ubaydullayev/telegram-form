from django.urls import path
from tax.views import index


urlpatterns = [
    path('api/', index, name='handler'),
  
   
]
