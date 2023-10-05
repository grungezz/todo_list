from django import forms
from tasks.models import Task, Tag


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            'tags': forms.CheckboxSelectMultiple,
        }