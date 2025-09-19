from django.urls import path
from .views import post_list , post_details , new_post , edit_post , delete_post

app_name = 'posts'

urlpatterns = [
    path('',post_list , name = 'post_list'),
    path('<int:id>' , post_details , name = 'post_details'),
    path('new' , new_post , name = 'new_post'),
    path('<int:id>/edit' , edit_post , name = 'edit_post'),
    path('<int:id>/delete' , delete_post , name = 'delete_post')
]
