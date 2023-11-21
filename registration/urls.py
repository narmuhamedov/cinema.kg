from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('', views.AuthLoginView.as_view(), name='login'),
    path('logout/', views.AuthLogoutView.as_view(), name='logout'),
    path('users/', views.UserListView.as_view(), name='user_list'),
]