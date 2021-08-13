from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from commentapp.models import Comment


def comment_ownership_required(func):
    def decorated(request, *args, **kwargs):
        target_comment = Comment.objects.get(pk=kwargs['pk'])
        #User의 조건을 부여해야함
        #get 메서드는 단일 객체를 가지고 올 수 있도록 해주는 함수이다.
        if target_comment.writer == request.user:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return decorated