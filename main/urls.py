from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('cr4d', views.cr4d, name='cr4d'),
    path('gd', views.gd, name='gd'),
    path('r', views.r, name='r'),
    path('nextvideo', views.whenisnextvideo, name='nextvideo'),
    path('nextlevel', views.nextlevel, name='nextlevel'),
    path('about', views.about, name='about'),
    path('cr4d/rules', views.cr4drules, name='cr4drules'),
    path('cr4d/rules/op', views.cr4drulesop, name='cr4drulesop'),
    path('cr4d/buildings', views.cr4dbuildings, name='cr4dbuildings'),
    path('cr4d/statistics', views.cr4dhistory, name='cr4dstatistics'),
    path('hexi', views.hexi, name='hexi'),
    path('hexi/qna', views.hexiqna, name='hexiqna'),
    path('sociallinks', views.sociallinks, name='sociallinks'),
    path('info', views.maininfo, name='maininfo'),


    path('r/info', views.info, name='info'),
    path('r/database', views.database, name='database'),
]