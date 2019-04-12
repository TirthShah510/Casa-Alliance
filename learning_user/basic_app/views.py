from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from basic_app.forms import UserForm, ProfileForm, HallForm, NoticeForm, PredictForm, ComplaintForm, PropertyForm, \
    VisitorForm, BlogForm, CommentAddForm, VehicleForm, StaffForm, UserChange
from basic_app import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,CreateView,ListView, DetailView, UpdateView, DeleteView)
from twilio.rest import Client
from django.contrib.auth.forms import UserChangeForm
from django.db.models import Q
from django.views import generic
from django.utils import timezone
from datetime import datetime

# FOR LOGIN IMPORT BELOW MENTION THINGS
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# MACHINE LEARNING

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.preprocessing import LabelEncoder


@login_required
def casa_home(request):
    return render(request, 'basic_app/casa_home.html')


def index(request):
    return render(request, 'basic_app/index.html')

# LOGOUT
#####################################################################################################################

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

# REGISTRATION OF USER
######################################################################################################################


def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.username_again = user
            profile.save()


            registered = True
            return HttpResponseRedirect(reverse('basic_app:user_login'))

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    return render(request, 'basic_app/profile_form.html', {'user_form': user_form, 'profile_form': profile_form})

# USER LOGIN
###################################################################################################################


