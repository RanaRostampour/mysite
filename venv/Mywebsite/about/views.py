from django.shortcuts import render
from django.db import models
from .form import subscribe
from django.shortcuts import redirect
from django.contrib import messages

def about_view(response,*awrgs):
    if response.method == "POST":
	    form = subscribe(response.POST)
	    if form.is_valid():
	        form.save()
	        return redirect("about.html")
            
    else:
        
	    messages.MessageFailure()

    return render(response, "about.html")