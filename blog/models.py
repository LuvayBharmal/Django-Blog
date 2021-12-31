from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug=models.CharField(max_length=130)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    username = models.CharField(max_length=50)
    message = models.TextField()
    date_comment = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    #username = models.ForeignKey(User, on_delete=models.CASCADE,related_name='comments')
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ('-date_comment',)
    
    def __str__(self):
        return self.message