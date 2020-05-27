from django.urls import path

from .views import PagesHome

app_name = "pages"

urlpatterns = [
    path("",PagesHome.as_view(), name="home"),

]
