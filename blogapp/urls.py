from django.urls import path
from . import views


app_name='articles'


urlpatterns = [
    path('', views.indexview, name='home'),
    path('articles/', views.allarticlesview, name='allarticles'),
    path('articles/<int:article_id>', views.articledetailview, name='detail'),
    path('categories/<int:category_id>', views.categoriesview, name='category'),
    path('author/<int:author_id>', views.authorview, name='author'),
    path('about/', views.aboutview, name='about'),
    path('create/', views.createview, name='create'),
    path('createcategory/', views.createcategoryview, name='createcategory'),
    path('author/category/<int:category_id>', views.authorcategoryview, name='authorcategory'),
]

