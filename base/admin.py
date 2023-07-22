from django.contrib import admin
from .models import Half_day_tour, Full_day_tour, Half_Day_Booking, Request, Full_Day_Booking, Holiday_Ideas_Booking, Opener, Tour_guider, Testimonial, Gallery, Video, Contact, AboutUs, Holiday_Leisure_Study





class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']

class BookingAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'country','tour_program','meeting_point','time_confirmation',]


admin.site.register(Half_day_tour)
admin.site.register(Full_day_tour)

admin.site.register(Holiday_Leisure_Study)
admin.site.register(Half_Day_Booking, BookingAdmin)
admin.site.register(Opener)
admin.site.register(Tour_guider)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Video)
admin.site.register(Contact)
admin.site.register(AboutUs)
admin.site.register(Testimonial)
admin.site.register(Full_Day_Booking, BookingAdmin)
admin.site.register(Holiday_Ideas_Booking, BookingAdmin)
admin.site.register(Request)
