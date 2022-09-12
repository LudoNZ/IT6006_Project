from django import forms
from forums.models import Comment


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('message',)

    widgets = {
        'message': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
    }
