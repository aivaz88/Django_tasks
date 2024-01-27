from django.shortcuts import render, redirect
from django.http import HttpResponse
import logging
from .models import User, Product, Order
from .forms import RegistrationForm, LoginForm

logger = logging.getLogger(__name__)


def main(request):
    logger.info("Main page started")
    try:
        name = request.COOKIES['user_name']
    except:
        name = ''
    context = {
        'user_name': name,
    }
    return render(request, 'shopapp/main.html', context)


def about(request):
    logger.info("About page started")
    try:
        name = request.COOKIES['user_name']
    except:
        name = ''
    context = {
        'user_name': name,
    }
    return render(request, 'shopapp/about.html', context)


def contacts(request):
    logger.info("Contacts page started")
    try:
        name = request.COOKIES['user_name']
    except:
        name = ''
    context = {
        'user_name': name,
    }
    return render(request, 'shopapp/contacts.html', context)


def clothes(request):
    logger.info("Clothes page started")
    try:
        name = request.COOKIES['user_name']
    except:
        name = ''
    products = Product.objects.filter(type='clothes')
    context = {
        'user_name': name,
        'products': products,
    }
    return render(request, 'shopapp/products.html', context)


def shoes(request):
    logger.info("Shoes page started")
    try:
        name = request.COOKIES['user_name']
    except:
        name = ''
    products = Product.objects.filter(type='shoes')
    context = {
        'user_name': name,
        'products': products,
    }
    return render(request, 'shopapp/products.html', context)


def accessories(request):
    logger.info("Accessories page started")
    try:
        name = request.COOKIES['user_name']
    except:
        name = ''
    products = Product.objects.filter(type='accessories')
    context = {
        'user_name': name,
        'products': products,
    }
    return render(request, 'shopapp/products.html', context)


def item_card(request, pk):
    logger.info("Product card page started")
    try:
        name = request.COOKIES['user_name']
    except:
        name = ''
    product = Product.objects.filter(id=pk).first()
    context = {
        'user_name': name,
        'product': product,
    }
    return render(request, 'shopapp/item_card.html', context)


def registration_form(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User(name=form.cleaned_data['name'],
                        surname=form.cleaned_data['surname'],
                        telephone=form.cleaned_data['telephone'],
                        email=form.cleaned_data['email'],
                        address=form.cleaned_data['address'],
                        password=form.cleaned_data['password']
                        )
            user.save()
            logger.info(f'Зарегистрирован новый пользователь')
            response = redirect('/')
            response.set_cookie('user_name', user.name)
            response.set_cookie('user_email', user.email)
            return response
    else:
        form = RegistrationForm()
    return render(request, 'shopapp/registration.html/', {'form': form})


def login_form(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(email=form.cleaned_data['email']).first()
            if not (user is None) and (user.password == form.cleaned_data['password']):
                logger.info(f'Выполнен вход пользователя {user.id=}')
                response = redirect('/')
                response.set_cookie('user_name', user.name)
                response.set_cookie('user_email', user.email)
                return response
            else:
                form = LoginForm()
                return render(request, 'shopapp/login.html/', {'form': form,
                                                               'message': 'Не правильно ввели почту или пароль!'})
    else:
        form = LoginForm()
    return render(request, 'shopapp/login.html/', {'form': form})


def greeting(request):
    logger.info('Greeting page started')
    if request.method == 'POST':
        response = redirect('/')
        response.set_cookie('user_name')
        response.set_cookie('user_email')
        return response
    else:
        name = request.COOKIES['user_name']
        email = request.COOKIES['user_email']
        context = {
            'user_name': name,
            'user_email': email,
        }
    return render(request, 'shopapp/greeting.html', context)


def order_access(request, pk):
    context = {'user_name': ""}
    try:
        email = request.COOKIES['user_email']
    except:
        email = ""
        context['message'] = 'Заказ не оформлен! Выполните вход в систему'
    if email == "":
        context['message'] = 'Заказ не оформлен! Выполните вход в систему'
    else:
        user = User.objects.filter(email=email).first()
        product = Product.objects.filter(id=pk).first()
        context['user_name'] = user.name
        context['message'] = 'Поздравляем, заказ оформлен!'
        order = Order(total_price=product.price, customer_id=user.id)
        order.save()
        logger.info(f'Оформлен заказ')
    return render(request, 'shopapp/order_access.html/', context)
