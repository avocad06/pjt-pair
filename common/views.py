from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .models import Common
# Create your views here.
def register(request):
    if request.method == 'GET':
        return render(request, 'common/register.html')
    
    elif request.method == 'POST':
        name = request.POST.get('user_name', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re_password', None)
        res_data = {}
        
        # 입력값이 비었을 경우
        if not (name and password and re_password):
            res_data['eroor'] = '모든 값을 입력해야 합니다.'
        if password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        # 입력값이 양식에 맞게 입력되었을 경우
        else:
            common = Common(name=name, password=make_password(password))
            common.save()
        return render(request, 'common/register.html', res_data)