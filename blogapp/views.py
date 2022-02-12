from django.shortcuts import redirect, render
from .models import Categories, Articles
from django.contrib.auth.models import User
from . import forms
from django.contrib.auth.decorators import login_required


# Create your views here.


def indexview(request):
    articles=Articles.objects.all().order_by('-created')[:4] #? MUESTRA LOS ULTIMOS 4 ARTICULOS CREADOS
    return render(request, 'blogapp/index.html', {'articles':articles})


def allarticlesview(request):
    articles=Articles.objects.all().order_by('-created')
    categories=Categories.objects.all()
    return render(request, 'blogapp/all_articles.html', {'articles':articles, 'categories':categories})


def articledetailview(request, article_id):
    article=Articles.objects.get(id=article_id)
    return render(request, 'blogapp/article_detail.html', {'article':article})


def categoriesview(request, category_id):
    category=Categories.objects.get(id=category_id)
    categories=Categories.objects.exclude(id=category_id)
    articles=Articles.objects.filter(category=category)
    return render(request, 'blogapp/categories.html', {'category':category, 'articles':articles, 'categories':categories})


def authorview(request, author_id):
    global id_author
    id_author=author_id
    author=User.objects.get(id=author_id)
    articles=Articles.objects.filter(author=author).order_by('-created')
    categories=Categories.objects.all()
    return render(request, 'blogapp/author.html', {'author':author, 'articles':articles, 'categories':categories})


def aboutview(request):
    return render(request, 'blogapp/about.html')


@login_required(login_url='/accounts/login')
def createview(request):
    categories=Categories.objects.all()
    if request.method=="POST":
        form=forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.author=request.user
            instance.save()
            form.save_m2m()
            return redirect('/home/create/?valid')
        else:
            return redirect('/home/create/?novalid')
    else:
        form=forms.CreateArticle()
    return render(request, 'blogapp/createarticle.html', {'form':form, 'categories':categories})


def createcategoryview(request):
    if request.method=="POST":
        form=forms.CreateCategory(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/home/createcategory/?valid')
        else:
            return redirect('/home/createcategory/?novalid')
    else:
        form=forms.CreateCategory()
    return render(request, 'blogapp/createcategory.html', {'form':form})


def authorcategoryview(request, category_id):
    global id_author
    author=User.objects.get(id=id_author)
    category=Categories.objects.get(id=category_id)
    articles=Articles.objects.filter(author=author, category=category).order_by('-created')
    categories=Categories.objects.exclude(id=category_id)
    return render(request, 'blogapp/authorcategory.html', {'articles':articles, 'categories':categories, 'author':author})

