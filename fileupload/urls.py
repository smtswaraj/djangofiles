from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    # path('',views.store_file),
    # path('',views.FileUpload.as_view()),
    path('',views.FileUpload.as_view()),
    path('imagelist',views.imageView.as_view())
]