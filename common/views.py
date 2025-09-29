from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from common.forms import UserForm

# 로그아웃 시의 화면 링크
def logout_view(request):
    logout(request)
    # return redirect('index') # 질문 리스트로 이동
    form = UserForm()
    return render(request, 'common/login.html', {'form': form}) # 로그인 페이지로 이동

# 회원가입 시의 화면 링크
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})
