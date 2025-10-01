from django import forms
from posts.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "post",
            "content",
        ]
# 의와 동일
# class CommentForm(forms.Form):
#     content = forms.CharField(min_length=200)
