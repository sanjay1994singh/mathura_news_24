from django.db import models

from category.models import Category


# Create your models here.
class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(upload_to='news_image', null=True, blank=True)
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        db_table = 'post'


class OtherNewsImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    other_image = models.ImageField(upload_to='other_news_image', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return str(self.post.title)

    class Meta:
        db_table = 'other_news_image'
