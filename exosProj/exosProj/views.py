from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User

class UserList(ListView):
    model = User
    template_name = 'user_list.html'


class UserDetail(DetailView):
    model = User
    template_name = 'user_detail.html'


class UserCreate(CreateView):
    model = User
    fields = ['username','first_name','last_name','password','birthday']
    template_name = 'user_create.html'


class UserUpdate(UpdateView):
    model = User
    template_name = 'user_update.html'
    fields = ['username','first_name','last_name','password','birthday']


class UserDelete(DeleteView):
    model = User
    template_name = 'user_delete.html'
