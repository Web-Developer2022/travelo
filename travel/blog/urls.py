from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path("change_lang" , change_lang , name="change_lang")
]