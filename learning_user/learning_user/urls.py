from django.conf.urls import url,include
from django.contrib import admin
from basic_app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView

urlpatterns = [

    url(r'^$',views.index,name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^basic_app/',include('basic_app.urls')),
    url(r'^logout/',views.user_logout,name='logout'),
    url(r'^reset_password/$',PasswordResetView.as_view(),name='reset_password'),
    url(r'^reset_password/done/$',PasswordResetDoneView.as_view(),name='password_reset_done'),
    url(r'^reset_password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    url(r'^reset_password/complete/$',PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    url(r'^search/$',views.search,name='search'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
