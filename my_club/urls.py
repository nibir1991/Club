from django.urls import path
from .import views
from .views import ShowProfile,Register 
urlpatterns = [
path('', views.home ,name='home'),
path('registration/', Register.as_view() ,name='registration'),
path('profile/<int:pk>',ShowProfile.as_view(),name='profile'),
]