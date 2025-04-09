#from django.urls import path
#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.ArticleListView.as_view(), name='home'),
    path('article/<int:pk>', views.ArticleListView.as_view(), name='detail'),
#    path('admin/', admin.site.urls),
#    path('', include('articles.urls')),

]