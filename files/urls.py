from django.urls import path
from files import views

app_name = 'files'

urlpatterns = [
    # path('upload/', views.UploadFileView.as_view()),
    path('', views.ShowFilesView.as_view()),
    # path('download/', views.DownloadFileView.as_view()),
    # path('<int:pk>/', views.ManageFileView.as_view()),
]