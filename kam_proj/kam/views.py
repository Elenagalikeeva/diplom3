from django.shortcuts import render, get_object_or_404, redirect
from .models import Kam, Vosho, Vse, More, Obzor, Rev
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from crm.models import Order
from crm.forms import OrderForm
from sample.sendmessage import send_telegram
from .forms import ReviewForm


def leave_review(request):
    if request.method == 'POST':
        form1 = ReviewForm(request.POST, request.FILES)
        if form1.is_valid():
            review = form1.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('index')
    else:
        form1 = ReviewForm()

    return render(request, 'kam/leave_review.html', {'form1': form1})


def carusel(request):
    return render(request, 'kam/carusel.html')


def index(request):
    projects = Kam.objects.all()
    reviews = Rev.objects.all()
    form = OrderForm()

    context = {
        'projects': projects,
        'form': form,
        'reviews': reviews,
    }

    return render(request, 'kam/index.html', context)


def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        element = Order(order_name=name, order_phone=phone)
        element.save()
        send_telegram(tg_name=name, tg_phone=phone)
        return render(request, 'kam/thanks.html', {'name': name})
    else:
        return render(request, 'kam/thanks.html')


def blogs(request):
    blogs = Kam.objects.all()
    return render(request, 'kam/blog.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Kam, pk=blog_id)
    return render(request, 'kam/details.html', {'blog': blog})


def kabinet(request):
    return render(request, 'kam/kabinet.html')


def vosho(request):
    vosho = Vosho.objects.all()
    return render(request, 'kam/vosho.html', {'vosho': vosho})


def more(request):
    more = More.objects.all()
    return render(request, 'kam/more.html', {'more': more})


def vse(request):
    vse = Vse.objects.all()
    return render(request, 'kam/vse.html', {'vse': vse})


def obzor(request):
    obzor = Obzor.objects.all()
    return render(request, 'kam/obzor.html', {'obzor': obzor})


def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('index')


def signupuser(request):
    if request.method == "GET":
        return render(request, 'kam/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('kab')

            except IntegrityError:
                return render(request, 'kam/signupuser.html', {'form': UserCreationForm(), 'error': \
                    'Такое имя пользователя уже существует. Задайте другое'})

        else:
            return render(request, 'kam/signupuser.html', {'form': UserCreationForm(), 'error': \
                'Пароли не совпадают'})


def loginuser(request):
    if request.method == "GET":
        return render(request, 'kam/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'kam/loginuser.html', {'form': AuthenticationForm(), 'error': \
                'Неверные данные'})
        else:
            login(request, user)
            return redirect('kab')
