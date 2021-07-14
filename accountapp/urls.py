from django.urls import path
from accountapp.views import hello_world, AccountCreateView

app_name  = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    path('create/', AccountCreateView.as_view(), name='create'), #클래스를 정상적으로 연동하기 위한 as_view()
]#어디로 ~하면 어디로 돌려 줄것인지