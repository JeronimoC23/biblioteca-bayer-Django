from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class SubCom(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = RichTextField(verbose_name="Descripcion")
    image = models.ImageField(default="null", verbose_name="Image",upload_to="articles")
    
    class Meta:
        verbose_name = "Subcomision"
        verbose_name_plural = "Subcomisiones"

    def __str__(self):
        return self.name
    
class Article(models.Model):

    title= models.CharField(max_length=100, verbose_name="Titulo")
    content=RichTextField(verbose_name="Contenido")
    slug=models.CharField(verbose_name="Friendly URL", unique=True, max_length=250)
    public=models.BooleanField(default=False,verbose_name="Publico?")
    created_at =models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")
    image = models.ImageField(default="null", verbose_name="Image",upload_to="articles")
    subcomision = models.ManyToManyField(SubCom, verbose_name="Subcomision", default="Equipo Biblioteca Bayer")
    author = models.CharField(max_length=50, verbose_name="Autor", default="La Bayer Band")
    

    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"
        ordering = ['-created_at']
        
    def __str__(self):
        return self.title



class Event(models.Model):
    
    title= models.CharField(max_length=80, verbose_name="Titulo")
    content=RichTextField(verbose_name="Contenido")
    slug=models.CharField(verbose_name="Friendly URL", unique=True, max_length=250)
    public=models.BooleanField(default=False,verbose_name="Public?")
    created_at =models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    image = models.ImageField(default="null", verbose_name="Image",upload_to="articles")
    author = models.CharField(max_length=50, verbose_name="Autor", default="La Bayer Band")
    fecha = models.DateField(verbose_name="Fecha del evento")

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ['fecha']
    def __str__(self):
        return self.title