def user_login(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                if user.is_staff and user.is_superuser:  # user is super user or not
                    return HttpResponseRedirect(reverse('admin:index'))
                elif user.is_staff and User.user_permissions:  # user is staff member or not
                    return HttpResponseRedirect(reverse('admin:index'))
                elif username == 'watchman':
                    return HttpResponseRedirect(reverse('basic_app:watchman_home'))
                else:  # user is member of society
                    return redirect('basic_app:casa_home')
            else:
                return HttpResponse('Account not active')
        else:
            return HttpResponse('Invalid Login Details!')
    else:
        return render(request, 'basic_app/login.html', {})

# LOGIN HOME
##################################################################################################################


@login_required
def watchman_home(request):

    return render(request, 'basic_app/watchman_home.html', {})


@login_required
def home(request):

    obj = models.Profile.objects.filter(Q(user__username__icontains=request.user.username))

    return render(request, 'basic_app/home.html', {'image': obj})

# PROPERTY TRACKER
###################################################################################################################


def property_public(request):
    obj = models.Property.objects.filter(Q(mode__icontains='public'))

    if obj:
        return render(request, 'basic_app/property_list.html', {'list': obj})
    else:
        return HttpResponse('No result found')


@login_required
def property_home(request):
    return render(request, 'basic_app/property_home.html', {})


@login_required
def property_create(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=True)
            obj.registered_by = request.user.username
            obj.save()
            return redirect('basic_app:property_notify')
    else:
        form = PropertyForm()
    return render(request, 'basic_app/property_form.html', {
        'form': form
    })


@login_required
def property_notify(request):

    account_sid = 'ACf1d0435bf860c66ce726f10d9f782ce3'  # Found on Twilio Console Dashboard
    auth_token = 'd9e2476b85af76eba2ef60a45a40d7af'  # Found on Twilio Console Dashboard

    myPhone = '+919601448989'  # Phone number you used to verify your Twilio account
    TwilioNumber = '+17632519834'  # Phone number given to you by Twilio

    client = Client(account_sid, auth_token)

    client.messages.create(
        to=myPhone,
        from_=TwilioNumber,
        body='\nNew property has been registered on the CASA ALLIANCE by: ' + request.user.username + u'\U0001f680')

    return HttpResponseRedirect(reverse('basic_app:property_home'))


@login_required
def property_list(request):

    obj = models.Property.objects.all()

    if obj:
        return render(request, 'basic_app/property_list.html', {'list': obj})
    else:
        return HttpResponse('No result found')


@login_required
def property_manage(request):

    if request.user.username == 'sachin':
        obj = models.Property.objects.all()

        if obj:
            return render(request, 'basic_app/property_manage.html', {'list': obj})
        else:
            return HttpResponse('No result found')
    else:

        obj = models.Property.objects.filter(Q(registered_by__icontains=request.user.username))

        if obj:
            return render(request, 'basic_app/property_manage.html', {'list': obj})
        else:
            return HttpResponse('No result found')


class PropertyUpdateView(LoginRequiredMixin, UpdateView):

    fields = ('wing_name', 'property_for', 'property_type', 'property_BHK', 'property_balconies', 'property_flor_number'
              , 'property_covered_area', 'property_carpet_area', 'property_price', 'property_owner', 'owner_contact',
              'mode', 'property_picture')

    model = models.Property

    success_url = reverse_lazy('basic_app:property_home')


class PropertyDeleteView(LoginRequiredMixin, DeleteView):

    model = models.Property

    success_url = reverse_lazy("basic_app:property_home")


class PropertyDetailView(LoginRequiredMixin, DetailView):

    context_object_name = "property_detail"
    model = models.Property
    template_name = 'basic_app/property_detail.html'


@login_required
def property_search(request):

    if request.method == "POST":
        srch = request.POST['srh']

        if srch:
            match = models.Property.objects.filter(Q(property_for__icontains=srch))

            if match:
                return render(request, 'basic_app/property_search.html', {'list': match})
            else:
                return HttpResponse('no result found')
        else:
            return HttpResponse('nothing')

    return render(request, 'basic_app/property_search.html')

# HOUSEHOLD SERVICES
####################################################################################################################


def service_request(request):

    if request.method == "POST":
        type = request.POST['type']
        name = request.POST['name']
        address = request.POST['add']
        mobile = request.POST['mobile']

        #contact = request.user.profile.contact_no
        #str_contact = str(contact)
        #str_flat = str(request.user.profile.flat_no)

        account_sid = 'ACf1d0435bf860c66ce726f10d9f782ce3'  # Found on Twilio Console Dashboard
        auth_token = 'd9e2476b85af76eba2ef60a45a40d7af'  # Found on Twilio Console Dashboard

        myPhone = '+919601448989'  # Phone number you used to verify your Twilio account
        TwilioNumber = '+17632519834'  # Phone number given to you by Twilio

        client = Client(account_sid, auth_token)

        client.messages.create(
            to=myPhone,
            from_=TwilioNumber,
            body='\nNotification for service registration \nService Type: ' + type + '\nName: ' + name +
                 '\nAddress: ' + address + '\nContact No: ' + mobile + '******' + u'\U0001f680')

        return render(request, 'basic_app/service_request_success.html')

    return render(request, 'basic_app/service_request_form.html')


@login_required
def household_search(request):
    if request.method == "POST":
        srch = request.POST['srh']

        if srch:
            match = models.HouseholdServices.objects.filter(Q(service_type__services__icontains=srch))

            if match:
                return render(request, 'basic_app/household_search.html', {'sr': match})

            else:
                return HttpResponse('no result found')
        else:
            return HttpResponse('nothing')

    return render(request, 'basic_app/household_search.html')


@login_required
def service_notify(request):

    contact = request.user.profile.contact_no
    str_contact = str(contact)
    str_flat = str(request.user.profile.flat_no)

    account_sid = 'ACf1d0435bf860c66ce726f10d9f782ce3'  # Found on Twilio Console Dashboard
    auth_token = 'd9e2476b85af76eba2ef60a45a40d7af'  # Found on Twilio Console Dashboard

    myPhone = '+919601448989'  # Phone number you used to verify your Twilio account
    TwilioNumber = '+17632519834'  # Phone number given to you by Twilio

    client = Client(account_sid, auth_token)

    client.messages.create(
        to=myPhone,
        from_=TwilioNumber,
        body='\nNotification for service requirement from:' + request.user.username + '\nFlat No: ' + str_flat +
            '\nContact No: ' + str_contact + '******' + u'\U0001f680')

    return redirect('basic_app:household_success')


@login_required
def household_success(request):
    return render(request, 'basic_app/household_success.html')


# MAINTENANCE PAYMENT
########################################################################################################################


@login_required
def maintenance_payment(request):

    return render(request, 'basic_app/maintenance_form.html', {})


@login_required
def maintenance_netbanking(request):

    return render(request, 'basic_app/maintenance_card.html', {})


@login_required
def maintenance_success(request):

    return render(request, 'basic_app/maintenance_receipt.html', {})

# COMPLAINT BOX
###################################################################################################################


def complaint_home(request):

    return render(request, 'basic_app/complaint_form.html', {})


@login_required
def complaint_create(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=True)
            obj.complaint_by = request.user.username
            obj.save()
            return redirect('basic_app:complaint_notify')
    else:
        form = ComplaintForm()
    return render(request, 'basic_app/complaintpost_form.html', {
        'form': form
    })


@login_required
def complaint_notify(request):
    obj = models.ComplaintPost.objects.latest('id')

    account_sid = 'ACf1d0435bf860c66ce726f10d9f782ce3'  # Found on Twilio Console Dashboard
    auth_token = 'd9e2476b85af76eba2ef60a45a40d7af'  # Found on Twilio Console Dashboard

    contact = '+919601448989'  # Phone number you used to verify your Twilio account
    twilio_number = '+17632519834'  # Phone number given to you by Twilio

    client = Client(account_sid, auth_token)

    client.messages.create(
        to=contact,
        from_=twilio_number,
        body='\nComplaint By: ' + request.user.username + '\nComplaint Category: ' + obj.category +
             '\nComplaint Subcategory:' + obj.subcategory + '\nComplaint Description: ' + obj.complaint_description +
             u'\U0001f680')

    return HttpResponseRedirect(reverse('basic_app:complaint_status'))


@login_required
def complaint_status(request):

    obj = models.ComplaintPost.objects.filter(Q(complaint_by__icontains=request.user.username))

    if obj:
        return render(request, 'basic_app/complaint_list.html', {'list': obj})
    else:
        return HttpResponse('No result found')


# PROFILE VIEW
#####################################################################################################################


@login_required
def view_profile(request):

    obj = models.Profile.objects.filter(Q(username_again__exact=request.user.username))

    if obj:
        return render(request, 'basic_app/view_profile.html', {'list': obj})
    else:
        return HttpResponse('No result found')


# PROFILE CHANGE
#######################################################################################################################


@login_required
def edit_profile(request):

    if request.method == 'POST':
        form = UserChange(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('basic_app:view_profile')
    else:
        form = UserChange(instance=request.user)
        args = {'form': form}
        return render(request, 'basic_app/edit_profile.html', args)

# NOTICE BOARD
#####################################################################################################################


@login_required
def notice_home(request):

    return render(request, 'basic_app/notice_home.html')


@login_required
def model_form_upload(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=True)
            obj.notice_by = request.user.username
            obj.save()
            return redirect('basic_app:notice_notify')
    else:
        form = NoticeForm()
    return render(request, 'basic_app/noticepost_form.html', {
        'form': form
    })


@login_required
def notice_notify(request):

    #  comp = models.Complaint.objects.filter()
    obj = models.NoticePost.objects.latest('id')

    account_sid = 'ACf1d0435bf860c66ce726f10d9f782ce3'  # Found on Twilio Console Dashboard
    auth_token = 'd9e2476b85af76eba2ef60a45a40d7af'  # Found on Twilio Console Dashboard

    contact = '+919601448989'  # Phone number you used to verify your Twilio account
    system_no = '+17632519834'  # Phone number given to you by Twilio

    client = Client(account_sid, auth_token)

    client.messages.create(
        to=contact,
        from_=system_no,
        body='\nNotice By: ' + request.user.username + '\nNotice Subject: ' + obj.notice_subject +
             '\nNotice Description: ' + obj.notice_description + u'\U0001f680')

    return HttpResponseRedirect(reverse('basic_app:notice_list'))


@login_required
def notice_list(request):

    obj = models.NoticePost.objects.all()

    if obj:
        return render(request, 'basic_app/notice_list.html', {'list': obj})
    else:
        return HttpResponse('No result found')


@login_required
def notice_edit(request):
    obj = models.NoticePost.objects.filter(Q(notice_by__icontains=request.user.username))

    if obj:
        return render(request, 'basic_app/notice_edit.html', {'list': obj})
    else:
        return HttpResponse('No result found')


class NoticeUpdateView(LoginRequiredMixin, UpdateView):

    fields = ('notice_subject', 'notice_description', 'notice_file')
    model = models.NoticePost

    success_url = reverse_lazy('basic_app:home')


class NoticeDeleteView(LoginRequiredMixin, DeleteView):

    model = models.NoticePost

    success_url = reverse_lazy("basic_app:home")


# HALL ALLOCATION
#####################################################################################################################


@ login_required
def hall(request):

    if request.method == 'POST':
        form = HallForm(request.POST)
        event_date = request.POST.get('date')
        format_str = '%Y-%m-%d'
        date_obj = datetime.strptime(event_date, format_str)
        date1 = datetime.now().date()

        if date_obj.date() <= date1:  # check that date is not less than current date
            return redirect('basic_app:hall_failure')
        else:
            match = models.Hall.objects.filter(Q(date__exact=event_date))  # check that same date is not registered

            if match:
                return redirect('basic_app:hall_failure')
            else:
                obj = form.save(commit=True)
                obj.booked_by = request.user.username
                obj.save()
                return redirect('basic_app:hall_notify')
    else:
        form = HallForm()
    return render(request, 'basic_app/hall_form.html', {'form': form})


@login_required
def hall_failure(request):

    return render(request, 'basic_app/hall_failure.html', {})


@login_required
def hall_success(request):

    return render(request, 'basic_app/hall_success.html', {})


@login_required
def hall_manage(request):

    obj = models.Hall.objects.filter(Q(booked_by__exact=request.user.username))

    if obj:
        return render(request, 'basic_app/hall_booking_list.html', {'list': obj})
    else:
        return HttpResponse('No result found')


class HallUpdateView(LoginRequiredMixin, UpdateView):

    fields = ('date', 'event_type', 'event_description')
    model = models.Hall

    success_url = reverse_lazy('basic_app:hall')


class HallDeleteView(LoginRequiredMixin, DeleteView):

    model = models.Hall

    success_url = reverse_lazy("basic_app:hall_manage")


@login_required
def hall_notify(request):

    #  obj1 = models.Hall.objects.latest('id')

    #  obj2 = models.Profile.objects.get(Q(first_name__icontains=obj1.host_name))  # For respective Contact Number
    #  no = obj2.contact_no

    account_sid = 'ACf1d0435bf860c66ce726f10d9f782ce3'  # Found on Twilio Console Dashboard
    auth_token = 'd9e2476b85af76eba2ef60a45a40d7af'  # Found on Twilio Console Dashboard

    contact = '+919601448989'  # Phone number you used to verify your Twilio account
    twilio_number = '+17632519834'  # Phone number given to you by Twilio

    client = Client(account_sid, auth_token)

    client.messages.create(
        to=contact,
        from_=twilio_number,
        body='\n*****NEW BOOKING has been done*****\n' + u'\U0001f680')

    return HttpResponseRedirect(reverse('basic_app:hall_success'))


# FUNDS
########################################################################################################################


@ login_required
def funds(request):

    obj = models.Report.objects.all()

    if obj:
        return render(request, 'basic_app/funds.html', {'list': obj})
    else:
        return HttpResponse('No result found')

# PROFILE SEARCH
########################################################################################################################


@login_required
def search(request):
    if request.method == "POST":
        srch = request.POST['srh']

        if srch:
            match = models.Profile.objects.filter(Q(occupation__icontains=srch) | Q(first_name__icontains=srch)
                                                  | Q(last_name__icontains=srch) | Q(wing_name__icontains=srch)
                                                  | Q(flat_no__icontains=srch))

            if match:
                return render(request, 'basic_app/search.html', {'sr': match})

            else:
                return HttpResponse('no result found')
        else:
            return HttpResponse('nothing')

    return render(request, 'basic_app/search.html')

# PREDICTION MODEL
#####################################################################################################################


@login_required
def prediction_form(request):

    if request.method == "POST":
        form = PredictForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('basic_app:prediction_result'))
    else:
        form = PredictForm
        args = {'form': form}
        return render(request, 'basic_app/prediction_form.html', args)


@login_required
def prediction_result(request):

    obj = models.Prediction.objects.latest('id')

    data = pd.read_csv("C:/Starc/noti/basic/hp_data.csv")
    data = data.iloc[:, 1:]
    #  enc = LabelEncoder()
    #  data.iloc[:, 1] = enc.fit_transform(data.iloc[:, 1])
    x = data.iloc[:, [1, 2, 3]]
    y = data.SalePrice
    x = pd.get_dummies(x, drop_first=True)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.3)
    linear = LinearRegression()
    linear.fit(x_train, y_train)
    data = [obj.bhk, obj.sq_ft, obj.built_year]
    xnew = np.array(data)
    ynew = linear.predict(xnew.reshape(1, -1))  # reshape row = 1 and column = unknown
    #  score = r2_score(y_test, ynew)
    return render(request, "basic_app/prediction_result.html", {'result': ynew})


