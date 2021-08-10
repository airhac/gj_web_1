from django.forms import ModelForm

from commentapp.models import Comment


class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        #form에서 user한테 입력 받는 내용은 content밖에 없다
