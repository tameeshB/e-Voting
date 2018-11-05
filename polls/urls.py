from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('vote/', views.vote, name='vote'),
    # path('init/', views.vote, name='vote'),
    # path('/verify', views.verify, name='verify'),
    # path('/thanks', views.thanks, name='thanks'),
]
urlpatterns += staticfiles_urlpatterns()
