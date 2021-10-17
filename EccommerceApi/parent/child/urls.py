
from django.urls import path
from .views import *

urlpatterns = [
    path("book/", BookListView.as_view(), name="book"),
    path("book/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("category/", CategoryListView.as_view(), name="category"),
    path("category/<int:pk>/", CategoryDetailView.as_view(), name="category-detail"),
    path("product/", ProductListView.as_view(), name="product"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
]
