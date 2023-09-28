from django.shortcuts import render,redirect
from .forms import ImageUploadForm
from .models import ImageModel

def property_grid(request):
    return render(request, 'property_grid.html')

def property_single(request):
    return render(request, 'property_single.html')

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
    else:
        form = ImageUploadForm()
    
    return render(request, 'upload_image.html', {'form': form})

def display_images(request):
    images = ImageModel.objects.all()
    return render(request, 'display_image.html', {'images': images})