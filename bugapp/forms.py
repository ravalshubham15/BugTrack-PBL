from django import forms
from .models import Bug

class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ["title", "description", "priority", "status", "assigned_to"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter bug title"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 5, "placeholder": "Describe the bug"}),
            "priority": forms.Select(attrs={"class": "form-select"}),
            "status": forms.Select(attrs={"class": "form-select"}),
            "assigned_to": forms.Select(attrs={"class": "form-select"}),
        }
