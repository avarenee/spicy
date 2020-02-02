from django.urls import path
from . import views

app_name = "spicegallery"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('mixes/', views.MixView.as_view(), name='mixes'),
]
