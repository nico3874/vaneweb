from django.urls import path
from .views import Category1, Category2, Category3, Category4, Category5, Category6

urlpatterns = [
path('newborn/', Category1.as_view(), name='newborn'),
path('minibaby/', Category2.as_view(), name='minibaby'),
path('fineart/', Category3.as_view(), name='fineart'),
path('brothers/', Category4.as_view(), name='brothers'),
path('maternity/', Category5.as_view(), name='maternity'),
path('family/', Category6.as_view(), name='family'),

]