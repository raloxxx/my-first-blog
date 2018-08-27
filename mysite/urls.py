from django.contrib import admin
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

urlpatterns = [
    url('', include('blog.urls')),
    url('admin/', admin.site.urls),
    url('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    url('accounts/logout/', auth_views.LoginView.as_view(), name='logout', kwargs={'next_page': '/'}),
    
]
