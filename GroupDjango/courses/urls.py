from django.urls import path
from .views import *
from .views import CourseNewDetailView, CourseEditDetailView, CourseDeleteDetailView

urlpatterns = [
    path("courses/list/", CourseListView.as_view(), name="course_list"),
    path("courses/new", CourseNewDetailView.as_view(), name="course_new"),
    path('courses/<int:pk>/edit', CourseEditDetailView.as_view(), name="course_edit"),
    path('courses/<int:pk>/delete', CourseDeleteDetailView.as_view(), name="course_delete"),  
    path("courses/<int:pk>/", CourseDetailView.as_view(), name="course_detail"),
    path("courses/<int:pk>/topiclist/", TopicListView.as_view(), name="topic_list"),
]

