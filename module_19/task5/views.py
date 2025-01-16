from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserRegister

users = ['user1', 'user2', 'user3', 'user4', 'user5']


def sign_up_by_django(request):
    info = dict()

    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            repeat_password = request.POST.get("repeat_password")
            age = request.POST.get("age")
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                info['success'] = f"Приветствуем, {username}!"

    else:
        form = UserRegister()

    return render(request, 'task5/registration_page_2.html', {'form': form, 'info': info})

def sign_up_by_html(request):
    info = dict()

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        age = request.POST.get("age")
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            info['success'] = f"Приветствуем, {username}!"



    return render(request, 'task5/registration_page.html', {'info': info})