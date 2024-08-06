from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name="home"),
    path('ru/', RussianPage, name="home_ru"),
    path('eng/', EnglishPage, name="home_eng"),

    path('uz/contact/', ContactUzb, name="contact_uz"),
    path('ru/contact/', ContactRus, name="contact_ru"),
    path('eng/contact/', ContactEng, name="contact_eng"),
]



