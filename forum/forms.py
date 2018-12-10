from django import forms
from .models import Topic, Post


class TopicForm(forms.ModelForm):
    
    class Meta:
        
        model = Topic
        fields = ("title", "description", "image")
        
    def clean_title(self):
        
        title = self.cleaned_data.get("title")
        if Topic.objects.filter(title=title).exists():
            raise forms.ValidationError("Please use another title. This one already exists.")
        return title
        
class PostForm(forms.ModelForm):
    
    class Meta:
        
        model = Post
        fields = ("title", "description", "image")