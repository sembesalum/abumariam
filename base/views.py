from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Booking, TourSite, Contact

# Create your views here.

def index(request):
    return render(request, 'index.html')

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

def book_form(request):
    if request.method == 'POST':        
        fullname = request.POST['fullname']
        country = request.POST['country']
        nationality = request.POST['nationality']
        home = request.POST['home']
        city = request.POST['city']
        passport_no = request.POST['passport_no']
        marital_status = request.POST['marital_status']
        phone_no = request.POST['phone_no']
        email = request.POST['email']
        type_of_client = request.POST['type_of_client']
        number_of_client = request.POST['number_of_client']
        status_of_client = request.POST['status_of_client']        
        # tour_program = request.POST['tour_program']
        type_of_tour_trip = request.POST['type_of_tour_trip']
        holiday_idea = request.POST['holiday_idea']
        client_Age_group  = request.POST['client_Age_group']
        include_in_tour = request.POST['include_in_tour']
        exclude_in_tour = request.POST['exclude_in_tour']
        meeting_point  = request.POST['meeting_point']
        language  = request.POST['language']
        # time_confirmation  = request.POST['time_confirmation']

        booking1 = Booking.objects.create(fullname=fullname, country=country, nationality=nationality, home=home,city=city,
        passport_no=passport_no, marital_status=marital_status, phone_no=phone_no, email=email, type_of_client=type_of_client,
        number_of_client=number_of_client, status_of_client=status_of_client, type_of_tour_trip=type_of_tour_trip,
        holiday_idea=holiday_idea, client_Age_group=client_Age_group, include_in_tour=include_in_tour, meeting_point=meeting_point,
        language=language, exclude_in_tour=exclude_in_tour)
        booking1.save()
        return redirect('index')
    return render(request, 'booking_form01.html')


def book_form2(request):


    context = {
        
    }
    return render(request, 'booking_form02.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        send_info = Contact.objects.create(name=name, email=email, subject=subject, message=message)
        send_info.save()
        
        return redirect('contact')        
    return render(request, 'contact.html')

def full_day(request):
    return render(request, 'full_day.html')

def half_day(request):
    return render(request, 'half_day.html')

def holiday_ideas(request):
    return render(request, 'holiday_ideas.html')

def images(request):
    return render(request, 'images.html')

def leisure_activities(request):
    return render(request, 'leisure_activities.html')

def videos(request):
    return render(request, 'videos.html')

def zanzibar(request):
    return render(request, 'zanzibar.html')

def not_found(request):
    return render(request, '404.html')

def parliament(request):
    return render(request, 'parliament.html')
    
def discovered_paradise(request):
    return render(request, 'discovered_paradise.html')

