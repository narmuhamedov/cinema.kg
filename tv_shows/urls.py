from django.urls import path
from . import views

urlpatterns = [
    path('', views.TvShowListView.as_view()),
    path('show_detaill/<int:id>/', views.TvShowDetailView.as_view()),
    path('delete_list/', views.DeleteShowView.as_view()),
    path('update_list/', views.UpdateShowView.as_view()),
    path('update_list/<int:id>/update/', views.EditShowView.as_view()),
    path('delete_list/<int:id>/delete/', views.DropFilmView.as_view()),
    path('create_film/', views.CreateShowView.as_view()),
]