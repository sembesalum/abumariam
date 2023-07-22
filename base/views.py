from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import BookingForm, BookingForm2, BookingForm3
from django.contrib.auth.decorators import login_required
from .models import Contact, AboutUs, Request, Testimonial, Tour_guider, Half_day_tour, Full_day_tour, Holiday_Leisure_Study, Opener, Gallery, Video

# Create your views here.

def index(request):
    header = Opener.objects.all()
    about_us = AboutUs.objects.all()
    testimonial = Testimonial.objects.all()
    tour_guides = Tour_guider.objects.all()
    gallery = Gallery.objects.all()

    context = {
        'header':header,
        'about_us':about_us,
        'testimonial':testimonial,
        'tour_guides':tour_guides,
        'gallery':gallery,
    }

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        send_info = Contact.objects.create(name=name, email=email, subject=subject, message=message)
        send_info.save()
        
        return redirect('index')        
    return render(request, 'index.html', context)


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password Not The Same')
            return redirect('signup')
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Credentials invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

@login_required(login_url='login')
def book_form(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        
        if form.is_valid():            
            form.save()
            return redirect('confirmation')
    context = {
        'form':form
    }
    return render(request, 'booking_form01.html', context)


@login_required(login_url='login')
def book_form2(request):
    form = BookingForm2()
    if request.method == 'POST':
        form = BookingForm2(request.POST)
        
        if form.is_valid():            
            form.save()
            return redirect('confirmation')
    context = {
        'form':form
    }
    return render(request, 'booking_form02.html', context)

@login_required(login_url='login')
def book_form3(request):
    form = BookingForm3()
    if request.method == 'POST':
        form = BookingForm3(request.POST)
        
        if form.is_valid():            
            form.save()
            return redirect('confirmation')
    context = {
        'form':form
    }
    return render(request, 'booking_form03.html', context)


def contact(request):

    about_us = AboutUs.objects.all()
    header = Opener.objects.all()

    context = {
        'about_us': about_us,
        'header': header
    }

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        send_info = Contact.objects.create(name=name, email=email, subject=subject, message=message)
        send_info.save()
        
        return redirect('contact')        
    return render(request, 'contact.html', context)

def full_day(request):

    about_us = AboutUs.objects.all()
    header = Opener.objects.all()
    tour_guides = Tour_guider.objects.all()
    testimonial = Testimonial.objects.all()

    context = {
        'about_us': about_us,
        'header': header,
        'tour_guides': tour_guides,
        'testimonial': testimonial
    }

    return render(request, 'full_day.html', context)

def half_day(request):

    about_us = AboutUs.objects.all()
    header = Opener.objects.all()
    tour_guides = Tour_guider.objects.all()
    testimonial = Testimonial.objects.all()

    context = {
        'about_us': about_us,
        'header': header,
        'tour_guides': tour_guides,
        'testimonial': testimonial
    }

    return render(request, 'half_day.html', context)

def holiday_ideas(request):

    about_us = AboutUs.objects.all()
    header = Opener.objects.all()

    context = {
        'about_us': about_us,
        'header': header
    }

    return render(request, 'holiday_ideas.html', context)


def images(request):
    gallery = Gallery.objects.all()
    about_us = AboutUs.objects.all()
    header = Opener.objects.all()

    context = {
        'gallery': gallery,
        'about_us': about_us,
        'header': header
    }

    return render(request, 'images.html', context)


def leisure_activities(request):
    about_us = AboutUs.objects.all()
    header = Opener.objects.all()

    context = {
        'about_us': about_us,
        'header': header
    }
    return render(request, 'leisure_activities.html', context)


def videos(request):
    videos = Video.objects.all()
    about_us = AboutUs.objects.all()
    header = Opener.objects.all()

    context = {
        'videos': videos,
        'about_us': about_us,
        'header': header
    }

    return render(request, 'videos.html', context)


def zanzibar(request):
    about_us = AboutUs.objects.all()
    header = Opener.objects.all()

    context = {
        'about_us': about_us,
        'header': header
    }

    return render(request, 'zanzibar.html', context)

def not_found(request):
    about_us = AboutUs.objects.all()
    header = Opener.objects.all()

    context = {
        'about_us': about_us,
        'header': header
    }
    return render(request, '404.html', context)


def parliament(request):
    about_us = AboutUs.objects.all()
    header = Opener.objects.all()

    context = {
        'about_us': about_us,
        'header': header
    }
    return render(request, 'parliament.html', context)

    
def discovered_paradise(request):
    about_us = AboutUs.objects.all()
    header = Opener.objects.all()

    context = {
        'about_us': about_us,
        'header': header
    }
    return render(request, 'discovered_paradise.html', context)


def confirmation(request):    
    about_us = AboutUs.objects.all()
    context = {
        'about_us': about_us
    }
    return render(request, 'confirmation.html', context)


def request(request):    
    about_us = AboutUs.objects.all()
    header = Opener.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        send_info = Request.objects.create(name=name, email=email, subject=subject, message=message)
        send_info.save()

        return redirect('confirmation') 

    context = {
        'about_us': about_us,
        'header': header
        }
        

    return render(request, 'request.html', context)