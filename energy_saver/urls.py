from django.urls import path
from energy_saver import views


app_name = 'energy_saver'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
