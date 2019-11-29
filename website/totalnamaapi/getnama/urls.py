from django.urls import path
from getnama import views

urlpatterns = [
    path('total/<nama>/', views.total_detail),
]