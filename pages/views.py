
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views import View
from article.models import Article


# Create your views here.

class HomePageView(View):
    def get(self,request):
        article=Article.objects.all().order_by('id')[0:6]
        paginator=Paginator(article,3)
        page_num=request.GET.get('page',1)
        page_obj=paginator.get_page(page_num)
        return render(request,'home.html',{'page_obj':page_obj})
