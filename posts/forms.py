from django import forms
from .models import Post,Comment,Key

class PostForm(forms.ModelForm) :
    title = forms.CharField(
        max_length=100,
        label='제목',
        help_text='제목은 12자이내로 작성해주세요.',
        widget=forms.TextInput(
            attrs={
                'class': 'my-input',
                 }
        )
    )

    content = forms.CharField(
        label='내용',
        help_text='자유롭게 작성해주세요.',
        widget=forms.Textarea(
            attrs={
                'row': 5,
                'col': 50,
            }
        )
    )

    class Meta:
        model = Post
        fields = ['title', 'content','category','image']

class CommentForm(forms.ModelForm) :
    content = forms.CharField(
        label='내용',
        help_text='자유롭게 작성해주세요.',
        widget=forms.Textarea(
            attrs={
                'row': 5,
                'col': 35,
            }
        )
    )

    class Meta :
        model = Comment
        fields=['content','image','link']


class KeyForm(forms.ModelForm):

    class Meta :
        model=Key
        fields=['key_number']
