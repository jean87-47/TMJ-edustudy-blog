
from django.contrib import admin
from django.urls import path,include
from posts import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url




urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('posts/',include('posts.urls')),
   #path('', views.index,name='index'),
    path('',views.key,name='key'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    url(r'^static/(?P<path>.*)', serve, kwargs={'insecure': True}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


