from django.urls import path
from accountapp.views import hello_world

app_name  = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
]#어디로 ~하면 어디로 돌려 줄것인지