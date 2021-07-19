from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accountapp.views import hello_world, AccountCreateView, AccountDetailView

app_name  = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', AccountCreateView.as_view(), name='create'),
    #클래스를 정상적으로 연동하기 위한 as_view()#routing을 해준것이다
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
]#어디로 ~하면 어디로 돌려 줄것인지