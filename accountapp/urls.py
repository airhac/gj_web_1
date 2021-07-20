from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accountapp.views import hello_world, AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name  = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', AccountCreateView.as_view(), name='create'),
    #클래스를 정상적으로 연동하기 위한 as_view()#routing을 해준것이다
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),# 고유값을 넘겨받아 어떠한 account객체의 고유값을 보고자하는지 알려준다.
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
]#어디로 ~하면 어디로 돌려 줄것인지