from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

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


def add_news(request):
    if request.method == 'POST':
        print("Hello")
        news_title = request.POST.get('news_title')
        print(news_title)
        news_description = request.POST.get('news_description')
        print(news_description)
        form = UploadImage(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.title = news_title
            form.news_description = news_description
            form.news_image = request.FILES['news_image']
            form.save()
            print(form.news_image)

        return render(request, 'add_news.html')  # Redirect to a success page after saving the news

    return render(request, 'add_news.html')
