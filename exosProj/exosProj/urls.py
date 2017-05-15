from django.conf.urls import url
from django.contrib import admin
from views import *

urlpatterns = [

    # List All Users
    url(r'^user/list/$', UserList.as_view(), name='user_list'),

    # User Detail
    url(r'^user/view/(?P<pk>\d+)/$', UserDetail.as_view(), name='user_detail'),

    # User Create
    url(r'^user/create/$', UserCreate.as_view( success_url='/user/list/' ), name='user_create'),
 
    # User Edit
    url(r'^user/update/(?P<pk>\d+)/$', UserUpdate.as_view( success_url='/user/list/'), name='user_update' ),

    # User Delete
    url(r'^user/delete/(?P<pk>\d+)/$', UserDelete.as_view( success_url='/user/list/'), name='user_delete' )
]
