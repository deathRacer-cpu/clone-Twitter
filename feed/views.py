from django.shortcuts import render
from .models import tweet  # Change "tweet" to "Tweet"
from django.views.generic import ListView, CreateView, UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
# Create your views here.

class TweetListView(LoginRequiredMixin, ListView):
    model = tweet  # Change "tweet" to "Tweet"
    template_name = 'feed/home.html'
    ordering = ['-datetime']

class TweetCreateView(LoginRequiredMixin, CreateView):
    model = tweet  # Change "tweet" to "Tweet"
    fields = ['text']
    success_url = '/'

    def form_valid(self, form):
        form.instance.uname = self.request.user
        return super().form_valid(form)

class TweetUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  # Change inheritance to UpdateView
    model = tweet  # Change "tweet" to "Tweet"
    fields = ['text']
    success_url = '/'

    def form_valid(self, form):
        form.instance.uname = self.request.user
        return super().form_valid(form)

    def test_func(self):
        tweet = self.get_object()
        if self.request.user == tweet.uname:
            return True
        return False


class TweetDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):  # Change inheritance to UpdateView
    model = tweet  # Change "tweet" to "Tweet"
    fields = ['text']
    success_url = '/'

   

    def test_func(self):
        tweet = self.get_object()
        if self.request.user == tweet.uname:
            return True
        return False        


    # views.py
 
    #def tweet_like(request,pk):
    	#tweet=get_object_or_404(tweet)









