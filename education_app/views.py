from django.shortcuts import render

# Create your views here.
def home_page(request):
    context ={}
    return render (request,"index.html", context)

def about_page(request):
    context ={}
    return render (request,"about.html", context)

def contact_page(request):
    context ={}
    return render (request,"contact.html", context)

def course_details_page(request):
    context ={}
    return render (request,"course-details.html", context)

def courses_page(request):
    context ={}
    return render (request,"courses.html", context)

def events_page(request):
    context ={}
    return render (request,"events.html", context)

def trainers_page(request):
    context ={}
    return render (request,"trainers.html", context)

def starter_page(request):
    context ={}
    return render (request,"starter.html", context)

def pricing_page(request):
    context ={}
    return render (request,"pricing.html", context)
