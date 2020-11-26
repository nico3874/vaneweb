from .models import OfferCarruselChildren, OfferCarruselChildren2, OfferCarruselChildren3, OfferCarruselChildren4, OfferCarruselChildren5, OfferCarruselChildren6
from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class Category1 (TemplateView):
    template_name = "category/carrusel.html"
    category = OfferCarruselChildren
    
    def render_to_response(self, request, **response_kwargs):
        request=self.request
        return render (request,self.template_name, {'category':self.category.objects.last()})

class Category2(Category1):
    template_name = "category/carrusel_2.html"       
    category = OfferCarruselChildren2

class Category3(Category1):
    template_name = "category/carrusel_3.html"       
    category = OfferCarruselChildren3

class Category4(Category1):
    template_name = "category/carrusel_4.html"       
    category = OfferCarruselChildren4

class Category5(Category1):
    template_name = "category/carrusel_5.html"       
    category = OfferCarruselChildren5

class Category6(Category1):
    template_name = "category/carrusel_6.html"       
    category = OfferCarruselChildren6