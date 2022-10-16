from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse

from accounts.models import CostumUser


# Create your models here.

class Article(models.Model):
    title=models.CharField(max_length=150)
    summary=models.CharField(max_length=200)
    body=RichTextUploadingField()
    img=models.ImageField(default='photo.jpeg',blank=True)
    creatad_at=models.DateTimeField(auto_now_add=True)
    like=models.ManyToManyField(CostumUser,related_name='blog_post')
    author=models.ForeignKey(
        CostumUser,on_delete=models.CASCADE
    )
    def total_like(self):
        return self.like.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_posts',args=[str(self.id)])
class Comment(models.Model):
    post=models.ForeignKey(Article,on_delete=models.CASCADE)
    comment=models.TextField()
    user=models.ForeignKey(CostumUser,on_delete=models.CASCADE)
    creted_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.title