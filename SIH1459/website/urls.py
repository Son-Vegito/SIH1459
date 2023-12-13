from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('logout/',views.logout_user,name='logout'),
    path("student_page", views.student_page, name='student_page'),

    path("courses_page", views.courses_page, name='courses_page'),
    path('courses_search', views.courses_search, name='courses_search'),

    path("schemes_page", views.schemes_page, name='schemes_page'),
    path("schemes_search", views.schemes_search, name='schemes_search'),

    path("state_page", views.state_page, name='state_page'),


    path("college_page", views.college_page, name='college_page'),
    path('add_college/',views.add_college ,name='add_college'),

    path('add_scheme/',views.add_scheme,name='add_scheme'),
    path('add_course/',views.add_course,name='add_course'),
    path('search_student/',views.search_student,name='search_student'),

]
