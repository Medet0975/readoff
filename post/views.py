from django.shortcuts import render, get_object_or_404
from .models import Category, Books
from django.views import generic, View
from post.models import Books


def index_page(request):
    # return HttpResponse('Hello world')
    # title = request.GET.get('title')
    # posts = Books.objects.all()
    # if title:
    #     posts = Books.objects.filter(Q(name__icontains=title) |
    #                                 Q(description__icontains=title)
    #                                 )
    return render(request, "base_page.html", locals())


def head_page(request):
    # return render(request, "post/about.html", locals())
    return render(request, "shop.html", locals())


def books_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    books = Books.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        books = books.filter(category=category)
    return render(request,
                  'index.html',
                  {'category': category,
                   'categories': categories,
                   'books': books})


def books_detail(request, id, slug):
    book = get_object_or_404(Books,
                             id=id,
                             slug=slug,
                             available=True)
    return render(request,
                  'shop/product/detail.html',
                  {'product': book})


def categories_detail(request, id, slug):
    category = get_object_or_404(Books,
                                 id=Books.cat_id,
                                 slug=slug,
                                 )
    return render(request,
                  'shop/product/category.html',
                  {'product': Books})


class DetailPostView(generic.DetailView):
    template_name = 'detail_post.html'
    model = Books
    context_object_name = "book"


def get_book_from_category(request, pk):
    books_cat = Books.objects.filter(cat_id=pk)
    return render(request, "cat.html", locals())