from django.urls import path
from . import views


urlpatterns = [
    path('meals/', views.ProductView.as_view(), name="meals"),
    path("", views.index, name="index"),
    # path("meals/",views.meals,name="meals"),
    path("about/", views.about, name="about"),
    path("contact/", views.ContactUS, name="ContactUs"),
]