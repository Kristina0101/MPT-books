from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/category/<int:category_id>/', views.category_books, name='category_books'),
    path('plans/', views.plans, name='plans'),
    path('catalog/description/<int:id>/', views.book_description, name='book_description'),
    path('category_description/<int:id>/', views.category_description, name='category_description'),
    path('add_to_favorites/', views.add_to_favorites, name='add_to_favorites')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)