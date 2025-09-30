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
        context = {
            "form":form,
        }

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

        context = {
            "form": form,
        }
        return render(request, "users/login.html", context)

def logout_view(request):
    logout(request)
    return redirect("/users/login/")

def signup(request):
    if request.method == "GET":
        form = SignupForm()
        context = {
            "form": form,
        }
        return render(request, "users/signup.html", context)
    else:
        form = SignupForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            profile_image = form.cleaned_data['profile_image']
            short_description = form.cleaned_data['short_description']

            if password1 != password2:
                form.add_error("password2", "비밀번호와 비밀번호 확인의 값이 다름")

            # username이 사용중인지? 아닌지?
            if User.objects.filter(username=username).exists():
                form.add_error(None, "이미 사용중인 username입니다.")

            if form.errors:
                context = {
                    "form": form,
                }
                return render(request, "users/signup.html", context)
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password1,
                    profile_image=profile_image,
                    short_description=short_description,
                )
                login(request, user)
                return redirect("/posts/feeds/")

        context = {
            "form": form,
        }
        return render(request, "users/signup.html", context)