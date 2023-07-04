from django.db import models

class TourSite(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    people_amount = models.CharField(max_length=200)
    discriptions = models.CharField(max_length=200)
    # image

    def __str__(self):
        return self.name

class Booking(models.Model):
    fullname = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    home = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    passport_no = models.CharField(max_length=200,)
    marital_status = models.CharField(max_length=200)
    sex = models.CharField(max_length=200)
    phone_no = models.IntegerField()
    email = models.EmailField(max_length=200)
    type_of_client = models.CharField(max_length=200)
    number_of_client = models.CharField(max_length=200)
    status_of_client = models.CharField(max_length=200)
    # tour_program = models.ForeignKey(TourSite, on_delete=models.SET_NULL , null=True)
    type_of_tour_trip = models.CharField(max_length=200)
    holiday_idea = models.CharField(max_length=200)
    client_Age_group  = models.CharField(max_length=200,)
    include_in_tour = models.CharField(max_length=200)
    exclude_in_tour = models.CharField(max_length=200)
    meeting_point  = models.CharField(max_length=200)
    language  = models.EmailField(max_length=200)
    # time_confirmation  = models.DateTimeField(max_length=200)
    # created
    # updated


    def __str__(self):
        return self.fullname


# Create your models here.
# class Opener(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField(max_length=200)
#     # hero_image = models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)

#     def __str__(self):
#         return self.title

# class Tour_guides(models.Model):
#     # guider_image = models.ImageField
#     full_name = models.CharField(max_length=200)
#     language = models.CharField(max_length=200)
#     interest = models.CharField(max_length=200)

#     def __str__(self):
#         return self.full_name

# class Testimonial(models.Model):
#     # client_image = models.ImageField
#     full_name = models.CharField(max_length=200)
#     location = models.CharField(max_length=200)
#     description = models.TextField(max_length=300)

#     def __str__(self):
#         return self.full_name


# # class Zanzibar(models.Model):
# #     images
  
# class Zanzibar_tour(models.Model):
#     location = models.CharField(max_length=200)
#     time = models.CharField(max_length=200)
#     people_amount = models.CharField(max_length=200)
#     name = models.CharField(max_length=200)
#     discriptions = models.CharField(max_length=200)
#     # image 

#     def __str__(self):
#         return self.name

# class Island_tour(models.Model):
#     location = models.CharField(max_length=200)
#     time = models.CharField(max_length=200)
#     people_amount = models.CharField(max_length=200)
#     name = models.CharField(max_length=200)
#     discriptions = models.CharField(max_length=200)
#     # image 

#     def __str__(self):
#         return self.name

# class BlueSafari_tour(models.Model):
#     location = models.CharField(max_length=200)
#     time = models.CharField(max_length=200)
#     people_amount = models.CharField(max_length=200)
#     name = models.CharField(max_length=200)
#     discriptions = models.CharField(max_length=200)
#     # image 

#     def __str__(self):
#         return self.name

# class Zanzibar_shallow(models.Model):
#     location = models.CharField(max_length=200)
#     time = models.CharField(max_length=200)
#     people_amount = models.CharField(max_length=200)
#     name = models.CharField(max_length=200)
#     discriptions = models.CharField(max_length=200)
#     # image 

#     def __str__(self):
#         return self.name

# class HalfDay_tour(models.Model):
#     location = models.CharField(max_length=200)
#     time = models.CharField(max_length=200)
#     people_amount = models.CharField(max_length=200)
#     name = models.CharField(max_length=200)
#     discriptions = models.CharField(max_length=200)
#     # image 

#     def __str__(self):
#         return self.name

# class Contact(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.CharField(max_length=200)
#     subject = models.CharField(max_length=200)
#     message = models.TextField(max_length=200)

#     def __str__(self):
#         return self.name
    
# class Region(models.Model):
#     name = models.CharField(max_length=200)
#     discription = models.TextField(max_length=300)
#     image = models.ImageField(upload_to='media', blank=True, null=True)


# class TourBook(models.Model):
#     name = models.CharField(max_length=200)
#     country = models.CharField(max_length=200)
#     nationality = models.CharField(max_length=200)
#     home = models.CharField(max_length=200)
#     city = models.CharField(max_length=200)
#     passport_no = models.CharField(max_length=200,)
#     marital_status = models.CharField(max_length=200)
#     sex = models.CharField(max_length=200)
#     phone_no = models.IntegerField()
#     email = models.EmailField(max_length=200)

    # def __str__(self):
    #     return self.name
    


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