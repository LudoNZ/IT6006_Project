from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Count

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
    fields = ('title', 'description', 'is_closed')


class SingleForum(generic.DetailView):
    model = Forum

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context

    def get_comment_count(self):
        comment_counter = Comment.object.annotate(count('forum'))
        comment_count = comment_counter[self]
        return comment_count


class ListForums(generic.ListView):
    model = Forum

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


class ListSelectedUserForums(generic.ListView):
    model = Forum
    template_name = 'forums/forum_list_selected_user.html'

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related("forums").get(
                username__iexact=self.kwargs.get("user")
            )
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.forums.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


class ListSelectedUnsolvedForums(generic.ListView):
    model = Forum
    template_name = 'forums/forum_list_selected_unsolve.html'

    def get_queryset(self):
        return Forum.objects.filter(is_closed='False')

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
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    forum_pk = comment.forum.pk
    comment.delete()
    return redirect('forums:single', pk=forum_pk)
