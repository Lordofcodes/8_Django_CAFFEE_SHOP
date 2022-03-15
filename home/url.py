from django.urls import path
from . import views

app_name = "home"  # IMPORTANT
urlpatterns = [
    path('', views.home, name="index"),
    path('signup/', views.signup, name="signup"),
    path('order/', views.place_order, name="order"),
    path('', views.logout_user, name="logout")
]
