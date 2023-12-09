from django.urls import path
from files import views

app_name = 'files'

urlpatterns = [
    path('upload/', views.UploadFileView.as_view(),name='file-upload'),
    path('', views.ShowFilesView.as_view(), name='file-list'),
    path('download/', views.ShowFilesView.as_view(), name='file-download'),
    path('<int:pk>/', views.ManageFileView.as_view()),
]