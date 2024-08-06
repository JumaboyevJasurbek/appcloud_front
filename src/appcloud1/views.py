from django.shortcuts import render, redirect

from .forms import SuggestionForm
from .models import Main_page, Rating, Information_page, Price, Blog_detail, Team, Suggestion


# Create your views here.


def index(requests):
    main_page = Main_page.objects.all()
    rating_department = Rating.objects.all()
    informationpage = Information_page.objects.all()
    price_department = Price.objects.all()
    team_department = Team.objects.all()
    blog_detail = Blog_detail.objects.all()
    contact_department = Suggestion.objects.all()

    ctx = {
        "main_page": main_page,
        "rating_department": rating_department,
        "informationpage": informationpage,
        "price_department": price_department,
        "team_department": team_department,
        "blog_detail": blog_detail,
        "contact_department": contact_department,
    }
    return render(requests, 'index.html', ctx)


def RussianPage(requests):
    main_page = Main_page.objects.all()
    rating_department = Rating.objects.all()
    informationpage = Information_page.objects.all()
    price_department = Price.objects.all()
    team_department = Team.objects.all()
    blog_detail = Blog_detail.objects.all()
    contact_department = Suggestion.objects.all()

    ctx = {
        "main_page": main_page,
        "rating_department": rating_department,
        "informationpage": informationpage,
        "price_department": price_department,
        "team_department": team_department,
        "blog_detail": blog_detail,
        "contact_department": contact_department,
    }
    return render(requests, 'index_ru.html', ctx)


def EnglishPage(requests):
    main_page = Main_page.objects.all()
    rating_department = Rating.objects.all()
    informationpage = Information_page.objects.all()
    price_department = Price.objects.all()
    team_department = Team.objects.all()
    blog_detail = Blog_detail.objects.all()
    contact_department = Suggestion.objects.all()

    ctx = {
        "main_page": main_page,
        "rating_department": rating_department,
        "informationpage": informationpage,
        "price_department": price_department,
        "team_department": team_department,
        "blog_detail": blog_detail,
        "contact_department": contact_department,
    }
    return render(requests, 'index_eng.html', ctx)


def ContactUzb(request):
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('contact_uz')  # Redirect to a success page or the same page
    else:
        form = SuggestionForm()

    return render(request, 'contact_uz.html', {'form': form})


def ContactRus(request):
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('contact_ru')  # Redirect to a success page or the same page
    else:
        form = SuggestionForm()

    return render(request, 'contact_ru.html', {'form': form})


def ContactEng(request):
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('contact_eng')  # Redirect to a success page or the same page
    else:
        form = SuggestionForm()

    return render(request, 'contact_eng.html', {'form': form})
