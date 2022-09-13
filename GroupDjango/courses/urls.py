from django.urls import path
from .views import *
from .views import CourseNewDetailView, CourseEditDetailView, CourseDeleteDetailView, TopicNewDetailView, DeveloperPageView, TopicEditDetailView, TopicDeleteDetailView, ContentNewDetailView

urlpatterns = [
    path('courses/developer/', DeveloperPageView.as_view(), name="developer"), 
    path("courses/list/", CourseListView.as_view(), name="course_list"),
    path("courses/new", CourseNewDetailView.as_view(), name="course_new"),
    path('courses/edit/<int:pk>', CourseEditDetailView.as_view(), name="course_edit"),
    path('courses/delete/<int:pk>', CourseDeleteDetailView.as_view(), name="course_delete"),  
    path("courses/<int:pk>/", CourseDetailView.as_view(), name="course_detail"),
    path("courses/topiclist/<int:pk>/", TopicListView.as_view(), name="topic_list"),
    path("courses/topiclist/add/", TopicNewDetailView.as_view(), name="topic_add"),
    path('courses/topic/edit/<int:pk>', TopicEditDetailView.as_view(), name="topic_edit"),
    path('courses/topic/delete/<int:pk>', TopicDeleteDetailView.as_view(), name="topic_delete"), 
    path("courses/topic/content/new", ContentNewDetailView.as_view(), name="content_add"),
]

