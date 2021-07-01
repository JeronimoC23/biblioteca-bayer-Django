from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Page(models.Model):

    title= models.CharField(max_length=100, verbose_name="Title")
    content=RichTextField(verbose_name="Content")
    slug=models.CharField(verbose_name="Friendly URL", unique=True, max_length=250)
    order=models.IntegerField(verbose_name="Order", default=0)
    public=models.BooleanField(default=False,verbose_name="Public")
    created_at =models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"

    def __str__(self):
        return self.title
    