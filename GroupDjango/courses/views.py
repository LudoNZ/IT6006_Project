from django.shortcuts import render
import requests
from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.urls import re_path
from courses.forms import TopicNoteForm

from .models import Course, Topic, Content

# Create your views here.

class DeveloperPageView(TemplateView):
    template_name = "courses/developer.html"

class CourseListView(ListView):
    model = Course
    template_name = "courses/course_list.html"

class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/course_detail.html"

class CourseNewDetailView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ("courses.add_courses")
    model = Course
    template_name = "courses/course_add.html"
    success_url="../../../courses/list/"
    fields =["name", "whatHeading", "whatDescription", "howHeading", "howDescription", "price"]

class CourseEditDetailView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ("courses.change_courses")
    model = Course
    template_name = "courses/course_edit.html"
    success_url="../../../courses/list/"
    fields =["name", "whatHeading", "whatDescription", "howHeading", "howDescription", "price"]

class CourseDeleteDetailView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ("courses.delete_courses")
    model = Course
    template_name = "courses/course_delete.html"
    success_url=reverse_lazy("courses")

class TopicListView(DetailView):
    model = Course
    template_name = "courses/topic_list.html"

class TopicNewDetailView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ("courses.add_topics")
    model = Topic
    template_name = "courses/topic_add.html"
    success_url="../../../courses/list/"
    fields =["course", "name", "intro"]

class TopicDetailView(DetailView):
    model = Topic
    template_name = "courses/topic_detail.html"

class TopicEditDetailView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ("courses.change_courses")
    model = Topic
    template_name = "courses/topic_edit.html"
    success_url="../../../courses/list/"
    fields =["course", "name", "intro"]

class TopicDeleteDetailView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView, DetailView):
    permission_required = ("courses.delete_courses")
    model = Topic
    template_name = "courses/topic_delete.html"
    success_url=reverse_lazy("courses")

class ContentDetailView(DetailView):
    model = Content
    template_name = "courses/content_detail.html"

class ContentNewDetailView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ("courses.add_topics")
    model = Content
    template_name = "courses/content_add.html"
    success_url="../../../courses/list/"
    fields =["topic", "name", "explanation", "example", "minutesToComplete"]