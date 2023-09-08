from django.urls import path, include
from . import views

urlpatterns=[
    path('',views.endpoint,name="endpoint")
]