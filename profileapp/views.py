from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name =  'profileapp/create.html'

    def form_valid(self, form):
        #이미지 파일  검증하고 나서 이후에 실행되는 함수
        form.instance.user = self.request.user
        #인스턴스의 user와 용청하는 user를 확인하는 방법
        return super.form_valid(form)#부모의 form을 그냥 가져와서 사용하는 것