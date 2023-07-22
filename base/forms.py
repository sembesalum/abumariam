from django.forms import ModelForm
from .models import Half_Day_Booking, Full_Day_Booking, Holiday_Ideas_Booking
from django.forms import ModelForm, TextInput, NumberInput, EmailInput, Select, DateInput




class BookingForm(ModelForm):
    class Meta:
        model = Half_Day_Booking
        fields = '__all__'
        # fields = ['fullname', 'country', 'nationality','home','city','sex','maritalstatus',]
        # 'maritalstatus','tour_program','no_of_client','status_of_client','type_of_tour_trip',
        # 'holiday_idea','client_age_group ', 'include_in_tour','exclude_in_tour','meeting_point','language','contact',
        # 'passport_no','time_confirmation']
        widgets = {
            'fullname': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Full name'
                }),

            'country': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Your country'
                }),

            'nationality': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Nationality'
                }),

            'home': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Home'
                }),

            'city': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'City'
                }),

            'sex': Select(attrs={
                'class': "form-control",
                'placeholder': 'Sex'
                }),

            'maritalstatus': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Marital Status'
                }),


# -------------------Tour Program------------

            'tour_program': Select(attrs={
                'class': "form-control",
                'placeholder': 'Tour Program'
                }),

            'no_of_client': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Number of Client'
                }),

            'status_of_client': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Status of client: e.g. teachers, students, VIP, businessmen, employed, unemployed, special group, worker, family’s'
                }),

            'type_of_client': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Type of client: e.g single, double, families or group, organization, students, businessmen, teachers, lovers'
                }),

            'holiday_idea': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Holiday Idea: e.g. spice tour, game viewing, animals watching, Safari to parliament, birds watching'
                }),

            'client_age_group': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Client Age Group: e.g. 0-18, 18-20, 20-30, 30-above, both range and above'
                }),


# -----------Complete Booking---------------

            'include_in_tour': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'What to include in your tour'
                }),

            'exclude_in_tour': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'What to exclude in your tour'
                }),

            'meeting_point': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Meeting point (location that guide will get your for tour e.g. name of hotel) '
                }),

            'language': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Language to use'
                }),

            'contact': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Contact'
                }),

            'passport_no': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Identity number/passport number '
                }),

            'time_confirmation': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Time confirmation'
                }),
            
        }


class BookingForm2(ModelForm):
    class Meta:
        model = Full_Day_Booking
        fields = '__all__'
        # fields = ['fullname', 'country', 'nationality','home','city','sex','maritalstatus',]
        # 'maritalstatus','tour_program','no_of_client','status_of_client','type_of_tour_trip',
        # 'holiday_idea','client_age_group ', 'include_in_tour','exclude_in_tour','meeting_point','language','contact',
        # 'passport_no','time_confirmation']
        widgets = {
            'fullname': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Full name'
                }),

            'country': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Your country'
                }),

            'nationality': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Nationality'
                }),

            'home': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Home'
                }),

            'city': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'City'
                }),

            'sex': Select(attrs={
                'class': "form-control",
                'placeholder': 'Sex'
                }),

            'maritalstatus': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Marital Status'
                }),


# -------------------Tour Program------------

            'tour_program': Select(attrs={
                'class': "form-control",
                'placeholder': 'Tour Program'
                }),

            'no_of_client': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Number of Client'
                }),

            'status_of_client': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Status of client: e.g. teachers, students, VIP, businessmen, employed, unemployed, special group, worker, family’s'
                }),

            'type_of_client': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Type of client: e.g single, double, families or group, organization, students, businessmen, teachers, lovers'
                }),

            'holiday_idea': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Holiday Idea: e.g. spice tour, game viewing, animals watching, Safari to parliament, birds watching'
                }),

            'client_age_group': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Client Age Group: e.g. 0-18, 18-20, 20-30, 30-above, both range and above'
                }),


# -----------Complete Booking---------------

            'include_in_tour': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'What to include in your tour'
                }),

            'exclude_in_tour': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'What to exclude in your tour'
                }),

            'meeting_point': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Meeting point (location that guide will get your for tour e.g. name of hotel) '
                }),

            'language': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Language to use'
                }),

            'contact': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Contact'
                }),

            'passport_no': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Identity number/passport number '
                }),

            'time_confirmation': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Time confirmation'
                }),
            
        }



class BookingForm3(ModelForm):
    class Meta:
        model = Holiday_Ideas_Booking
        fields = '__all__'
        # fields = ['fullname', 'country', 'nationality','home','city','sex','maritalstatus',]
        # 'maritalstatus','tour_program','no_of_client','status_of_client','type_of_tour_trip',
        # 'holiday_idea','client_age_group ', 'include_in_tour','exclude_in_tour','meeting_point','language','contact',
        # 'passport_no','time_confirmation']
        widgets = {
            'fullname': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Full name'
                }),

            'country': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Your country'
                }),

            'nationality': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Nationality'
                }),

            'home': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Home'
                }),

            'city': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'City'
                }),

            'sex': Select(attrs={
                'class': "form-control",
                'placeholder': 'Sex'
                }),

            'maritalstatus': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Marital Status'
                }),


# -------------------Tour Program------------

            'tour_program': Select(attrs={
                'class': "form-control",
                'placeholder': 'Tour Program'
                }),

            'no_of_client': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Number of Client'
                }),

            'status_of_client': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Status of client: e.g. teachers, students, VIP, businessmen, employed, unemployed, special group, worker, family’s'
                }),

            'type_of_client': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Type of client: e.g single, double, families or group, organization, students, businessmen, teachers, lovers'
                }),

            'holiday_idea': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Holiday Idea: e.g. spice tour, game viewing, animals watching, Safari to parliament, birds watching'
                }),

            'client_age_group': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Client Age Group: e.g. 0-18, 18-20, 20-30, 30-above, both range and above'
                }),


# -----------Complete Booking---------------

            'include_in_tour': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'What to include in your tour'
                }),

            'exclude_in_tour': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'What to exclude in your tour'
                }),

            'meeting_point': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Meeting point (location that guide will get your for tour e.g. name of hotel) '
                }),

            'language': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Language to use'
                }),

            'contact': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Contact'
                }),

            'passport_no': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Identity number/passport number '
                }),

            'time_confirmation': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Time confirmation'
                }),
            
        }