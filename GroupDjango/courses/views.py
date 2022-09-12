from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.urls import re_path

from .models import Course, Topic

# Create your views here.

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
    success_url="courses/"
    fields =["name", "whatHeading", "whatDescription", "howHeading", "howDescription", "price"]

class CourseEditDetailView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ("courses.change_courses")
    model = Course
    template_name = "courses/course_edit.html"
    success_url="courses/"
    fields =["name", "whatHeading", "whatDescription", "howHeading", "howDescription", "price"]

class CourseDeleteDetailView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ("courses.delete_courses")
    model = Course
    template_name = "courses/course_delete.html"
    success_url=reverse_lazy("courses")


class TopicListView(ListView):
    model = Course
    template_name = "courses/topic_list.html"

    # def get_queryset(self):
    #     return Topic.objects.all()

    # def get_object(self, queryset=None):
    #     return queryset.get(slug=self.slug)

# def showmessage(request, msg):
#     return render(request, 'courses/topic_list.html', {'msg' : msg})



# class TopicEditView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
#     permission_required = ("courses.add_topic")
#     model = Topic
#     template_name = "courses/topic_add.html"
#     success_url="courses/"
#     fields =["course", "name", "intro"]
