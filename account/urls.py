from django.contrib.auth import views
from django.urls import path
from .views import *


urlpatterns = [
    path('login/', views.LoginView.as_view(), name="login"),
    path('profile/', ProfilePage.as_view(), name="profile"),
    path('register/', RegisterView.as_view(), name="register"),
    path('contacts/', ContactView.as_view(), name='contact_page'),
]