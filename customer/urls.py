from django.urls import path
from. import views

urlpatterns=[
  path('chome',views.home),
  path('clogin',views.login),
]