# VISITOR
########################################################################################################################


@login_required
def visitor_form(request):
    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('basic_app:visitor_notify')
    else:
        form = VisitorForm()
    return render(request, 'basic_app/visitor_form.html', {'form': form})


@login_required
def visitor_notify(request):

    obj1 = models.Visitor.objects.latest('id')

    #  obj2 = models.Profile.objects.get(Q(first_name__icontains=obj1.host_name))  # For respective Contact Number
    #  no = obj2.contact_no

    account_sid = 'ACf1d0435bf860c66ce726f10d9f782ce3'  # Found on Twilio Console Dashboard
    auth_token = 'd9e2476b85af76eba2ef60a45a40d7af'  # Found on Twilio Console Dashboard

    contact = '+919601448989'  # Phone number you used to verify your Twilio account
    twilio_number = '+17632519834'  # Phone number given to you by Twilio

    client = Client(account_sid, auth_token)

    client.messages.create(
        to=contact,
        from_=twilio_number,
        body='\nVisitor Name: ' + obj1.visitor_name + u'\U0001f680')

    return render(request, 'basic_app/watchman_home.html')


@login_required
def visitor_list(request):

    obj = models.Visitor.objects.all()

    if obj:
        return render(request, 'basic_app/visitor_list.html', {'list': obj})
    else:
        return HttpResponse('No result found')


