from django.http import Http404
from django.shortcuts import render

from .models import Teacher, TeacherImage


# Create your views here.

def main_view(request):
    context = {}
    template = 'main/index.html'

    return render(request, template, context)


def information_view(request):
    context = {}
    template = 'Information.html'

    return render(request, template, context)


def teachers_view(request):
    teacher = Teacher.objects.all()
    template = 'Teachers.html'
    context = {"teachers": teacher}

    return render(request, template, context)


def single(request, id):
    try:
        teachers = Teacher.objects.get(id=id)

        images = TeacherImage.objects.filter(teacher=teachers)

        context = {"teachers": teachers, "images": images}
        template = 'Profile.html'

        return render(request, template, context)

    except Teacher.DoesNotExist:
        raise Http404
    except TeacherImage.DoesNotExist:
        raise Http404
