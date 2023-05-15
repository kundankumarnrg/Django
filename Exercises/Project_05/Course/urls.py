from django.urls import path
from Course import views

urlpatterns = [
    path('course/',views.course_name),
]
