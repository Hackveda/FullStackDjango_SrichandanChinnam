
from django.http import HttpResponse
from .models import Student
from django.shortcuts import render
from .forms import StudentLoginForm

def say_hello(request):
    print("abc")
    return HttpResponse('Hi Shivam, Welcome to django')


def say_shivam(request):
    print("I am in say_shivam")
    return HttpResponse('Hi Shivam')

def get_name(request, name):
    print("I am in get_name", name)
    return HttpResponse(f'My Name is : {name}')


def create_student(request):
   student = Student.objects.create(first_name='Preeti',last_name='M', address='3/1-20, WhiteField, Bangalore', pincode=511121 )
   return HttpResponse('Student is created')

def no_of_students_in_class(request):
    students = Student.objects.all()
    print(students)
    return HttpResponse('No. of students got it from Database')

def only_student_info(request,id):
    student = Student.objects.get(pk=id)
    print(student)
    return HttpResponse(student)

def to_delete_student(request,id):
    student = Student.objects.filter(pk=id).delete()
    print(student)
    return HttpResponse('Student is deleted')



def student_login(request):
    username = "User is not logged in"
    
    if request.method == "POST":
        #Get the posted form
        my_login_form = StudentLoginForm(request.POST)
        
        if my_login_form.is_valid():
            username = my_login_form.cleaned_data['username']
            request.session['username'] = username
    else:
        my_login_form = StudentLoginForm()
        print(my_login_form,";;;;;;;;;;;;")
    return render(request, 'student_loggedin.html', {"username" : username})
    

def check_user_access(request):
    if request.session.has_key('username'):
        username = request.session['username']
        return render(request, 'student_loggedin.html', {"username" : username})
    else:
        return render(request, 'student_login.html', {})