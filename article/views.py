
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from article.forms import CommentForm
from article.models import Article,Comment



# Create your views here.

class PostPageView(View):
   def get(self,request):
       search_query=''
       if request.GET.get('q'):
           search_query=request.GET.get('q')
       posts = Article.objects.filter(title__icontains=search_query)
       return render(request,'article/post_view.html',{'object_list':posts})

class AddPostPageView( LoginRequiredMixin ,UserPassesTestMixin,CreateView):
    model = Article
    fields = ['title','summary','body','img']
    success_url = reverse_lazy('posts')
    template_name = 'article/add_postview.html'
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)



    def test_func(self):
        return self.request.user.is_superuser

class PostDetailView(View):
    def get(self,request,pk):
        article=Article.objects.get(id=pk)
        review_form=CommentForm()
        total_like =article.total_like()
        count=Comment.objects.filter(post=article.pk).count()
        return render(request,'article/post_detail.html',{'article':article,'from':review_form,'count':count,"total_like":total_like})

class LikePostView(LoginRequiredMixin,View):
    def post(self,request,pk):
        posts=get_object_or_404(Article,id=request.POST.get('post_id'))
        posts.like.add(request.user)
        return redirect(reverse('detail_posts', kwargs={'pk': posts.pk}))

class BookReview(LoginRequiredMixin,View):
    def post(self,request,pk):
        article = Article.objects.get(id=pk)
        review_form = CommentForm(data=request.POST)
        if review_form.is_valid():
            Comment.objects.create(
                post=article,
                user=request.user,
                comment=review_form.cleaned_data['comment']
            )
            return redirect(reverse('detail_posts',kwargs={'pk':article.pk}))
        return render(request, 'article/post_detail.html', {'article': article, 'from': review_form})


class PostEditView(LoginRequiredMixin ,UpdateView):
    model = Article
    fields = ['title','summary','body','img']
    template_name = 'article/post_edit.html'


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Article
    template_name = 'article/post_delete.html'
    success_url = reverse_lazy('posts')
