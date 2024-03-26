from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from newsInfo.forms import SearchForms, UploadImage
from newsInfo.models import NewsModel, CategoryModel
from django.views.generic.list import ListView


class HomePage(ListView):
    form = SearchForms
    template_name = 'index.html'
    model = NewsModel
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories_list"] = CategoryModel.objects.all()
        context["news_list"] = NewsModel.objects.all()
        return context


def all_news(request):
    news_list = NewsModel.objects.all().order_by('id')
    categories_list = CategoryModel.objects.all()
    form = SearchForms
    return render(request, "index.html",
                  {"news_list": news_list, "categories_list": categories_list, "form": form})


class CategoriesPage(ListView):
    form = SearchForms
    paginate_by = 5
    template_name = "bad.html"
    context_object_name = "categories_page"
    model = NewsModel

    def get_queryset(self):
        value = self.kwargs.get("pk")

        query_set = NewsModel.objects.filter(news_category=value)
        return query_set


class NewsPage(ListView):
    template_name = "news.html"
    context_object_name = "news_page"
    model = NewsModel

    def get_queryset(self):
        value = self.kwargs.get("pk")
        query_set = NewsModel.objects.get(id=value)
        return query_set


class Login(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return "/"


def logout_view(request):
    logout(request)
    return redirect("all_news")


def get_insert(request):
    category = CategoryModel.objects.all()
    return render(request, "add_news.html", {"category": category})


class VideoCreateView(CreateView):
    model = NewsModel
    fields = []
    template_name = 'add_news.html'
    success_url = reverse_lazy('all_news')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = CategoryModel.objects.all()
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        news_title = self.request.POST.get('news_title')
        news_category_id = self.request.POST.get('news_category')
        news_image = self.request.FILES.get('news_image')
        news_description = self.request.POST.get("news_description")

        if news_image and news_category_id and news_title and news_description:
            category_instance = CategoryModel.objects.get(pk=news_category_id)
            form.instance.news_description = news_description
            form.instance.news_image = news_image
            form.instance.news_category = category_instance
            form.instance.news_title = news_title
            print('Success')
        else:
            return self.form_invalid(form)

        form.save()
        return super().form_valid(form)