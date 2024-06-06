from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Stock
import datetime

# Create your views here.

def index(request):
    return render(request, 'index.html')

def compare_stocks(request):
    if request.method == 'POST':
        symbols = request.POST.get('symbols').split(',')
        stocks = Stock.objects.filter(symbol__in==symbols)
        # Add your logic for comparing stocks here
        result = {"comparison": "result"}  # Replace with actual comparison result
        return JsonResponse(result)
    return render(request, 'compare_stocks.html')

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})