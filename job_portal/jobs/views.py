from django.shortcuts import render
from .models import Jobs

# Create your views here.
def home(request):

    job_list = Jobs.objects.all()
    return render(request, "home.html", {"jobs": job_list})
