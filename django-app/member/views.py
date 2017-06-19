from django.shortcuts import render, redirect

from member.models import Student


def student_list(request):
    students = Student.objects.all()
    context = {
        'students123': students
    }
    return render(request, 'member/member.html', context)


def student_del(request, s_pk):
    student = Student.objects.get(pk=s_pk)
    if request.method == 'POST':
        student.delete()
        return redirect('member/member.html')
