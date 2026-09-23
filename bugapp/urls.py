from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", views.register, name="register"),
    path("bugs/", views.bug_list, name="bug_list"),
    path("bugs/add/", views.bug_create, name="bug_create"),
    path("bugs/<int:pk>/", views.bug_detail, name="bug_detail"),
    path("bugs/<int:pk>/edit/", views.bug_update, name="bug_update"),
    path("bugs/<int:pk>/delete/", views.bug_delete, name="bug_delete"),
]
