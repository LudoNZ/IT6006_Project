# import form class from django
from django import forms
 
# import GeeksModel from models.py
from .models import Topic

class TopicNoteForm(forms.ModelForm):
    def __init__(self, topic_list, *args, **kwargs):
        super(TopicNoteForm, self).__init__(*args, **kwargs)
        self.fields['name'] = forms.ChoiceField(choices=tuple([(name, name) for name in topic_list]))
        #widgets = {'agent': forms.widgets.TextInput(attrs={'readonly': True})}
    class Meta:
        model = Topic
        fields = '__all__'