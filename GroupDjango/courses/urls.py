from django.urls import path
from .views import *

urlpatterns = [
    path("courses/list/", CourseListView.as_view(), name="course_list"),
     path("courses/<int:pk>/", CourseDetailView.as_view(), name="course_detail"),
]

