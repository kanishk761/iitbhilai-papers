from django.shortcuts import render
from .models import paperModel
from django.http import HttpResponseRedirect
from .forms import addPaper
from .models import courseModel
# Create your views here.
def paperUploadShow(request):
    if request.method == 'POST':
        form = addPaper(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = addPaper()
    else:
        form = addPaper(None)
    return render(request, 'imageUpload.html', {'addPaperForm' : form})

def filterPaper(request):
    if request.method == 'POST':
        get_program = request.POST['program']
        get_courseType = request.POST['course_type']
        get_dept = request.POST['department']
        if get_dept == 'none':
            a = courseModel.objects.filter(program=get_program).filter(course_type=get_courseType)
        else:
            a = courseModel.objects.filter(program=get_program).filter(course_type=get_courseType).filter(department=get_dept)
        if len(a) == 0:
            return render(request, 'filterpaper2.html', {'coursequery' : a, 'empty' : True})
        return render(request, 'filterpaper2.html', {'coursequery' : a, 'empty' : False})
    total_prog = courseModel.objects.values('program').distinct()
    total_course_type = courseModel.objects.values('course_type').distinct()
    total_dept = courseModel.objects.values('department').distinct()
    return render(request, 'filterpaper1.html', {'programs' : total_prog, 'courseTypes' : total_course_type, 'departments' : total_dept})

def showPapers(request, code = 'None'):
    if code == 'None':
        get_coursename = request.POST['coursename']
        coursequery = courseModel.objects.get(course_name=get_coursename)
        code = coursequery.course_code
        return HttpResponseRedirect('/showPapers/'+code+'/')
    paperquery = paperModel.objects.filter(course_code=code)
    if len(paperquery) == 0:
        return render(request, 'showpapers.html', {'paperquery' : paperquery, 'empty' : True})
    return render(request, 'showpapers.html', {'paperquery' : paperquery, 'empty' : False})
