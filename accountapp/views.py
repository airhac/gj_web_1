from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from accountapp.models import NewModel


def hello_world(request):
    if request.method == 'POST':

        temp = request.POST.get('input_text')#서버의 데이터를 뽑아서 온다.
        model_instance = NewModel()
        model_instance.text = temp#이 값을 저장하는 데이터를 호풀해야함
        model_instance.save() #모델에 데이터를 저장한다.

        return HttpResponseRedirect(reverse('accountapp:hello_world'))#url을 nameing 해주는 것이다.
        #마지막 요청이 get으로 바뀐다.
    else:
        data_list = NewModel.objects.all()  # 이 모델의 모든 오브젝트드을 가지고 오겠다.

        return render(request, 'accountapp/hello_world.html', context={'data_list': data_list})
        #어떠한 주소로 들어갔을떄 이것을 볼수 있는지 확인


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'