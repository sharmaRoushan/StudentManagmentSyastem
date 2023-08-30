from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views,Hod_views,Staff_views,Student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base',views.base,name='base'),
    # path('singhup',views.singhup,name='singhup'),
    #  login path
    path('',views.Login,name='Login'),
    path('dologin',views.dologin,name='dologin'),



    

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
