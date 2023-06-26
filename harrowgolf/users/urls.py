from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    # Welcome
    path("", views.welcome, name="welcome"),

    # Auth
    path("login", views.LoginView.as_view(), name="login"),
    path("signup/student", views.StudentSignupView.as_view(), name="student-signup"),
    path("signup/school", views.TeacherSignupView.as_view(), name="school-signup"),
    path("logout", views.logout_request, name='logout'),

    # School
    path("school", views.school_home, name="school-home"),
    path("school/golfcourses", views.school_golfcourses, name="school-golfcourses"),

    # Student
    path("student", views.student_home, name='student-home'),

]
