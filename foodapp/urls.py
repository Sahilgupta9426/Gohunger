from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm
# MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm


urlpatterns = [
    path('meals/', views.ProductView.as_view(), name="meals"),
    path('login/', views.login, name="login"),
    # path('accounts/login/', auth_views.LoginView.as_view(template_name='htmls/login.html', authentication_form=LoginForm), name='login'),
    # path('profile/', views.ProfileView.as_view(), name='profile'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path("", views.index, name="index"),
    # path("meals/",views.meals,name="meals"),
    path("about/", views.about, name="about"),
    path("contact/", views.ContactUS, name="ContactUs"),
]