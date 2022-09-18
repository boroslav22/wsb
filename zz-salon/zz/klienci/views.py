from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .models import Zwierze, Wizyty
import datetime
from datetime import timedelta
from .forms import ZwierzeForm, WizytyForm
from django.http import HttpResponseRedirect
import calendar
from calendar import HTMLCalendar
# Create your views here.

def index(request):
    now = datetime.date.today()
    today_pets = Wizyty.objects.filter(visit_date=now).order_by('visit_time')
    tomorrow_pets = Wizyty.objects.filter(visit_date=now + timedelta(days=1)).order_by('visit_time')
    return render(request, 'klienci/index.html', {
        "today_pets": today_pets,
        "tomorrow_pets": tomorrow_pets
    })

def pets(request):
    submitted = False
    if request.method == "POST":
        form = ZwierzeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/klienci?submitted=True')
    else:
        form = ZwierzeForm
        if 'submitted' in request.GET:
            submitted = True

    latest_pets_list = Zwierze.objects.order_by('-create_date')[:4]
    return render(request, "klienci/klienci.html", {
        "latest_pets_list": latest_pets_list,
        "form": form,
        "submitted": submitted
    })

def detail(request, zwierze_id):
    pet = Zwierze.objects.get(pk=zwierze_id)
    try:
        return render(request, 'klienci/pet.html', {
            "pet": pet
            })
    except:
        return HttpResponseNotFound("Nie ma takiego klienta!")

def calendar(request):
    visit_list = Wizyty.objects.all()
    return render(request, 'klienci/kalendarz.html', {
        'visit_list': visit_list,
    })

def shop(request):
    return render(request, 'klienci/sprzedaz.html', {})

def statistics(request):
    return render(request, 'klienci/statystyki.html', {})

def search(request):
    searched = request.POST['searched']
    pets = Zwierze.objects.filter(imie__contains=searched)
    return render(request, 'klienci/search.html', {
        'searched': searched,
        'pets': pets,
        })   
    
def edit_pet(request, zwierze_id):
    pet = Zwierze.objects.get(pk=zwierze_id)
    form = ZwierzeForm(request.POST or None, instance=pet)
    if form.is_valid():
        form.save()
        return redirect('index')
    
    try:
        return render(request, 'klienci/edit_pet.html', {
            'pet': pet,
            'form': form,})
    except:
        return HttpResponseNotFound("Nie ma takiego klienta!")

def add_visit(request):
    submitted = False
    if request.method == "POST":
        form = WizytyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_visit?submitted=True')
    else:
        form = WizytyForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "klienci/add_visit.html", {
        "form": form,
        "submitted": submitted
    })


def edit_visit(request, visit_id):
    visit = Wizyty.objects.get(pk=visit_id)
    form = WizytyForm(request.POST or None, instance=visit)
    if form.is_valid():
        form.save()
        return redirect('index')
    
    try:
        return render(request, 'klienci/edit_visit.html', {
            'visit': visit,
            'form': form,})
    except:
        return HttpResponseNotFound("Nie ma takiej wizyty!")