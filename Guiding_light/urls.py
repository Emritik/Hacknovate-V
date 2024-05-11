from django.urls import path
from . import views
urlpatterns = [
   path('',views.index,name='home'),
   path('contact',views.contact,name='contact'),
   path('appointment',views.appointment,name='appointment'),
   path('features',views.features,name='features'),
   path('testimonial',views.testimonial,name='testimonial'),
   path('about',views.about,name='about'),
   path('service',views.service,name='service'),
   path('team',views.team,name='team'),
]
