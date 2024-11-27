from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),  # List students
    path('create/', views.student_create, name='student_create'),  # Create a student
    path('update/<int:pk>/', views.student_update, name='student_update'),  # Update a student
    path('delete/<int:pk>/', views.student_delete, name='student_delete'),  # Delete a student
]
