from django.urls import path
from .import views
from .views import register,ShowProfile 
urlpatterns = [
path('', views.home ,name='home'),
path('registration/', register.as_view() ,name='registration'),
path('profile/<int:pk>',ShowProfile.as_view(),name='profile'),
]