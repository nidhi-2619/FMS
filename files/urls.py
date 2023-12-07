from django.urls import path
from files import views

app_name = 'files'

urlpatterns = [
    path('add/', views.CreateFileView.as_view()),
    path('', views.ListFileView.as_view()),
    path('<int:pk>/', views.ManageFileView.as_view()),
]