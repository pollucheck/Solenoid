from django.urls import path, include
from streamapp import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('take', views.take, name='take'),
    path('quiz', views.quiz, name='quiz'),
    path('video_feed', views.video_feed, name='video_feed'),
    path('correction', views.correction, name='correction'),
    path('video_fee', views.video_fee, name='video_fee'),
    

    ]

