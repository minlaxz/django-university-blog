from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=25)

class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    categories = models.ManyToManyField('Category', related_name='posts')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self) -> str:
        return self.title