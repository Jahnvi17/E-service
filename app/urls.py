from django.urls import path,include
from . import views
urlpatterns = [
    
    ## Page Urls
    path("registerpage/",views.RegisterPage,name="registerpage"),
    path("",views.LoginPage,name="loginpage"),
    path("homepage/",views.HomePage,name="homepage"),
    path("otp/",views.otp,name="otp"),
    path("indexpage/",views.IndexPage,name="indexpage")



    ## Functionalty Urls
    path("registeruser/",views.registeruser,name="registeruser"),
    path("loginuser/",views.Loginuser,name="loginuser"),
    path("logout/",views.logout,name="logout"),
    path("u_verf/",views.user_verification,name="u_verf"),
]