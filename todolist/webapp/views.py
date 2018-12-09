from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import List
from datetime import datetime


def index_view(request):
    lists = List.objects.all()
    return render(request, 'index.html', context={
        'lists': lists
    })


def create_view(request):
    list = List.objects.create(
        name=request.POST.get('name'),
        due_date=request.POST.get('due_date')
    )
    return redirect('index')

def update_view(request, list_pk):
    list = get_object_or_404(List, pk=list_pk)

    if request.method == 'GET':
        return render(request, 'update.html', context={
            'list': list
        })

    elif request.method == 'POST':
        name = request.POST.get('name')
        status = request.POST.get('status')
        list.name = name
        list.status = status
        list.save()
        return redirect('index')


def delete_view(request, list_pk):
    list = get_object_or_404(List, pk=list_pk)

    if request.method == 'GET':
        return render(request, 'delete.html', context={
            'list': list
        })
    elif request.method == 'POST':
        if request.POST.get('delete') == 'yes':
            list.delete()
        return redirect('index')

def delete_done_view(request):
    list = List.objects.filter(status = 'done')

    if request.method == 'GET':
        return render(request, 'delete_done.html', context={
            'list': list
        })
    elif request.method == 'POST':
        if request.POST.get('delete') == 'yes':
            list.delete()
        return redirect('index')
