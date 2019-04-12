from django.conf.urls import url
from basic_app import views


app_name = 'basic_app'

urlpatterns = [

    url(r'^casa_home/$', views.casa_home, name='casa_home'),

    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^home/$',views.home,name='home'),

    url(r'^watchman_home/$',views.watchman_home, name='watchman_home'),
    url(r'^visitor_form/$',views.visitor_form, name='visitor_form'),
    url(r'^visitor_notify/$', views.visitor_notify, name='visitor_notify'),
    url(r'^visitor_list/$', views.visitor_list, name='visitor_list'),
    url(r'^visitor_list/visitor_update/(?P<pk>\d+)/$', views.VisitorUpdateView.as_view(), name='visitor_update'),
    url(r'^visitor_list/visitor_out/(?P<pk>\d+)/$', views.visitor_out, name='visitor_out'),

    url(r'^property_public/$', views.property_public, name='property_public'),
    url(r'^property_public/(?P<pk>\d+)/$',views.PropertyDetailView.as_view(),name='property_detail'),
    url(r'^property_home/$',views.property_home,name='property_home'),
    url(r'^property/$',views.property_create,name='property'),
    url(r'^property_search/$', views.property_search, name='property_search'),
    url(r'^property_search/(?P<pk>\d+)/$',views.PropertyDetailView.as_view(),name='property_detail'),
    url(r'^property_search/$', views.property_search, name='property_search'),
    url(r'^property_search/(?P<pk>\d+)/$',views.PropertyDetailView.as_view(),name='property_detail'),
    url(r'^property_manage/$', views.property_manage, name='property_manage'),
    url(r'^property_manage/property_update/(?P<pk>\d+)/$',views.PropertyUpdateView.as_view(),name="property_update"),
    url(r'^property_delete/(?P<pk>\d+)/$',views.PropertyDeleteView.as_view(),name="property_delete"),
    url(r'^property_manage/(?P<pk>\d+)/$',views.PropertyDetailView.as_view(),name='property_detail'),
    url(r'^property_notify/$',views.property_notify,name='property_notify'),

    url(r'^service_request/$', views.service_request, name='service_request'),

    url(r'^household_search/$',views.household_search,name='household_search'),
    url(r'^service_notify/$',views.service_notify,name='service_notify'),
    url(r'^household_success/$', views.household_success, name='household_success'),

    url(r'^maintenance/$',views.maintenance_payment,name='maintenance'),
    url(r'^maintenance_netbanking/$',views.maintenance_netbanking,name='maintenance_netbanking'),
    url(r'^maintenance_success/$',views.maintenance_success,name='maintenance_success'),

    url(r'^view_profile/$',views.view_profile,name='view_profile'),
    url(r'^edit_profile/$',views.edit_profile,name='edit_profile'),

    url(r'^complaint_home/$',views.complaint_home,name='complaint_home'),
    url(r'^complaint/$',views.complaint_create,name='complaint'),
    url(r'^complaint_notify/$',views.complaint_notify,name='complaint_notify'),
    url(r'^complaint_status/$',views.complaint_status,name='complaint_status'),

    url(r'^notice_home/$',views.notice_home,name='notice_home'),
    url(r'^notice_post/$',views.model_form_upload,name='notice_post'),
    url(r'^notice_list/$',views.notice_list,name='notice_list'),
    url(r'^notice_edit/$',views.notice_edit,name='notice_edit'),
    url(r'^notice_edit/notice_update/(?P<pk>\d+)/$', views.NoticeUpdateView.as_view(),
        name="notice_update"),
    url(r'^notice_delete/(?P<pk>\d+)/$',views.NoticeDeleteView.as_view(),name='notice_delete'),
    url(r'^notice_notify/$',views.notice_notify,name='notice_notify'),

    url(r'^hall/$',views.hall,name='hall'),
    url(r'^hall_notify/$', views.hall_notify, name='hall_notify'),
    url(r'^hall_failure/$',views.hall_failure,name='hall_failure'),
    url(r'^hall_success/$', views.hall_success, name='hall_success'),
    url(r'^hall_manage/$',views.hall_manage, name='hall_manage'),
    url(r'^hall_manage/hall_booking_update/(?P<pk>\d+)/$', views.HallUpdateView.as_view(),
        name="hall_booking_update"),
    url(r'^hall_booking_delete/(?P<pk>\d+)/$',views.HallDeleteView.as_view(),name='hall_booking_delete'),

    url(r'^funds/$',views.funds,name='funds'),

    url(r'^prediction/$',views.prediction_form,name='prediction'),
    url(r'^prediction_result/$',views.prediction_result,name='prediction_result'),

    url(r'^directory/$', views.directory, name='directory'),
    url(r'^vendors/$', views.vendors, name='vendors'),
    url(r'^neighbours/$', views.neighbours, name='neighbours'),
    url(r'^committee/$', views.committee, name='committee'),

    url(r'^poll_index/$', views.PollIndexView.as_view(), name='poll_index'),
    url(r'^poll_index/(?P<pk>\d+)/$', views.PollDetailView.as_view(), name='poll_detail'),
    url(r'^poll_index/(?P<question_id>\d+)/poll_vote/$', views.vote, name='poll_vote'),
    url(r'^poll_index/(?P<pk>\d+)/results/$', views.PollResultsView.as_view(), name='poll_results'),

    url(r'^blog_home/$', views.blog_home, name='blog_home'),
    url(r'^blog_create/$', views.blog_create, name='blog_create'),
    url(r'^blog_list/$', views.blog_list, name='blog_list'),
    url(r'^blog_list/(?P<pk>\d+)/$', views.BlogDetailView.as_view(), name='blog_detail'),
    url(r'^blog_manage/$', views.blog_manage, name='blog_manage'),
    url(r'^blog_manage/blog_update/(?P<pk>\d+)/$', views.BlogUpdateView.as_view(),name="blog_update"),
    url(r'^blog_delete/(?P<pk>\d+)/$',views.BlogDeleteView.as_view(),name="blog_delete"),
    url(r'^blog_list/(?P<pk>\d+)/add_comment/$', views.add_comment, name='add_comment'),
    url(r'^blog_list/comment_list/(?P<pk>\d+)/$', views.comment_list, name='comment_list'),
    url(r'^blog_list/comment_list/comment_update/(?P<pk>\d+)/$', views.CommentAddUpdateView.as_view(), name='comment_update'),
    url(r'^comment_delete/(?P<pk>\d+)/$', views.CommentAddDeleteView.as_view(), name='comment_delete'),

    url(r'^flat/$', views.flat_view, name='flat'),
    url(r'^flat/flat_edit/(?P<pk>\d+)/$', views.flat_edit, name='flat_edit'),

    url(r'^flat/vehicle_form/$', views.vehicle_form, name='vehicle_form'),
    url(r'^flat/vehicle_list/$', views.vehicle_list, name='vehicle_list'),
    url(r'^flat/vehicle_list/vehicle_update/(?P<pk>\d+)/$',views.VehicleUpdateView.as_view(),name="vehicle_update"),
    url(r'^flat/vehicle_delete/(?P<pk>\d+)/$',views.VehicleDeleteView.as_view(),name="vehicle_delete"),

    url(r'^staff_form/$', views.staff_form, name='staff_form'),
    url(r'^staff_list/$', views.staff_list, name='staff_list'),
    url(r'^staff_list/staff_update/(?P<pk>\d+)/$', views.StaffUpdateView.as_view(),name="staff_update"),
    url(r'^staff_delete/(?P<pk>\d+)/$', views.StaffDeleteView.as_view(),name="staff_delete"),






]