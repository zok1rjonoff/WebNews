from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

from newsInfo.models import NewsModel, CategoryModel


def all_news(request):
    news_list = NewsModel.objects.all().order_by('id')
    categories_list = CategoryModel.objects.all()
    return render(request, "index.html", {"news_list": news_list,"categories_list":categories_list})


class Login(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return "/"


def logout_view(request):
    logout(request)
    return redirect("all_news")