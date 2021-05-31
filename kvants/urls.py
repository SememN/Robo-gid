from django.urls import path
from . import views

app_name = 'kvants'
urlpatterns = [
    path('it-kvant', views.load_it_page, name='it-kvant-page'),
    path('aero-kvant', views.load_aero_page, name='aero-kvant-page'),
    path('auto-kvant', views.load_auto_page, name='auto-kvant-page'),
    path('prom-design-kvant', views.load_design_page, name='design-kvant-page'),
    path('prom-robo-kvant', views.load_robo_page, name='robo-kvant-page'),
    path('hi-tech-kvant', views.load_hi_tech_page, name='hi-tech-kvant-page'),
]
