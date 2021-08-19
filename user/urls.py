from django.urls import path
from .views import register, login, log_out

urlpatterns = [
    path('register/',register,name = "register"),
    path('login/',login, name = "login"),
    path('logout/',log_out, name = "logout")
]
