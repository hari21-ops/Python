from tkinter.font import names

from django.urls import path
from .views import SignUpView
#from ..login.urls import urlpatterns

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]