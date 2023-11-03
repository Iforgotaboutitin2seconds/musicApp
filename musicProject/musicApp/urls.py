from django.urls import path
from . import views

urlpatterns = [
    path('', views.songListView.as_view(), name='songs'),
    path('songs/', views.songListView.as_view(), name='songs'),
    path('song/<int:pk>/', views.songDetailView.as_view(), name='song_detail'),
    path('song/new/', views.songCreateView.as_view(), name='song_new'),
    path('song/<int:pk>/edit/', views.songUpdateView.as_view(), name='song_edit'),
    path('song/<int:pk>/delete/', views.songDeleteView.as_view(), name='song_delete'),
]
