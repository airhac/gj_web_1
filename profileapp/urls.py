from django.urls import path

from profileapp.views import ProfileCreateView

app_name = 'profileapp'

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create'),
]#어디로 ~하면 어디로 돌려 줄것인지