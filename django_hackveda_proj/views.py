
from django.http import HttpResponse, JsonResponse
from .models import Student, Employee
from django.shortcuts import render
from .forms import StudentLoginForm
from rest_framework.decorators import api_view
from .serializers import StudentSerializer
import numpy as np 
import pandas as pd

def create_numpy_array(request):
    a = np.array(['Shivam','Srichandan', 'Sarath'])
    b = pd.Series(a)
    print(b)
    return HttpResponse('Created Numpy Array')

def create_pd_series_from_dict(request):
    dict = {'a':1, 'b' : 2, 'c' : 3, 'd' : 4}
    s = pd.Series(dict)
    print(s)
    return HttpResponse('create_pd_series_from_dict')

def create_pd_df_from_list(request):
    a = [1,2,3,4,5]
    df = pd.DataFrame(a)
    print(df)
    return HttpResponse('create_pd_df_from_list')

def create_pd_df_from_list_of_lists(request):
    a = [['Alex',65],['Matturi',76],['Douguls',72]]
    df = pd.DataFrame(a, columns = ['Name_1' , 'age_1'])
    print(df)
    return HttpResponse('create_pd_df_from_list_of_lists')

def create_pd_df_from_dict_of_lists(request):
    a ={'Name':['Alex','Matturi','Douguls'],'Age':[65,76,89]}
    df = pd.DataFrame(a)
    print(df)
    return HttpResponse('create_pd_df_from_dict_of_lists')

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
   student = Student.objects.create(first_name=first_name,last_name=last_name, address=address, pincode=pincode )
   return HttpResponse('Student is created')

@api_view(['PUT'])
def update_student(request, id):
   data = request.data
   first_name = data['first_name']
   last_name = data['last_name']
   address = data['address']
   pincode = data['pincode']
   student = Student.objects.filter(id=id).update(first_name=first_name, last_name = last_name, address = address, pincode = pincode)
   return HttpResponse('Student is updated successfully')

@api_view(['DELETE'])
def delete_student(request,id):
    student = Student.objects.filter(id=id).delete()
    return HttpResponse('Student is deleted successfully')

@api_view(['GET'])
def get_all_students(request):
    students = Student.objects.all()
    print(students)
    return HttpResponse('All students got returned from Database')

@api_view(['POST'])
def create_employee(request):
   emp = Employee.objects.create(empname='Shivam', empId= 10000123)
   return HttpResponse('Employee is created')

def no_of_students_in_class(request):
    students = Student.objects.all()
    print(students)
    serializer = StudentSerializer(students, many=True)
    return JsonResponse(serializer.data,safe=False)

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


