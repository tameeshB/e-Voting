from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('vote/', views.vote, name='vote'),
    # path('/verify', views.verify, name='verify'),
    # path('/thanks', views.thanks, name='thanks'),
]