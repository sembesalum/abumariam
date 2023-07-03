from django.contrib import admin
from .models import Opener, Tour_guides, Testimonial, Company, Zanzibar_tour, Island_tour, BlueSafari_tour, Zanzibar_shallow, HalfDay_tour, Contact

# Register your models here.

admin.site.register(Opener)
admin.site.register(Tour_guides)
admin.site.register(Testimonial)
admin.site.register(Zanzibar_tour)
admin.site.register(Island_tour)
admin.site.register(BlueSafari_tour)
admin.site.register(Zanzibar_shallow)
admin.site.register(HalfDay_tour)
admin.site.register(Contact)

