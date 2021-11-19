from django.shortcuts import redirect, render

from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()

    context = {
        'articles' : articles
    }

    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    article = Article(title=title,  content=content)
    article.save()

    return redirect('/articles/')

def detail(request, pk):
    article = Article.objects.get(pk=pk)

    context = {
        'article' : article
    }

    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()

    return redirect('/articles/')

def edit(request, pk):
    article = Article.objects.get(pk=pk)

    context = {
        'article' : article
    }

    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)

    title = request.GET.get('title')
    content = request.GET.get('content')

    article.title = title
    article.content = content

    article.save()

    return redirect(f'/articles/{article.pk}/')