class VisitorUpdateView(LoginRequiredMixin, UpdateView):

    fields = ('time_out',)

    model = models.Visitor

    success_url = reverse_lazy('basic_app:watchman_home')


@login_required
def visitor_out(request, pk):

    obj = models.Visitor.objects.get(pk=pk)
    obj.date_and_time_out = timezone.now()
    obj.save()
    return redirect('basic_app:watchman_home')


# Directory
#####################################################################################################################


@login_required
def directory(request):

    return render(request, 'basic_app/directory.html', {})


@login_required
def vendors(request):

    obj = models.Vendor.objects.all()

    if obj:
        return render(request, 'basic_app/vendors.html', {'list': obj})
    else:
        return HttpResponse('No result found')


@login_required
def neighbours(request):

    obj = models.Profile.objects.all()

    if obj:
        return render(request, 'basic_app/neighbours.html', {'sr': obj})
    else:
        return HttpResponse('NOOOOO')


@login_required
def committee(request):

    obj = models.Committee.objects.all()

    if obj:
        return render(request, 'basic_app/committee.html', {'list': obj})
    else:
        return HttpResponse('NOOOOO')

# Poll
#####################################################################################################################


class PollIndexView(LoginRequiredMixin, ListView):
    template_name = 'basic_app/poll_index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return models.Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class PollDetailView(LoginRequiredMixin, DetailView):
    model = models.Question
    template_name = 'basic_app/poll_detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return models.Question.objects.filter(pub_date__lte=timezone.now())


