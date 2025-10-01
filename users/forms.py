from django import forms
from users.models import User
from django.core.exceptions import ValidationError

class LoginfForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        widget=forms.TextInput(
            attrs={"placeholder":"사용자명 (3자리 이상)"},
        ),)
    password = forms.CharField(
        min_length=4,
        widget=forms.PasswordInput(
            attrs={"placeholder":"비밀번호는 4자리 이상)"},
        ),)


class SignupForm(forms.Form):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    profile_image = forms.ImageField()
    short_description = forms.CharField()


    # 유효성섬사를 하기 위한 방법을 제공함
    # 하나의 멤버변수에 대해서 유효성 검사를 하는 함수명을 "clean_필드명" 이 형식으로 생성하자
    def clean_username(self):
        username = self.cleaned_data["username"]

        # username이 사용중인지? 아닌지?
        if User.objects.filter(username=username).exists():
            raise ValidationError(f"{username}: 해당 username은 이미 사용중 입니다.")
        return username

    # 2개 이상의 멤버변수값에 대한 유효성 혹은 어떤처리를 하기 위해서는
    # "clean_변수명" -> 이 룰로 함수를 만들 수 없다.
    # --> 전체검사를 하기 위한 함수는 "clean"이를으로 함수를 생성
    def clean(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if password1 != password2:
            self.add_error("password2", "비밀번호와 비밀번호 확인의 값이 다름")

    def save(self):
        username = self.cleaned_data["username"]
        password1 = self.cleaned_data["password1"]
        profile_image = self.cleaned_data["profile_image"]
        short_description = self.cleaned_data["short_description"]

        user = User.objects.create_user(
            username=username,
            password=password1,
            profile_image=profile_image,
            short_description=short_description,
        )

        return user