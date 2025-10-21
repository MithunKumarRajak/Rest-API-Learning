from django.urls import include, path
from . import views

urlpatterns = [
    # Here students is endpoint for all students
    path('students/', views.students, name='students'),
    # Here students ke place pe kuch bhi naam de shakte ho and <int:pk> is used to capture integer primary key from URL
    path('students/<int:pk>/', views.studentView, name='studentview'),
]
