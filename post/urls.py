from django.urls import path
from . import views

urlpatterns = [
    path('', views.books_list, name='books_list'),
    path("detail/post/<int:pk>/", views.DetailPostView.as_view(), name="detail_post"),
    path("detail/books-genre/<int:pk>/", views.get_book_from_category, name="detail_category"),

]
