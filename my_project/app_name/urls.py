from django.urls import include, path
from app_name import views

urlpatterns = [
    path('base',views.home,name='base'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('contact_form_submit',views.contact_form_submit,name='contact_form_submit'),
    path('all_data',views.all_data,name='all_data'),
    path('portfolio',views.portfolio,name='portfolio'),
]
 