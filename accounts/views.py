from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        # receive user input data
        form  = UserCreationForm(request.POST) # access all the data POST and create UserCreationForm() 
        if form.is_valid():
            form.save()
            # log user in
            return redirect('image:index') # image.urls 'app_name:name'
    else:
        form = UserCreationForm() #blank form
    return render(request,'accounts/signup.html',{"form":form}) # form in signup.html
