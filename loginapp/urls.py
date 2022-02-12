from django.urls import path
from . import views


app_name='accounts'


urlpatterns = [
    path('signup/', views.signupview, name="signup"),
    path('login/', views.loginview, name="login"),
    path('logout/', views.logoutview, name='logout'),
    path('signup/saveinfo/', views.saveinfoview, name='saveinfo'),
]

