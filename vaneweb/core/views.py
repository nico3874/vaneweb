from django.views.generic.base import TemplateView


# Create your views here.

class BaseView(TemplateView):

    template_name = "core/index.html"
    
class AboutView(TemplateView):

    template_name = "core/about.html"

class CookiesView(TemplateView):

    template_name = "core/cookies.html"

class ConditionsView(TemplateView):

    template_name = "core/conditions.html"




