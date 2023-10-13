from django.urls import path
from . import views

urlpatterns = [
    path('', views.tvShowListView),
    path('show_detaill/<int:id>/', views.tvShowDetailView),
]