from django.urls import path
from . import views

urlpatterns = [
    path("", views.course_list, name="course_list"),
    path("courses", views.course_list, name="course_list"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("my_courses", views.my_courses, name="my_courses"),
    path("course/<int:course_id>/", views.course_detail, name="course_detail"),
]
