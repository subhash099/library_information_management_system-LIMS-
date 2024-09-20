from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404

from LIMS_app.forms import ReaderForm
from .models import *
from django.urls import reverse


def home(request):
    return render(request,"home.html",context={"current_tab":"home"})
def readers(request):
    return render(request,"readers.html",context={"current_tab":"readers"})
def readers_tab(request):
    readers=Reader.objects.all()
    if request.method=="GET":
        return render(request,"readers.html",context={"current_tab":"readers","readers":readers})
    else:
        query=request.POST['query']
        readers=Reader.objects.raw("select * from LIMS_app_reader where reader_name like '%"+query+"%'")
        return render(request,"readers.html",context={"current_tab":"readers","readers":readers})

def readers_info(request,id):
    readers=Reader.objects.get(pk=id)
    return HttpResponseRedirect(reverse('readers'))


def add(request):
    if request.method=="POST":
        form=ReaderForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'add.html',{
                'success':True
            })
    else:

        return render(request,'add.html')

def books(request):
    books=Book.objects.all()
    if request.method=="GET":
        return render(request,"books.html",context={"current_tab":"books","books":books})
    else:
        query=request.POST['query']
        books=books.objects.raw("select * from LIMS_app_book where books_name like '%"+query+"%'")
        return render(request,"books.html",context={"current_tab":"books","books":books,"query":query})
    
def delete_reader(request,id):
    if request.method=="POST":
        readers=Reader.objects.get(pk=id)
        readers.delete()
        return HttpResponseRedirect("/readers")
    


def edit(request,id):
    readers=get_object_or_404(Reader,pk=id)
    if request.method=="POST":
        readers=Reader.objects.get(pk=id)
        form=ReaderForm(request.POST,instance=readers)
        
        if form.is_valid():
            form.save()
            return render (request,'edit.html',{
                'form':form,
                'success':True
            })
    else:
        readers=Reader.objects.get(pk=id)
        form=ReaderForm(instance=readers)
    return render(request,'edit.html',{
        'form':form
    })  

