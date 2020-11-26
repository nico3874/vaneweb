from django.db import models
from ckeditor.fields import RichTextField 
# Create your models here.
class News (models.Model):
    title = models.CharField (verbose_name="Título", max_length=100)
    content = RichTextField(verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imagen", upload_to='news')
    created= models.DateTimeField(auto_now_add="True")
    update= models.DateTimeField(auto_now="True")

    class Meta:
        verbose_name= "Noticia"
        verbose_name_plural= "Noticias"
        ordering= ["-created"]

    def __str__(self):
        return self.title
