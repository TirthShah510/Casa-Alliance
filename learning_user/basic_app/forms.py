from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from basic_app.models import Profile, Hall, NoticePost, Prediction, ComplaintPost, Property, Visitor, \
    Blog, CommentAdd, Vehicle, Staff, HouseholdServices
from bootstrap_datepicker_plus import DatePickerInput
from django.contrib.admin import widgets
from django.forms.fields import DateField
from django.contrib.admin.widgets import AdminDateWidget
from basic_app.choices import *
from basic_app.admin import QuestionAdmin


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class ProfileForm(forms.ModelForm):

    contact_no = forms.RegexField(regex=r'^\d{10}$')

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'total_members', 'occupation', 'contact_no',
                  'society_name', 'house_name', 'wing_name', 'flat_no', 'society_address', 'profile_pic')


class PropertyForm(forms.ModelForm):
    property_for = forms.ChoiceField(choices=PROPERTY_FOR)
    property_type = forms.ChoiceField(choices=PROPERTY_TYPE)
    property_BHK = forms.ChoiceField(choices=PROPERTY_BHK)
    property_balconies = forms.ChoiceField(choices=PROPERTY_BALCONIES)
    property_flor_number = forms.ChoiceField(choices=PROPERTY_FLOR_NO)
    mode = forms.ChoiceField(choices=MODE)

    class Meta:
        model = Property
        fields = ('wing_name', 'flat_no', 'property_for', 'property_type', 'property_BHK', 'property_balconies',
                  'property_flor_number', 'property_covered_area', 'property_carpet_area', 'property_price',
                  'property_owner', 'owner_contact', 'mode', 'property_picture')


class HallForm(forms.ModelForm):
    event_type = forms.ChoiceField(choices=hall_event)

    class Meta:
        model = Hall
        fields = ('date', 'event_type', 'event_description')


class ComplaintForm(forms.ModelForm):

    class Meta:
        model = ComplaintPost
        fields = ('category', 'subcategory', 'complaint_description')


class NoticeForm(forms.ModelForm):

    class Meta:
        model = NoticePost
        fields = ('notice_subject', 'notice_description', 'notice_file')


class PredictForm(forms.ModelForm):
    bhk = forms.ChoiceField(choices=PROPERTY_BHK)

    class Meta:
        model = Prediction
        fields = ('bhk','sq_ft','built_year')


class VisitorForm(forms.ModelForm):
    visitor_prefix = forms.ChoiceField(choices=NAME_PREFIX)

    class Meta:
        model = Visitor
        fields = ('visitor_prefix', 'visitor_name', 'host_name')


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title', 'description')


class CommentAddForm(forms.ModelForm):

    class Meta:
        model = CommentAdd
        fields = ('text',)


class VehicleForm(forms.ModelForm):
    type = forms.ChoiceField(choices=VEHICLE_TYPE)

    class Meta:
        model = Vehicle
        fields = ('type', 'number')


class StaffForm(forms.ModelForm):
    servant = forms.ChoiceField(choices=SERVANT_TYPE)
    service = forms.ChoiceField(choices=SERVICE_TYPE)

    class Meta:
        model = Staff
        fields = ('servant', 'service', 'full_name')


class HouseholdForm(forms.ModelForm):

    class Meta:
        model = HouseholdServices
        fields = ('service_type', 'service_person', 'address' , 'contact')


class UserChange(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email')
