from django.shortcuts import render, redirect


# Create your views here.
def feeds(request):
    #로그인을 했다라면, 어떤 정보를 보내고,
    #로그인을 하지 않았다면, 로그인을 하도록 하자

    if not request.user.is_authenticated:

        return redirect('/users/login/') #redirect는 서버안에서 이루어짐, 빠르게 스위칭
    else:
        return render(request, 'posts/feeds.html')