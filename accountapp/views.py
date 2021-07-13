from django.http import HttpResponse
from django.shortcuts import render

from accountapp.models import NewModel


def hello_world(request):
    if request.method == 'POST':

        temp = request.POST.get('input_text')#서버의 데이터를 뽑아서 온다.
        model_instance = NewModel()
        model_instance.text = temp#이 값을 저장하는 데이터를 호풀해야함
        model_instance.save() #모델에 데이터를 저장한다.

        data_list = NewModel.objects.all() #이 모델의 모든 오브젝트드을 가지고 오겠다.


        return render(request,'accountapp/hello_world.html', context={'data_list': data_list})
    else:
        data_list = NewModel.objects.all()  # 이 모델의 모든 오브젝트드을 가지고 오겠다.

        return render(request, 'accountapp/hello_world.html', context={'data_list': data_list})
#어떠한 주소로 들어갔을떄 이것을 볼수 있는지 확인