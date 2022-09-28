from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.urls import reverse
from .models import Category
from post.models import Books
from post.forms import CreatePostForm



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
def detail_post(request, books_detail):
    book = get_object_or_404(Books, slug=books_detail)
    return render(request,
                  'detail_post.html',
                  locals())



def get_book_from_category(request, pk):
    books_cat = Books.objects.filter(cat_id=pk)
    return render(request, "cat.html", locals())


class CreatePostView(generic.CreateView):
    template_name = 'create_post.html'
    model = Books
    form_class = CreatePostForm

    def form_valid(self, form):
        form.instance.author =self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')

def post_search(request):
    form = SearchForm()
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            cd = form.cleaned_data
            results = SearchQuerySet().models(Post).filter(content=cd['query']).load_all()
            # count total results
            total_results = results.count()
    return render(request,
                  'blog/post/search.html',
                  {'form': form,
                   'cd': cd,
                   'results': results,
                   'total_results': total_results})

def get_cabinet(request):
    sur_name=request.GET.get('name', None)
    authors = Books.objects.all().order_by('id')
    if sur_name:
        books = Books.objects.filter(name__icontains=sur_name).order_by('id')


    print(request)
    return render(request, 'index.html', locals())
