from django import forms
class Userform(forms.Form):
    name = forms.CharField(max_length=20,min_length=1,label="用户名")
    age = forms.CharField(max_length=20,min_length=1,label="年龄")
    password = forms.CharField(max_length=20,min_length=1,label="密码")