
from django.http import HttpResponse
from .models import Student, Employee
from django.shortcuts import render
from .forms import StudentLoginForm
from rest_framework.decorators import api_view

def say_hello(request):
    print("abc")
    return HttpResponse('Hi Shivam, Welcome to django')


def say_shivam(request):
    print("I am in say_shivam")
    return HttpResponse('Hi Shivam')

def get_name(request, name):
    print("I am in get_name", name)
    return HttpResponse(f'My Name is : {name}')


@api_view(['POST'])
def create_student(request):
   data = request.data
   first_name = data['first_name']
   last_name = data['last_name']
   address = data['address']
   pincode = data['pincode']
#    student = Student.objects.create(first_name='Surya',last_name='B', address='Old Area, Hyderabad', pincode=500005 )
   student = Student.objects.create(first_name=first_name,last_name=last_name, address=address, pincode=pincode )
   return HttpResponse('Student is created')

@api_view(['POST'])
def create_employee(request):
   emp = Employee.objects.create(empname='Shivam', empId= 10000123)
   return HttpResponse('Employee is created')

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
    return render(request, 'student_loggedin.html', {"username" : username})
    

def check_user_access(request):
    if request.session.has_key('username'):
        username = request.session['username']
        return render(request, 'student_loggedin.html', {"username" : username})
    else:
        return render(request, 'student_login.html', {})


