from django.urls import path
from .views import homepage, about, getpost, createpost, editpost, deletepost

urlpatterns = [
    path('',homepage, name='home'),
    path('about/',about, name='about'),
    path('getpost/<int:id>',getpost, name='post_details'),
    path('createpost/',createpost, name='create_post'),
    path('editpost/<int:id>',editpost, name='post_edit'),
    path('deletepost/<int:id>',deletepost, name='post_delete')
]