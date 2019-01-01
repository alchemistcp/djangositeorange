from django.contrib import admin
from django.urls import include, path
#from django.conf.urls import url

urlpatterns = [
    path(r'', include('blog.urls')),
    path(r'', include('comments.urls')),
    path(r'users/', include('users.urls')),
    path(r'admin/', admin.site.urls),
]
