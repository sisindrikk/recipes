

from django.urls import path
from . import views

app_name = "testapp3"

urlpatterns = [
    path('home/', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('data/', views.data, name='data'),
    path('recipe_list/', views.recipe_list, name='recipe_list'),
    path('<int:recipe_id>/details/', views.details, name='details'),
    path('login/', views.user_login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('logout/', views.logout_user, name='logout'),
    path('custom_login/', views.custom_login, name='custom_login'),
    path('custom_registartion/', views.custom_registartion, name='custom_registartion'),
]