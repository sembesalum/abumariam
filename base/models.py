from django.db import models
from django.contrib.auth.models import User


class Half_day_tour(models.Model):
    name = models.CharField(max_length=200)
    # tour_type = models.CharField(max_length=200)
    # people_amount = models.CharField(max_length=200)
    # discriptions = models.CharField(max_length=200)
    # image = models.ImageField(upload_to='tour_site/', blank=True, null=True)
    # created = models.DateTimeField(auto_now_add=True)
    # image

    def __str__(self):
        return self.name


class Full_day_tour(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name



class Holiday_Leisure_Study(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name



class Half_Day_Booking(models.Model):
    # fullname = models.ForeignKey(User, on_delete=models.CASCADE , null=True)
    # half day
    sexs = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    fullname = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    home = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    sex = models.CharField(max_length=10, choices=sexs)
    maritalstatus = models.CharField(max_length=200)



    # -------------------------Tour Program -------------

    tour_program = models.ForeignKey(Half_day_tour, on_delete=models.CASCADE , null=True)
    no_of_client = models.IntegerField()
    status_of_client = models.CharField(max_length=200)
    type_of_client = models.CharField(max_length=200)
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

    # ---------------------- End of Half Day Booking---------



class Full_Day_Booking(models.Model):
    # fullname = models.ForeignKey(User, on_delete=models.CASCADE , null=True)
    # form2
    sexs = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    fullname = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    home = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    sex = models.CharField(max_length=10, choices=sexs)
    maritalstatus = models.CharField(max_length=200)



    # -------------------------Tour Program -------------

    tour_program = models.ForeignKey(Full_day_tour, on_delete=models.CASCADE , null=True)
    no_of_client = models.IntegerField()
    status_of_client = models.CharField(max_length=200)
    type_of_client = models.CharField(max_length=200)
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

    # ---------------------- End of Full Day Booking---------


class Holiday_Ideas_Booking(models.Model):
    # leisure
    # fullname = models.ForeignKey(User, on_delete=models.CASCADE , null=True)
    sexs = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    fullname = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    home = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    sex = models.CharField(max_length=10, choices=sexs)
    maritalstatus = models.CharField(max_length=200)



    # -------------------------Tour Program -------------

    tour_program = models.ForeignKey(Holiday_Leisure_Study, on_delete=models.CASCADE , null=True)
    no_of_client = models.IntegerField()
    status_of_client = models.CharField(max_length=200)
    type_of_client = models.CharField(max_length=200)
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

    # ---------------------- End of Full Day Booking---------




class Opener(models.Model):
    title = models.CharField(max_length=200)
    discription = models.CharField(max_length=200)
    description2 = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Tour_guider(models.Model):
    full_name = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    interest = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    guider_image = models.ImageField(upload_to='guider/', blank=True, null=True)

    def __str__(self):
        return self.full_name

class Testimonial(models.Model):
    full_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    client_image = models.ImageField(upload_to='testmonial/', blank=True, null=True)

    def __str__(self):
        return self.full_name


class Gallery(models.Model):    
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='gallery/', blank=True, null=True)

    def __str__(self):
        return self.title

class Video(models.Model):    
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    video = models.FileField(upload_to="videos/", null=True, verbose_name="")

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()

    def __str__(self):
        return self.name

class Request(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()

    def __str__(self):
        return self.subject
    
class AboutUs(models.Model):
    email = models.EmailField()
    phone_no = models.CharField(max_length=200)
    whatsapp_no = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    acc_name = models.CharField(max_length=200)
    acc_no = models.CharField(max_length=200)
    privacy_policy = models.TextField()
    terms_condition = models.TextField()
    
    def __str__(self):
        return self.email