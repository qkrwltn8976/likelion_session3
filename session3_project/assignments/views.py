from django.shortcuts import render, redirect, get_object_or_404
from .models import Assignment


def list(request):
    assignments = Assignment.objects.all()
    return render(request, 'assignments/list.html', {'assignments': assignments})


def add(request):
    if request.method == "POST":
        id = request.POST.get('id')
        name = request.POST.get('name')
        course = request.POST.get('course')
        submission_date = request.POST.get('submission_date')
        content = request.POST.get('content')
        finish = 0
        assignment = Assignment(id=id, name=name, course=course, submission_date=submission_date, content=content, finish=finish)
        assignment.save()
        return redirect('list')
    return render(request, 'assignments/add.html')


def detail(request, id):
    item = get_object_or_404(Assignment, pk=id)
    return render(request, 'assignments/detail.html', {'item': item})


def edit(request, id):
    item = get_object_or_404(Assignment, pk=id)
    if request.method == "POST":
        #item = get_object_or_404(Assignment, pk=item_id)
        item.name = request.POST.get('name')
        item.course = request.POST.get('course')
        item.submission_date = request.POST.get('submission_date')
        print("++++++"+str(item.submission_date))
        item.content = request.POST.get('content')
        item.save()
        return redirect('detail', item.id)
    return render(request, 'assignments/edit.html', {'item': item})


def delete(request, id):
    item = get_object_or_404(Assignment, pk=id)
    item.delete()
    return redirect('list')


