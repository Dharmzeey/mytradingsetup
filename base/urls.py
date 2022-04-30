from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('', views.BaseView.as_view(), name="home"),
    path('create/', views.CreateSetUp.as_view(), name="create")
]