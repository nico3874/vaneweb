from django.shortcuts import render
from .models import News
from django.views.generic.base import TemplateView





# Create your views here.
class NewsView (TemplateView):
    template_name = "news/news.html"
    news = News
    
    def render_to_response(self, request, **response_kwargs):
        request=self.request
        return render (request,self.template_name, {'news':self.news.objects.all()})