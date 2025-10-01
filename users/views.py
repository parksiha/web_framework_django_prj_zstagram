from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from users.forms import LoginfForm, SignupForm

from users.models import User

# Create your views here.
# info is below:
#     view : login_view
#     templates : users/login.html
#     URL : /user/login/

def login_view(request):

    if request.user.is_authenticated:
        return redirect('/posts/feeds/') #redirect는 서버안에서 이루어짐, 빠르게 스위칭

    # 인증받지 않았다면
    if request.method == "GET":
        form = LoginfForm()
        context = {"form":form,}

        return render(request, "users/login.html", context)
    else:
        # POST로 전달이 된 경우,
        form = LoginfForm(data=request.POST) # (request.POST["username"], request.POST["password"])

        #전달된 데이터에 대한 유효성 검사
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect("/posts/feeds/")
            else:
                form.add_error(None, "입력한 계정정보가 존재하지 않습니다.")

        context = {"form": form,}
        return render(request, "users/login.html", context)

def logout_view(request):
    logout(request)
    return redirect("/users/login/")

def signup(request):
    if request.method == "POST":
        form = SignupForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/posts/feeds/")
    else:
        form = SignupForm()

    context = {"form":form}
    return render(request, "users/signup.html", context)