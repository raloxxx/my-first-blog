from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
	url('', include('blog.urls')),
    url('admin/', admin.site.urls)
    
]
