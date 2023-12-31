from django.urls import path

from subscribapp.views import SubscriptionView, SubscriptionListView

app_name = 'subscribapp'

urlpatterns=[
    path('subscribe/', SubscriptionView.as_view(), name='subscribe'),
    path('list/', SubscriptionListView.as_view(), name='list'),
]