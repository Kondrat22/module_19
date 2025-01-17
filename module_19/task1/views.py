from django.shortcuts import render
from .forms import UserRegister
from .models import Buyer, Game, News
from django.core.paginator import Paginator


def news(request):
    news = News.objects.all().order_by('-date')
    paginator = Paginator(news, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'task1/news.html', {'page_obj': page_obj})

def platform(request):
    context = {
        'title': 'Главная страница',
    }
    return render(request, template_name='task1/platform.html', context=context)

def shop(request):
    games = Game.objects.all()

    context = {
        'title': 'Игры',
        'games': games,
    }

    return render(request, template_name='task1/shop.html', context=context)

def bag(request):
    context = {
        'title': 'Корзина',
    }
    return render(request, template_name='task1/bag.html', context=context)



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
            buyer = Buyer.objects.filter(name=username).first()
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                info['success'] = f"Приветствуем, {username}!"
            if not buyer:
                Buyer.objects.create(name=username, age=age, balance=0.00)

    else:
        form = UserRegister()

    return render(request, 'task1/registration_page_2.html', {'form': form, 'info': info})

def sign_up_by_html(request):
    info = dict()

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        age = request.POST.get("age")
        buyer = Buyer.objects.filter(name=username).first()
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            info['success'] = f"Приветствуем, {username}!"
        if not buyer:
            Buyer.objects.create(name=username, age=age, balance=0.00)



    return render(request, 'task1/registration_page.html', {'info': info})

