from django.db import models
from accounts.models import Owner


# Create your models here.

class Posts(models.Model):
    Owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='post_owner')
    description = models.TextField()
    image = models.ImageField(upload_to='post_images/')
    date_created = models.DateTimeField(auto_now_add=True)
    number_of_likes = models.IntegerField(default=0)
    number_of_comments = models.IntegerField(default=0)

    def __str__(self):
        return self.description


class Comment(models.Model):
    Owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='comment_Owner')
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comment_post')
    content = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Owner.username