@login_required
def vote(request, question_id):
    question = get_object_or_404(models.Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, models.Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'basic_app/poll_detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:

        obj = models.VoteDone.objects.get(byy__exact=request.user.username)
        no = obj.counter
        if no == 0:
            obj.counter = 1
            obj.save()
            selected_choice.votes += 1
            selected_choice.save()
        else:
            return HttpResponse('You have submitted your VOTE')

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('basic_app:poll_results', args=(question.id,)))


class PollResultsView(LoginRequiredMixin, DetailView):
    model = models.Question
    template_name = 'basic_app/poll_results.html'

# BLOG
#####################################################################################################################


@login_required
def blog_home(request):

    return render(request, 'basic_app/blog_home.html', {})


@login_required
def blog_create(request):

    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=True)
            obj.blog_by = request.user.username
            obj.save()
            return redirect('basic_app:blog_home')
    else:
        form = BlogForm()
    return render(request, 'basic_app/blog_form.html', {'form': form})


@login_required
def blog_list(request):

    obj = models.Blog.objects.all()

    if obj:
        return render(request, 'basic_app/blog_list.html', {'list': obj})
    else:
        return HttpResponse('No result found')


class BlogDetailView(LoginRequiredMixin, DetailView):

    context_object_name = "blog_detail"
    model = models.Blog
    template_name = 'basic_app/blog_detail.html'


