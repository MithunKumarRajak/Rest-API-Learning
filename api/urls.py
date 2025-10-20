from django.urls import include, path
from . import views

urlpatterns = [
    path('students/', views.students, name='students'),
]