from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# 로그인하면 DB에 저장해서 무결성 확인 및 이후 경로 설정
class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")

