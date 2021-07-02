from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
    return render(request,'accountapp/hello_world.html')
#어떠한 주소로 들어갔을떄 이것을 볼수 있는지 확인