from django.urls import path

from .views import HomePage,SignupView

app_name = "users"

urlpatterns = [
        path("",HomePage.as_view(), name = "home"),
        path("signup/",SignupView.as_view(), name="signup"),
        
]
