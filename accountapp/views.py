from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.models import NewModel
from accountapp.templates.accountapp.forms import AccountCreationForm


def hello_world(request):
    if request.user.is_authenticated:
        if request.method == 'POST':

            temp = request.POST.get('input_text')#서버의 데이터를 뽑아서 온다.
            model_instance = NewModel()
            model_instance.text = temp#이 값을 저장하는 데이터를 호풀해야함
            model_instance.save() #모델에 데이터를 저장한다.

            return HttpResponseRedirect(reverse('accountapp:hello_world'))#url을 nameing 해주는 것이다.
            #마지막 요청이 get으로 바뀐다.
        else:
            data_list = NewModel.objects.all()  # 이 모델의 모든 오브젝트드을 가지고 오겠다.
            return render(request, 'accountapp/hello_world.html',
                          context={'data_list': data_list})
            #어떠한 주소로 들어갔을떄 이것을 볼수 있는지 확인
    else:
        return HttpResponseRedirect(reverse('accountapp:login'))

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user' # target_user는 어떠한 키값이든지 간에 다 받는 변수의 이름
    template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView): #어떠한 객체를 업데이트 할것인가?
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world') #업데이트도 성공했을떄 어디로 연결할지를 적어 주어야한다.
    template_name = 'accountapp/update.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:#targetuser의 객체를 그대로 가져와 쓴다.
            return super().get(self, request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().post(self, request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url =  reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/delete.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:  # targetuser의 객체를 그대로 가져와 쓴다.
            return super().get(self, request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().post(self, request, *args, **kwargs)
        else:
            return HttpResponseForbidden()