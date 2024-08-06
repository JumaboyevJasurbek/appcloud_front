from django.db import models
from django.utils.text import slugify


# Create your models here.

class Main_page(models.Model):
    title_eng = models.CharField(max_length=56)
    title_ru = models.CharField(max_length=56)
    title_uz = models.CharField(max_length=56)
    short_title_eng = models.CharField(max_length=500)
    short_title_ru = models.CharField(max_length=500)
    short_title_uz = models.CharField(max_length=500)
    image1 = models.ImageField(upload_to='static/main_images', null=True, blank=True)
    image2 = models.ImageField(upload_to='static/main_images', null=True, blank=True)
    image3 = models.ImageField(upload_to='static/main_images', null=True, blank=True)
    image4 = models.ImageField(upload_to='static/main_images', null=True, blank=True)

    def __str__(self):
        return self.title_eng


class Rating(models.Model):
    years_of_experience = models.IntegerField(default=2000, blank=True, null=True)
    customers_worldwide = models.IntegerField(default=2000, blank=True, null=True)
    project_completed = models.IntegerField(default=2000, blank=True, null=True)

    def __str__(self):
        return str(self.years_of_experience) if self.years_of_experience is not None else 'No experience'


class Information_page(models.Model):
    title_uz = models.CharField(max_length=128)
    title_eng = models.CharField(max_length=128)
    title_ru = models.CharField(max_length=128)
    short_title_uz = models.CharField(max_length=500)
    short_title_ru = models.CharField(max_length=500)
    short_title_eng = models.CharField(max_length=500)
    video_link = models.URLField()

    def __str__(self):
        return self.title_uz


class Price(models.Model):
    price_month = models.IntegerField(default=0, null=True, blank=True)
    price_years = models.IntegerField(default=0, null=True, blank=True)

    title1_uz = models.CharField(max_length=256)
    title2_uz = models.CharField(max_length=256)
    title3_uz = models.CharField(max_length=256)
    title4_uz = models.CharField(max_length=256)
    title5_uz = models.CharField(max_length=256)

    title1_ru = models.CharField(max_length=256)
    title2_ru = models.CharField(max_length=256)
    title3_ru = models.CharField(max_length=256)
    title4_ru = models.CharField(max_length=256)
    title5_ru = models.CharField(max_length=256)

    title1_eng = models.CharField(max_length=256)
    title2_eng = models.CharField(max_length=256)
    title3_eng = models.CharField(max_length=256)
    title4_eng = models.CharField(max_length=256)
    title5_eng = models.CharField(max_length=256)

    def __str__(self):
        return str(self.price_month) if self.price_month is not None else 'No price'


class Team(models.Model):
    name_lastname = models.CharField(max_length=56, blank=True, null=True)
    job_name = models.CharField(max_length=182, blank=True, null=True)
    image = models.ImageField(upload_to='static/main_images', null=True, blank=True)

    def __str__(self):
        return self.name_lastname


class Blog_detail(models.Model):
    name_lastname = models.CharField(max_length=56, blank=True, null=True)
    ctg_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static/main_images', null=True)
    short_descriptions_uz = models.CharField(max_length=256, blank=True, null=True)
    short_descriptions_ru = models.CharField(max_length=256, blank=True, null=True)
    short_descriptions_eng = models.CharField(max_length=256, blank=True, null=True)
    data = models.DateTimeField()
    post_link = models.URLField()

    def __str__(self):
        return self.name_lastname


class Suggestion(models.Model):
    fullname = models.CharField(max_length=256)
    email = models.EmailField()
    phone = models.CharField(max_length=128)
    subject = models.TextField()

    def __str__(self):
        return self.fullname
