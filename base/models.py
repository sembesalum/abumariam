from django.db import models

# Create your models here.
class Opener(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    # hero_image = models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.title

class Tour_guides(models.Model):
    # guider_image = models.ImageField
    full_name = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    interest = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name

class Testimonial(models.Model):
    # client_image = models.ImageField
    full_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.full_name

class Company(models.Model):
    company_name = models.CharField(max_length=200)
    # email
    # twitter
    # facebook
    # youtube
    # linkedn
    privacy_policy = models.TextField(max_length=800)
    terms_condition = models.TextField(max_length=200)

    def __str__(self):
        return self.company_name

# class Zanzibar(models.Model):
#     images
  
class Zanzibar_tour(models.Model):
    location = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    people_amount = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    discriptions = models.CharField(max_length=200)
    # image 

    def __str__(self):
        return self.name

class Island_tour(models.Model):
    location = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    people_amount = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    discriptions = models.CharField(max_length=200)
    # image 

    def __str__(self):
        return self.name

class BlueSafari_tour(models.Model):
    location = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    people_amount = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    discriptions = models.CharField(max_length=200)
    # image 

    def __str__(self):
        return self.name

class Zanzibar_shallow(models.Model):
    location = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    people_amount = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    discriptions = models.CharField(max_length=200)
    # image 

    def __str__(self):
        return self.name

class HalfDay_tour(models.Model):
    location = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    people_amount = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    discriptions = models.CharField(max_length=200)
    # image 

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=200)

    def __str__(self):
        return self.name
    
class Region(models.Model):
    name = models.CharField(max_length=200)
    discription = models.TextField(max_length=300)
    image = models.ImageField(upload_to='media', blank=True, null=True)


################ RURAL AND URBAN TOUR ################

# class Dodoma_tour(models.Model):
#     dodoma_image01
#     dodoma_image02
#     dodoma_image03
#     dodoma_image04

# class Grape_tour(models.Model):
#     dodoma_image01
#     dodoma_image02
#     dodoma_image03
#     dodoma_image04

# class Dar_tour(models.Model):
#     dodoma_image01
#     dodoma_image02
#     dodoma_image03
#     dodoma_image04

# class Arisha_tour(models.Model):
#     dodoma_image01
#     dodoma_image02
#     dodoma_image03
#     dodoma_image04

# class Food_tour(models.Model):
#     dodoma_image01
#     dodoma_image02
#     dodoma_image03
#     dodoma_image04

# class Wildlife_tour(models.Model):
#     dodoma_image01
#     dodoma_image02
#     dodoma_image03
#     dodoma_image04

# class Game_tour(models.Model):
#     dodoma_image01
#     dodoma_image02
#     dodoma_image03
#     dodoma_image04

# class Balloon_tour(models.Model):
#     dodoma_image01
#     dodoma_image02
#     dodoma_image03
#     dodoma_image04

# class Birds_tour(models.Model):
#     dodoma_image01
#     dodoma_image02
#     dodoma_image03
#     dodoma_image04

# class Cultural_tour(models.Model):
#     dodoma_image01
#     dodoma_image02
#     dodoma_image03
#     dodoma_image04

# class Historical_tour(models.Model):
#     dodoma_image01
#     dodoma_image02
#     dodoma_image03
#     dodoma_image04

# class Charity_tour(models.Model):
#     dodoma_image01
#     dodoma_image02
#     dodoma_image03
#     dodoma_image04

# class Video_gallery(models.Model):
#     video


################# BOOKING AND DONATION FORMS ##################