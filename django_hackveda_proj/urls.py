"""django_hackveda_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import say_hello, say_shivam, get_name, create_student, check_user_access, student_login, no_of_students_in_class, only_student_info,to_delete_student

from django.contrib.auth import views as auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', say_hello),
    path('shivam/',say_shivam),
    path('get_name/<str:name>/',get_name),

    path('create_student', create_student),
    path('no_of_students_in_class', no_of_students_in_class),
    path('only_student_info/<str:id>',only_student_info),
    path('to_delete_student/<str:id>',to_delete_student),

    path('connection/',check_user_access, name = 'loginform'),
	path('student_login/', student_login, name = 'student_login')


]
