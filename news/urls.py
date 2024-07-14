from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_main, name='main'),
    path('', views.news_main, name='end_post'),
    path('new', views.newpost, name='newpost'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='post-detail'),
    path('<int:pk>/editK4ifGn', views.NewsUpdateView.as_view(), name='post-update'),
    path('<int:pk>/deleteK4ifGn', views.NewsDeleteView.as_view(), name='post-delete'),
]