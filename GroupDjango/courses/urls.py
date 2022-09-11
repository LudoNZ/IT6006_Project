from django.urls import path
from .views import *
from .views import CourseNewDetailView, CourseEditDetailView, CourseDeleteDetailView
from . import views
from django.conf.urls import include, url

urlpatterns = [
    path("courses/list/", CourseListView.as_view(), name="course_list"),
    path("courses/new", CourseNewDetailView.as_view(), name="course_new"),
    path('courses/<int:pk>/edit', CourseEditDetailView.as_view(), name="course_edit"),
    path('courses/<int:pk>/delete', CourseDeleteDetailView.as_view(), name="course_delete"),  
    path("courses/<int:pk>/", CourseDetailView.as_view(), name="course_detail"),
    path("courses/topiclist/<str:msg>", TopicListView.as_view(), name="topic_list"),
    #url(r'^(?P<name>[\w-]+)/$', TopicListView.as_view(), name="topic_list"),
    #path("courses/topiclist/<str:msg>", views.showmessage, name="topic_list"),
]

