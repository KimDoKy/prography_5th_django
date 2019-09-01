from django.urls import path
from . import views

app_name = 'boards'

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('write/', views.PostNew.as_view(), name='post_new'),
    path('<pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('<pk>/edit/', views.PostEdit.as_view(), name='post_edit'),
    path('<pk>/del/', views.PostDelete.as_view(), name='post_del'),
    path('<pk>/comment/create/', views.comment_create, name='comment_create'),
]
