from django.urls import path
from .views import anime, unit



urlpatterns = [path("", anime, name="index"), path("<str:path>", unit)]
