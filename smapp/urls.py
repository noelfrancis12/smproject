from django.urls import path
from . import views  # Assuming your views are in the same directory or package



urlpatterns = [
    path("", views.home, name="home"),
    path('login1',views.login1,name='login1'),
    path('logout',views.logout,name='logout'),
    path('adminprofile/',views.adminprofile,name='adminprofile'),
    path('signup',views.signup,name='signup'),
    path('signupdb',views.signupdb,name='signupdb'),
    path('userprofile/',views.userprofile,name='userprofile'),
]