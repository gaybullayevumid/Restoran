from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('service/', ServicePageView.as_view(), name='service'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('menu/', MenuPageView.as_view(), name='menu'),
    path('pages/', PagesView.as_view(), name='pages'),
    path('book/', BookPageView.as_view(), name='book'),
    path('team/', TeamPageView.as_view(), name='team'),
    path('testimonial/', TestimonialPageView.as_view(), name='testimonial'),
    path('contact/', ContactPageView.as_view(), name='contact'),
]
