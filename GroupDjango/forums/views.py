from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.http import Http404
from django.views import generic
from forums.models import Forum, Category, Comment
from forums.forms import CommentForm
from braces.views import SelectRelatedMixin


from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model
User = get_user_model()


class CreateForum(LoginRequiredMixin, generic.CreateView):
    model = Forum
    fields = ('title', 'category', 'description')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class UpdateForum(LoginRequiredMixin, generic.UpdateView):
    model = Forum
    fields = ('title', 'category', 'description')


class SingleForum(generic.DetailView):
    model = Forum

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


class ListForums(generic.ListView):
    model = Forum

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


######################################################################################################

######################################################################################################


@login_required
def add_comment_to_post(request, pk):
    forum = get_object_or_404(Forum, pk=pk)
    user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.forum = forum
            comment.user = user
            comment.save()
            return redirect('forums:single', pk=forum.pk)
    else:
        form = CommentForm()
    return render(request, 'forums/comment_form.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post.pk)
