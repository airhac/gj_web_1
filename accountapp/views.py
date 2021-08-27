from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.models import NewModel
from accountapp.forms import AccountCreationForm
from articleapp.models import Article

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('articleapp:list')
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user' # target_user는 어떠한 키값이든지 간에 다 받는 변수의 이름
    template_name = 'accountapp/detail.html'
    def get_context_data(self, **kwargs):
        article_list = Article.objects.filter(writer=self.object)
        return super().get_context_data(object_list=article_list,**kwargs)
has_ownership = [login_required, account_ownership_required]



@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
#메서드에도 데토레이터가 적용될 수 있도록 변환 해주는 박업을 한다.
class AccountUpdateView(UpdateView): #어떠한 객체를 업데이트 할것인가?
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    #success_url = reverse_lazy('accountapp:hello_world') #업데이트도 성공했을떄 어디로 연결할지를 적어 주어야한다.
    template_name = 'accountapp/update.html'
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.pk})
    #traget ㅐㅠㅓㄷㅊㅅfmf qkfh rkwudhftn dlTek


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url =  reverse_lazy('articleapp:list')
    template_name = 'accountapp/delete.html'



    '''def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:  # targetuser의 객체를 그대로 가져와 쓴다.
            return super().get(self, request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().post(self, request, *args, **kwargs)
        else:
            return HttpResponseForbidden()'''