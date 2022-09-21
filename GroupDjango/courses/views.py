from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
import requests
from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.urls import re_path
from courses.forms import TopicNoteForm

from .models import Course, Question, Topic, Content
from enrolment.models import Result

# Create your views here.

class DeveloperPageView(TemplateView):
    template_name = "courses/developer.html"

class CourseListView(ListView):
    model = Course
    template_name = "courses/course_list.html"

class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/course_detail.html"

    def get(self, request, pk):
        course = Course.objects.get(id=pk)
        topics = Topic.objects.filter(course=course).all()

        contents = Content.objects.filter(topic__course__pk=pk).all()
        user_results = Result.objects.filter(user=request.user, result=True).all()
        
        for c in contents:
            c.template_user_result = 0
            for a in user_results:
                if a.question.content == c:
                    c.template_user_result += 1
        
        return render(request, 'courses/course_detail.html', {'course': course, 
                                                                'topics': topics,
                                                                'contents': contents,
                                                                'user_results': user_results,
                                                                })


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
    
    def get(self, request, pk):
        topic = Topic.objects.get(id=pk)
        content = Content.objects.filter(topic__pk=pk).all()
        user_results = Result.objects.filter(user=request.user, result=True).all()
        
        for c in content:
            c.template_user_result = 0
            for a in user_results:
                if a.question.content == c:
                    c.template_user_result += 1

        return render(request, 'courses/topic_detail.html', {'content': content,
                                                                'topic': topic})

    
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
    
    def get(self, request, pk):
        content = Content.objects.get(pk=pk)
        user_results = Result.objects.filter(user=request.user).all()
        return render(request, 'courses/content_detail.html', {'user_results': user_results, 
                                                                'content': content})


class ContentNewDetailView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ("courses.add_topics")
    model = Content
    template_name = "courses/content_add.html"
    success_url="../../../courses/list/"
    fields =["topic", "name", "explanation", "example", "minutesToComplete"]

def answer_true(request, id, pk):
    question = get_object_or_404(Question, id=id)
        
    if question.answer:
        result = Result.objects.update_or_create(
                        user=request.user, 
                        question=question,
                        defaults={'result': True})
    else:
        result = Result.objects.update_or_create(
                        user=request.user, 
                        question=question,
                        defaults={'result': False})
    result.save()

    return JsonResponse({'is_correct': result.result})

def answer_false(request, id, pk):
    question = get_object_or_404(Question, id=id)
    

    if not question.answer:
        result = Result.objects.update_or_create(
                        user=request.user, 
                        question=question,
                        defaults={'result': True})
    else:
        result = Result.objects.update_or_create(
                        user=request.user, 
                        question=question,
                        defaults={'result': False})

    result.save()

    return JsonResponse({'is_correct': result.result})