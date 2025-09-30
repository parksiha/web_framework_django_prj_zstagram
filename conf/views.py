from django.shortcuts import render, redirect

def index(request):
    '''
    if request.user.is_authenticated:
        return redirect('/posts/feeds/') #redirect는 서버안에서 이루어짐, 빠르게 스위칭
    else:
        return render(request, "users/login.html")
        '''
    return render(request, 'index.html')