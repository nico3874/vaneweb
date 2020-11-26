from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class OfferCarruselChildren (models.Model):
    
    image_1= models.ImageField(verbose_name="Imagen 1", upload_to='category')
    image_2= models.ImageField(verbose_name="Imagen 2", upload_to='category')
    image_3= models.ImageField(verbose_name="Imagen 3", upload_to='category')
    offer_1= RichTextField(verbose_name="Combo_1",null=True, blank=True)
    offer_2= RichTextField(verbose_name="Combo_2",null=True, blank=True)
    
    created= models.DateTimeField(auto_now_add="True")
    

    class Meta:
        verbose_name= "Carrusel y Oferta"
        verbose_name_plural= "Newborn"

    def __str__(self):
        return "Oferta del {}".format(self.created.strftime("%d/%m/%Y"))

class OfferCarruselChildren2 (models.Model):
    
    image_1= models.ImageField(verbose_name="Imagen 1", upload_to='category')
    image_2= models.ImageField(verbose_name="Imagen 2", upload_to='category')
    image_3= models.ImageField(verbose_name="Imagen 3", upload_to='category')
    offer_1=  RichTextField(verbose_name="Combo_1",null=True, blank=True)
    offer_2=  RichTextField(verbose_name="Combo_2",null=True, blank=True)
    
    created= models.DateTimeField(auto_now_add="True")
    

    class Meta:
        verbose_name= "Carrusel y Oferta"
        verbose_name_plural= "Mini baby"

    def __str__(self):
        return "Oferta del {}".format(self.created.strftime("%d/%m/%Y"))


class OfferCarruselChildren3 (models.Model):
    
    image_1= models.ImageField(verbose_name="Imagen 1", upload_to='category')
    image_2= models.ImageField(verbose_name="Imagen 2", upload_to='category')
    image_3= models.ImageField(verbose_name="Imagen 3", upload_to='category')
    offer_1= RichTextField(verbose_name="Paquete Fine Art", null=True, blank=True)
   
    created= models.DateTimeField(auto_now_add="True")
    

    class Meta:
        verbose_name= "Carrusel y Oferta"
        verbose_name_plural= "Fine Art "

    def __str__(self):
        return "Oferta del {}".format(self.created.strftime("%d/%m/%Y"))

class OfferCarruselChildren4 (models.Model):
    
    image_1= models.ImageField(verbose_name="Imagen 1", upload_to='category')
    image_2= models.ImageField(verbose_name="Imagen 2", upload_to='category')
    image_3= models.ImageField(verbose_name="Imagen 3", upload_to='category')
    offer_1=  RichTextField(verbose_name="Combo_1",null=True, blank=True)
    offer_2=  RichTextField(verbose_name="Combo_2",null=True, blank=True)
    
    created= models.DateTimeField(auto_now_add="True")
    

    class Meta:
        verbose_name= "Carrusel y Oferta"
        verbose_name_plural= "Hermanitos"

    def __str__(self):
        return "Oferta del {}".format(self.created.strftime("%d/%m/%Y"))

class OfferCarruselChildren5 (models.Model):
    
    image_1= models.ImageField(verbose_name="Imagen 1", upload_to='category')
    image_2= models.ImageField(verbose_name="Imagen 2", upload_to='category')
    image_3= models.ImageField(verbose_name="Imagen 3", upload_to='category')
    offer_1= RichTextField(verbose_name="Combo_1", null=True, blank=True)
    offer_2= RichTextField(verbose_name="Combo_2", null=True, blank=True)
   
    created= models.DateTimeField(auto_now_add="True")
    

    class Meta:
        verbose_name= "Carrusel y Oferta"
        verbose_name_plural= "Maternidad"

    def __str__(self):
        return "Oferta del {}".format(self.created.strftime("%d/%m/%Y"))

class OfferCarruselChildren6 (models.Model):
    
    image_1= models.ImageField(verbose_name="Imagen 1", upload_to='category')
    image_2= models.ImageField(verbose_name="Imagen 2", upload_to='category')
    image_3= models.ImageField(verbose_name="Imagen 3", upload_to='category')
    offer_1= RichTextField(verbose_name="Paquete Familiar", null=True, blank=True)
    
   
    created= models.DateTimeField(auto_now_add="True")
    

    class Meta:
        verbose_name= "Carrusel y Oferta"
        verbose_name_plural= "Familia"

    def __str__(self):
        return "Oferta del {}".format(self.created.strftime("%d/%m/%Y"))        

    