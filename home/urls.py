from django.urls import path
from .views import homepage, about, getpost, createpost, editpost, deletepost, send_mail_view

urlpatterns = [
    path('',homepage, name='home'),
    path('about/',about, name='about'),
    path('getpost/<int:id>',getpost, name='post_details'),
    path('createpost/',createpost, name='create_post'),
    path('editpost/<int:id>',editpost, name='post_edit'),
    path('deletepost/<int:id>',deletepost, name='post_delete'),
    path('send_mail/', send_mail_view, name='send_mail'),
]