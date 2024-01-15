
from django.urls import path
from . import views
from .views import TweetListView
from .views import TweetCreateView,TweetUpdateView,TweetDeleteView
urlpatterns = [
    path('', TweetListView.as_view(),name='home'),

    path('/create', TweetCreateView.as_view(),name='tweetcreate'),
    path('tweet/<int:pk>/update', TweetUpdateView.as_view(),name='tweetupdate'),
    path('tweet/<int:pk>/delete', TweetDeleteView.as_view(),name='tweetdelete'),

     
]