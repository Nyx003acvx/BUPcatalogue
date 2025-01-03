
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.favorite_summary, name = 'favorite_summary'),
    path('', views.favorite_add, name = 'favorite_add'),
    path('', views.favorite_remove, name = 'favorite_remove'),
    path('', views.favorite_update, name = 'favorite_update'),
    
    

]