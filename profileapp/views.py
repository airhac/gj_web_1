from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    template_name =  'profileapp/create.html'

    def form_valid(self, form):
        #이미지 파일  검증하고 나서 이후에 실행되는 함수
        form.instance.user = self.request.user
        #인스턴스의 user와 용청하는 user를 확인하는 방법
        return super().form_valid(form)#부모의 form을 그냥 가져와서 사용하는 것
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})
    #traget ㅐㅠㅓㄷㅊㅅfmf qkfh rkwudhftn dlTek

@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileCreationForm
    context_object_name = 'target_profile'
    template_name = 'profileapp/update.html'
     #내부 메서드를 오버라이딩하여 success_url을 대신한다.
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})
    #traget ㅐㅠㅓㄷㅊㅅfmf qkfh rkwudhftn dlTek