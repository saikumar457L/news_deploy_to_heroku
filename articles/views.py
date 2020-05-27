from django.shortcuts import render

from django.views.generic import TemplateView,DetailView,ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from .models import Article

# Create your views here.

class ArticlesHome(ListView):
    model = Article
    template_name = "articles/articles_home.html"

class ArticleDetail (DetailView):
    model = Article
    template_name = "articles/articles_detail.html"



class ArticleCreate(LoginRequiredMixin,CreateView):
    model = Article
    template_name = "articles/articles_new.html"
    fields = ["title","body"]
    login_url = "login"

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class ArticleUpdate(LoginRequiredMixin,UpdateView):
    model = Article
    template_name = "articles/articles_edit.html"
    fields = ["title","body"]
    login_url = 'login'

    def dispatch (self,request,*args,**kwargs):
        get_user = self.get_object() # get all users
        user  = self.request.user # get current user

        if get_user != user: # checking the user match
            return render(request,"articles/articles_warn.html")
        return super().dispatch(request,*args, **kwargs)

class ArticleDelete(DeleteView):
    model = Article
    template_name = "articles/articles_delete.html"
    success_url = reverse_lazy("article:home")
    login_url = 'login'

    def dispatch(self,request,*args, **kwargs):
        get_users = self.get_object() # get all users
        user = self.request.user # get current user

        if get_users != user:
            raise PermissionDenied
        return super().dispatch(request,*args,**kwargs)


class ArticleWarn(TemplateView):
    template_name = "articles/articles_warn.html"