@login_required
def blog_manage(request):

    obj = models.Blog.objects.filter(Q(blog_by__exact=request.user.username))

    if obj:
        return render(request, 'basic_app/blog_manage.html', {'list': obj})
    else:
        return HttpResponse('No result found')


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    fields = ('title', 'description')

    model = models.Blog

    success_url = reverse_lazy('basic_app:blog_home')


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Blog

    success_url = reverse_lazy("basic_app:blog_home")


@login_required
def add_comment(request, pk):

    blog = get_object_or_404(models.Blog, pk=pk)

    if request.method == 'POST':
        form = CommentAddForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user.username
            comment.blog = blog
            comment.save()
            return redirect('basic_app:blog_home')
    else:
        form = CommentAddForm()
    return render(request, 'basic_app/commentadd_form.html', {'form': form})


@login_required
def comment_list(request, pk):

    blog = get_object_or_404(models.Blog, pk=pk)

    obj = models.CommentAdd.objects.filter(Q(blog__icontains=blog))

    if obj:
        return render(request, 'basic_app/comment_list.html', {'list': obj})
    else:
        return HttpResponse('No Comments')


class CommentAddUpdateView(LoginRequiredMixin, UpdateView):

    fields = ('text',)

    model = models.CommentAdd

    success_url = reverse_lazy('basic_app:blog_list')


class CommentAddDeleteView(LoginRequiredMixin, DeleteView):
    model = models.CommentAdd

    success_url = reverse_lazy("basic_app:blog_list")

#######################################################################################################################


@login_required
def flat_view(request):

    obj = models.Profile.objects.filter(Q(username_again__exact=request.user.username))

    if obj:
        return render(request, 'flat/flat_view.html', {'list': obj})
    else:
        return HttpResponse('No Found')


@login_required
def vehicle_form(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=True)
            obj.owner = request.user.username
            obj.save()
            return redirect('basic_app:flat')
    else:
        form = VehicleForm()
    return render(request, 'basic_app/vehicle_form.html', {'form': form})


@login_required
def vehicle_list(request):

    obj = models.Vehicle.objects.filter(Q(owner__exact=request.user.username))

    if obj:
        return render(request, 'basic_app/vehicle_list.html', {'list': obj})
    else:
        return HttpResponse('No Vehicle(s)')


class VehicleUpdateView(LoginRequiredMixin, UpdateView):
    fields = ('type', 'number')

    model = models.Vehicle

    success_url = reverse_lazy('basic_app:vehicle_list')


class VehicleDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Vehicle

    success_url = reverse_lazy("basic_app:vehicle_list")


@login_required
def staff_form(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=True)
            obj.owner = request.user.username
            obj.save()
            return redirect('basic_app:flat')
    else:
        form = StaffForm()
    return render(request, 'basic_app/staff_form.html', {'form': form})


@login_required
def staff_list(request):

    obj = models.Staff.objects.filter(Q(owner__exact=request.user.username))

    if obj:
        return render(request, 'basic_app/staff_list.html', {'list': obj})
    else:
        return HttpResponse('No Staff')


class StaffUpdateView(LoginRequiredMixin, UpdateView):
    fields = ('servant', 'service', 'full_name')

    model = models.Staff

    success_url = reverse_lazy('basic_app:staff_list')


class StaffDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Staff

    success_url = reverse_lazy("basic_app:staff_list")


@login_required
def flat_edit(request, pk):

    instance = get_object_or_404(models.Profile, pk=pk)
    form = ProfileForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('basic_app:flat')
    return render(request, 'flat/flat_edit.html', {'form': form})

########################################################################################################################

