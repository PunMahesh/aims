from django.shortcuts import render, redirect
from .models import Crop
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required (login_url="login")
def add_crop(request):
    if request.method == "POST":
        user = request.user
        crop_name = request.POST.get("crop_name")
        pesticide_used = request.POST.get("pesticide_used")
        market_value = request.POST.get("market_value")
        disease = request.POST.get("disease")
        season = request.POST.get("season")
        crop_img = request.FILES.get("crop_img")
        description = request.POST.get("description")

        details = Crop(user=user,crop_name=crop_name, pesticide_used=pesticide_used, market_value=market_value,
                         disease=disease, season=season, crop_img=crop_img, description=description)
        details.save()
        return redirect("crop_added")
    return render(request, 'add_crop.html')

@login_required (login_url="login")
def get_crops(request):
    # Fetch Crops information here and pass it in the context. The format should be as follows:
    crops = Crop.objects.all()
    context = {'crops': crops}
    return render(request, 'crops.html', context)

@login_required (login_url="login")
def get_crop(request, id):
    crop = Crop.objects.get(id=id)
    fss = FileSystemStorage()
    context = {'crop': crop, 'crop_img_url': request.build_absolute_uri(fss.url(crop.crop_img))}
    return render(request, 'crops_show_more.html', context)

@login_required (login_url="login")
def delete_crop(request, id):
    crop = Crop.objects.get(id=id)
    crop.delete()
    return render(request, "crops_show_more.html")

@login_required (login_url="login")
def crop_added(request):
    return render(request, "crops_added.html")
