from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



app_name='posts'

urlpatterns = [
    path('stark/',views.index, name='index'),
    path('schedule/',views.schedule, name='schedule'),
    path('introduction/',views.introduction,name='introduction'),
    path('<int:pk>/',views.detail,name='detail'),
    path('listi/',views.list,name='list'),
    path('create/',views.create,name='create'),
    path('<int:pk>/delete/',views.delete,name='delete'),
    path('<int:pk>/edit/',views.edit,name='edit'),
    path('<int:pk>/comments/',views.comments_create,name='comments_create'),
    path('comments/<int:pk>/delete/',views.comment_delete,name='comment_delete'),
    path('category/',views.category_list,name='category_list'),
    path('category/<int:pk>/',views.category,name='category'),






] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
