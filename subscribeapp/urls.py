from django.urls import path

from subscribeapp.views import SubscriptionView

app_name = 'subscribeapp'
urlpatterns=[
    path('subscribe/<int:pk>', SubscriptionView.as_view(), name='subscribe')
]