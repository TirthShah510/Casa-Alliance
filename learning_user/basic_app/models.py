from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User
from bootstrap_datepicker_plus import DatePickerInput
from basic_app.choices import *
import datetime
from django.utils import timezone
from django.shortcuts import reverse


name_regex = RegexValidator(r'^[a-zA-Z\s]*$', 'Only alphabets are allowed.')
mobile_regex = RegexValidator(r'^\d{10}$', 'Enter 10 digit mobile number.')

# USER PROFILE
####################################################################################################################


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.PROTECT)

    username_again = models.CharField(max_length=64)
    first_name = models.CharField(validators=[name_regex], max_length=64)
    last_name = models.CharField(validators=[name_regex], max_length=64)
    occupation = models.CharField(validators=[name_regex], max_length=64)
    contact_no = models.PositiveIntegerField()
    total_members = models.PositiveIntegerField()
    house_name = models.CharField(validators=[name_regex], max_length=64, blank=True)
    wing_name = models.CharField(validators=[name_regex], max_length=64)
    flat_no = models.IntegerField()
    society_name = models.CharField(validators=[name_regex], max_length=64)
    society_address = models.TextField(max_length=500)
    profile_pic = models.FileField(blank=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


# VEHICLE
########################################################################################################################


class Vehicle(models.Model):

    owner = models.CharField(max_length=64)
    type = models.CharField(choices=VEHICLE_TYPE, max_length=10)
    number = models.CharField(max_length=10)

    def __str__(self):
        return self.owner

# STAFF
########################################################################################################################


class Staff(models.Model):

    owner = models.CharField(max_length=64)
    servant = models.CharField(choices=SERVANT_TYPE, max_length=10)
    service = models.CharField(choices=SERVICE_TYPE, max_length=30)
    full_name = models.CharField(validators=[name_regex], max_length=20)

    def __str__(self):
        return self.owner

# PROPERTY TABLE
########################################################################################################################


class Property(models.Model):

    registered_by = models.CharField(max_length=64)
    wing_name = models.CharField(validators=[name_regex], max_length=20)
    flat_no = models.PositiveIntegerField()
    property_for = models.CharField(choices=PROPERTY_FOR, default=1, max_length=64)
    property_type = models.CharField(choices=PROPERTY_TYPE, max_length=64)
    property_BHK = models.PositiveIntegerField(choices=PROPERTY_BHK)
    property_balconies = models.PositiveIntegerField(choices=PROPERTY_BALCONIES)
    property_flor_number = models.PositiveIntegerField(choices=PROPERTY_FLOR_NO)
    property_covered_area = models.PositiveIntegerField()
    property_carpet_area = models.PositiveIntegerField()
    property_price = models.PositiveIntegerField()
    property_owner = models.CharField(validators=[name_regex], max_length=25)
    owner_contact = models.PositiveIntegerField(validators=[mobile_regex])
    mode = models.CharField(choices=MODE, max_length=10)
    property_picture = models.FileField(blank=False)

    def __str__(self):
        return self.wing_name

# HOUSEHOLD SERVICES TABLE
#######################################################################################################################


class HouseholdTypes(models.Model):

    services = models.CharField(validators=[name_regex], max_length=64)

    def __str__(self):
        return self.services


class HouseholdServices(models.Model):

    service_type = models.ForeignKey(HouseholdTypes, related_name="households", on_delete=models.PROTECT)
    service_person = models.CharField(validators=[name_regex], max_length=20)
    address = models.CharField(max_length=64)
    contact = models.PositiveIntegerField(validators=[mobile_regex])

    def __str__(self):
        return self.service_person

# MAINTENANCE PAYMENT
#######################################################################################################################


class Maintenance(models.Model):

    maintenance_month = models.CharField(max_length=64)
    maintenance_amount = models.PositiveIntegerField()
    maintenance_payment_mode = models.CharField(max_length=64)

    def __str__(self):
        return self.maintenance_amount

# COMPLAINT BOX TABLE
#######################################################################################################################


class ComplaintPost(models.Model):

    complaint_by = models.CharField(max_length=64)
    category = models.CharField(choices=Complaint_Category, max_length=20)
    subcategory = models.CharField(choices=complaint_subcategory, max_length=20)
    complaint_description = models.TextField(max_length=100)
    complaint_status = models.CharField(default='Initiate', max_length=64)
    date_time = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.category

# NOTICE BOARD TABLE
#######################################################################################################################


class NoticePost(models.Model):

    notice_by = models.CharField(max_length=64)
    notice_subject = models.CharField(validators=[name_regex], max_length=20)
    notice_description = models.TextField(max_length=100)
    notice_file = models.FileField(blank=True)
    date_time = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.notice_subject

# HALL ALLOCATION TABLE
########################################################################################################################


class Hall(models.Model):

    booked_by = models.CharField(max_length=64)
    date = models.DateField(default='yyyy-mm-dd')
    event_type = models.CharField(choices=hall_event, max_length=20)
    event_description = models.TextField(max_length=100)
    registration_date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.event_type

# ANNUAL REPORT
########################################################################################################################


class Report(models.Model):

    name = models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    file = models.FileField()

    def __str__(self):
        return self.name

# PREDICTION TABLE
########################################################################################################################


class Prediction(models.Model):

    bhk = models.PositiveIntegerField(choices=PROPERTY_BHK)
    sq_ft = models.PositiveIntegerField()
    built_year = models.PositiveIntegerField()

# VISITOR TABLE
########################################################################################################################


class Visitor(models.Model):

    visitor_prefix = models.CharField(choices=NAME_PREFIX, max_length=10)
    visitor_name = models.CharField(validators=[name_regex], max_length=20)
    host_name = models.ForeignKey(Profile, on_delete=models.PROTECT)
    date_and_time = models.DateTimeField(default=timezone.now())
    date_and_time_out = models.DateTimeField(blank=True, default=timezone.now())

    def __str__(self):
        return self.visitor_name


# VENDOR
########################################################################################################################

class Vendor(models.Model):

    name = models.CharField(validators=[name_regex], max_length=20)
    service = models.CharField(validators=[name_regex], max_length=30)
    days = models.CharField(max_length=30)
    timing = models.TimeField()
    contact = models.PositiveIntegerField(validators=[mobile_regex])

    def __str__(self):
        return '%s %s' % (self.name, self.service)


# COMMITTEE
########################################################################################################################

class Committee(models.Model):

    name = models.CharField(validators=[name_regex], max_length=30)
    flat = models.CharField(max_length=10)
    designation = models.CharField(choices=DESIGNATION, max_length=30)
    contact = models.PositiveIntegerField(validators=[mobile_regex])

    def __str__(self):
        return '%s %s' % (self.designation, self.name)


# POLL
########################################################################################################################

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=timezone.now())

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class VoteDone(models.Model):

    vote_by = models.ForeignKey(User, on_delete=models.PROTECT)
    byy = models.CharField(default=vote_by, max_length=30, primary_key=True)
    counter = models.IntegerField(default=0)

    def __str__(self):
        return self.byy

# BLOG
########################################################################################################################


class Blog(models.Model):

    blog_by = models.CharField(max_length=20)
    title = models.CharField(max_length=64)
    description = models.TextField()
    published_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse("basic_app:blog_home")

    def __str__(self):
        return self.title


class CommentAdd(models.Model):
    blog = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse("basic_app:blog_detail")

    def __str__(self):
        return self.text

