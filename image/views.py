from django.shortcuts import render
from .models import Image

# Create your views here.
def index(request):
    # receive image
    if request.method == 'POST':
        files = request.FILES.getlist('images') # images in index
        file_list = []
        for file in files:
            new_image = Image(
                # file = request.FILES['img']
                file = file # from model
            )
            new_image.save()
            file_list.append(new_image.file.url)
        # return render(request,'index.html',{'img_url': str(new_image.file.url)}) # img_url in index
        return render(request,'index.html',{'img_urls': file_list}) # img_url in index
    else:
        return render(request,'index.html')