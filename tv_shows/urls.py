from django.urls import path
from . import views

urlpatterns = [
    path('', views.tvShowListView),
    path('show_detaill/<int:id>/', views.tvShowDetailView),
    path('delete_list/', views.deleteListView),
    path('update_list/', views.updateListView),
    path('update_list/<int:id>/update/', views.editFilmView),
    path('delete_list/<int:id>/delete/', views.dropFilmView),
    path('create_film/', views.createShowView ),
]