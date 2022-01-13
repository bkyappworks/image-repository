from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        # receive user input data
        form  = UserCreationForm(request.POST) # access all the data POST and create UserCreationForm() 
        if form.is_valid():
            user = form.save()
            # log user in
            login(request,user)
            return redirect('image:index') # image.urls 'app_name:name'
    else:
        form = UserCreationForm() #blank form
    return render(request,'accounts/signup.html',{"form":form}) # form in signup.html

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            #log user in
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next')) # name="next" in login.html
            else:
                return redirect('image:index') #app_name:url_name
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{"form":form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('image:index')
