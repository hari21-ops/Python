from django.shortcuts import render
from django.views.generic import ListView
from .models import Article
from django.views.generic import ListView, DetailView

# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail.html'


