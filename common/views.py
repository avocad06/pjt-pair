from django.shortcuts import render, redirect
from .models import Common
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
def register(request):
    if request.method == "GET":
        return render(request, "common/register.html")

    elif request.method == "POST":
        name = request.POST.get("user_name", None)
        password = request.POST.get("password", None)
        re_password = request.POST.get("re_password", None)
        res_data = {}

        # 입력값이 비었을 경우
        if not (name and password and re_password):
            res_data["eroor"] = "모든 값을 입력해야 합니다."
        if password != re_password:
            res_data["error"] = "비밀번호가 다릅니다."
        # 입력값이 양식에 맞게 입력되었을 경우
        else:
            common = Common(name=name, password=make_password(password))
            common.save()
        return render(request, "common/register.html", res_data)


def login(request):
    response_data = {}

    # 로그인 화면을 요청했다면,
    if request.method == "GET":
        return render(request, "common/login.html")

    # 로그인 화면에 입력한 거라면,
    elif request.method == "POST":
        login_username = request.POST.get("user_name", None)
        login_password = request.POST.get("password", None)

        # 입력된 값이 없다면
        if not (login_username and login_password):
            response_data["error"] = "아이디와 비밀번호를 모두 입력해 주세요."

        # 양식에 맞게 입력되었다면,
        else:
            # 로그인한 사용자와 아이디가 일치하는 DB를 꺼내온다.
            common = Common.objects.get(name=login_username)

            if check_password(login_password, common.password):
                request.session["user"] = common.id

                return redirect("review:index")

        return render(request, "common/login.html", response_data)


def home(request):
    user_id = request.session.get("user")

    # 사용자가 로그인한 상태라면(user_id가 세션에 있다면)
    if user_id:
        common_info = Common.objects.get(pk=user_id)
        # 사용자의 이름을 출력한다
        return HttpResponse(common_info.name)

    return HttpResponse("로그인을 해 주세요.")


def logout(request):
    # 사용자가 로그아웃을 요청한다면,
    # 세션에서 제거한다.
    request.session.pop("user")
    return redirect("review:index")
