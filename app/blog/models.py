from django.db import models

# Create your models here.
class Writer(models.Model):
    id = models.IntegerField(primary_key=True)
    age = models.IntegerField()
    name = models.CharField(max_length=100, blank=False)
    email = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=1000, blank=False)

    class Meta:
        ordering = ['name']


class Writer(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200, blank=False)
    excerpt = models.CharField(max_length=100, blank=False)
    text = models.CharField(max_length=1000, blank=False)
    date_created = models.DateTimeField(auto_now=True)
    date_updates = models.DateTimeField(auto_now=True)
    # image = models.ImageField()
    writer = models.ForeignKey(Writer, related_name='writer', on_delete=models.PROTECT)

    class Meta:
        ordering = ['title']

