from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import *
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required




# Create your views here.

def base(request):
    return render(request, 'books/base.html')

def main_page(request):
    categories = Category.objects.all()
    return render(request, 'books/main_page.html', {'categories': categories})

def catalog(request):
    categories = Category.objects.all()
    books = book.objects.all()
    return render(request, 'books/catalog.html', {'categories': categories, 'books': books})

def category_books(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    books = book.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'books/catalog.html', {'categories': categories, 'books': books})

@login_required
def plans(request):
    user_favorites = in_planes.objects.filter(user=request.user)
    favorite_books = [favorite.id_books for favorite in user_favorites]
    return render(request, 'books/plans.html', {'favorite_books': favorite_books})

def login(request):
    return render(request, 'books/login.html')

def book_description(request, id):
    books = book.objects.get(pk=id)
    return render(request, 'books/book_description.html', {'books': books})

def category_description(request, id):
    category = get_object_or_404(Category, pk=id)
    books = book.objects.filter(category=category)
    return render(request, 'books/category_description.html', {'category': category, 'books': books})

def add_to_favorites(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            book_id = request.POST.get('book_id')
            book_instance = get_object_or_404(book, pk=book_id)
            
            # Проверяем, добавлена ли книга в избранное пользователем
            favorite_books = in_planes.objects.filter(user=request.user, id_books=book_instance)
            
            if favorite_books.exists():
                # Если книга уже была добавлена ранее
                messages.warning(request, "Эта книга уже есть в вашем списке избранных.")
            else:
                # Если книга не была добавлена ранее, создаем новую запись
                in_planes.objects.create(user=request.user, id_books=book_instance)
                messages.success(request, "Книга успешно добавлена в избранное.")
                
            return redirect('book_description', id=book_id)
        else:
            # Обработка случая, когда пользователь не аутентифицирован
            # Можно например перенаправить его на страницу входа или регистрации
            return redirect('login')  # Нужно заменить на ваше представление для входа/регистрации
    return redirect('main_page')  # Обработка GET запросов
