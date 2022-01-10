from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from students.models import StudentInfo
from teachers.models import TeacherInfo

@login_required
def index(request):
    context = {
        "teachers_count": TeacherInfo.objects.all().count(),
        "students_count" : StudentInfo.objects.all().count()
    }
    # return render(request, "home.html")
    return render(request, "home.html", context)


