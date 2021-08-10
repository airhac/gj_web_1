from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from articleapp.decorators import article_ownership_required
from articleapp.forms import ArticleCreationForm
from articleapp.models import Article

decorator_list= [login_required,article_ownership_required]

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/create.html'

    def form_valid(self, form):
        form.instance.writer = self.request.user #로그인이 되어있다는 보장이 되어 있어야한다.
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})

        #self.object target article과 동일
class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'target_article'
    #우리가 볼려는 게시물의 객체
    template_name = 'articleapp/detail.html'

@method_decorator(decorator_list, 'get')
@method_decorator(decorator_list, 'post')
class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleCreationForm
    context_object_name = 'target_article'
    template_name = 'articleapp/update.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})

@method_decorator(decorator_list, 'get')
@method_decorator(decorator_list, 'post')
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'target_article'
    success_url = reverse_lazy('articleapp:list')
    template_name =  'articleapp/delete.html'

class ArticleListView(ListView):
    model = Article
    context_object_name = 'article_list' #게시글들을 담고 있는 list
    template_name = 'articleapp/list.html'
    paginate_by = 2