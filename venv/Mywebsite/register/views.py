
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
def register(response,*awrgs):
    if response.method == "POST":
	    form = RegisterForm(response.POST)
	    if form.is_valid():
	        form.save()



	        return redirect("/")
    else:
        
	    form = RegisterForm()
	
    return render(response, "register.html", {"form":form})
