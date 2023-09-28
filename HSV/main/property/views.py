from django.shortcuts import render


def property_grid(request):
    return render(request, 'property_grid.html')

def property_single(request):
    return render(request, 'property_single.html')