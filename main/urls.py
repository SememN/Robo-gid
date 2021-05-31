from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.load_main_page),

]
