from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def compare_stocks(request):
    if request.method == 'POST':
        symbols = request.POST.get('symbols').split(',')
        # Add your logic for comparing stocks here
        result = {"comparison": "result"}  # Replace with actual comparison result
        return JsonResponse(result)
    return render(request, 'compare_stocks.html')