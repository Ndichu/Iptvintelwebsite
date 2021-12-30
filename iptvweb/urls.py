from django.urls import path, include
from . import views

urlpatterns = [
   path('',views.home, name="home"),
   path('About_Us',views.about, name="about"),
   path('features',views.features, name="features"),
   path('subscribe',views.subscribe, name="subscribe"),
   path('subscribe',views.subscribe2, name="subscribe2"),
   path('contact_Us',views.contact, name="contact"),
   path('signin',views.login_user, name="login_user"),
   path('register',views.register, name="register"),
   path('Dashboard/ADMIN/Superuser',views.Dashboard, name="dashboard"),
   path('Myprofilepage',views.profile, name="profile"),
   path('logout',views.logout, name="logout"),
   path('', include(('django.contrib.auth.urls'))),


   


]