from django.db import models
from django.contrib.auth.models import User


class TourSite(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    people_amount = models.CharField(max_length=200)
    discriptions = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # created = models.DateTimeField(auto_now_add=True)
    # image

    def __str__(self):
        return self.name

class Booking(models.Model):
    # fullname = models.ForeignKey(User, on_delete=models.CASCADE , null=True)
    fullname = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    home = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    sex = models.CharField(max_length=200)
    maritalstatus = models.CharField(max_length=200)



    # -------------------------Tour Program -------------

    tour_program = models.ForeignKey(TourSite, on_delete=models.CASCADE , null=True)
    no_of_client = models.IntegerField()
    status_of_client = models.CharField(max_length=200)
    type_of_client = models.CharField(max_length=200)
    type_of_tour_trip = models.CharField(max_length=200)
    holiday_idea = models.CharField(max_length=200)
    client_age_group = models.CharField(max_length=200)


    # ---------------------- Complete Booking---------

    include_in_tour = models.CharField(max_length=200)
    exclude_in_tour = models.CharField(max_length=200)
    meeting_point  = models.CharField(max_length=200)
    language  = models.CharField(max_length=200)
    contact = models.IntegerField()
    passport_no = models.CharField(max_length=200)
    time_confirmation  = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.fullname




class Opener(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.title

class Tour_guides(models.Model):
    full_name = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    interest = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    # guider_image = models.ImageField(upload_to='guider/', blank=True, null=True)

    def __str__(self):
        return self.full_name

class Testimonial(models.Model):
    full_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    # client_image = models.ImageField(upload_to='testmonial/', blank=True, null=True)

    def __str__(self):
        return self.full_name


class Gallery(models.Model):
    tour_name = models.ForeignKey(TourSite, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    # image = models.ImageField(upload_to='gallery/', blank=True, null=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()

    def __str__(self):
        return self.name
    
class AboutUs(models.Model):
    email = models.EmailField()
    phone_no = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    acc_name = models.CharField(max_length=200)
    acc_no = models.CharField(max_length=200)
    privacy_policy = models.TextField()
    terms_condition = models.TextField()
    
    def __str__(self):
        return self.acc_name