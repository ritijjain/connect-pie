from django.shortcuts import render
from .models import University, uClass, Note, URL
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import Create_uClass, Create_Note, Create_URL
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Q

def home(request):
    return redirect('/uni')

def about(request):
    return render(request, 'main/about.html', {'title': 'About'})

def toc(request):
    return render(request, 'main/toc.html', {'title': 'TOC'})

def uni_list(request):
    uni_list = University.objects.all()[:20]

    if 'search' in request.GET:
        search_term = request.GET['search']
        uni_list = University.objects.all().filter(name__icontains=search_term)[:20]

    context = {'uni_list': uni_list, 'title': 'Uni Page'}
    return render(request, 'main/uni_list.html', context)

def class_list(request, shortname):
    class_list = uClass.objects.all().filter(uni__shortname=shortname)[:20]
    uni = University.objects.get(shortname=shortname)

    if 'search' in request.GET:
        search_term = request.GET['search']
        class_list = uClass.objects.all().filter(Q(uni__shortname=shortname), Q(class_code__icontains=search_term) | Q(description__icontains=search_term))[:20]
    
    context = {'class_list': class_list, 'uni': uni, 'title': uni.name}
    return render(request, 'main/class_list.html', context)

def note_list(request, shortname, uclass_id):
    uclass = uClass.objects.get(uclass_id=uclass_id)
    note_list = Note.objects.all().filter(uClass__uclass_id=uclass_id)[:20]
    url_list = URL.objects.all().filter(uClass__uclass_id=uclass_id)[:20]
    uni = University.objects.get(shortname=shortname)

    if 'search' in request.GET:
        search_term = request.GET['search']
        note_list = Note.objects.all().filter(uClass__uclass_id=uclass_id, content__icontains=search_term)[:20]
        url_list = URL.objects.all().filter(uClass__uclass_id=uclass_id, description__icontains=search_term)[:20]
    
    context = {'note_list': note_list, 'uni': uni, 'uclass': uclass, 'url_list': url_list, 'title':uclass.class_code}
    return render(request, 'main/note_list.html', context)

def add_class(request):
    next_page = request.GET['next']
    sp = next_page.split('/')
    sp = University.objects.get(shortname=sp[2])

    if request.method == 'POST':
        form = Create_uClass(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Class added successfully')
            next_page = request.GET['next']
            return redirect(next_page)
    else:
        form = Create_uClass(initial={'uni':sp})

    context = {'form': form, 'title': 'Add Class'}
    return render(request, 'main/form.html', context)

def add_note(request):
    next_page = request.GET['next']
    sp = next_page.split('/')
    sp = uClass.objects.get(uclass_id=sp[3])
    

    if request.method == 'POST':
        form = Create_Note(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Class added successfully')
            return redirect(next_page)

    else:
        form = Create_Note(initial={'uClass':sp})

    context = {'form': form, 'title': 'Add Note'}
    return render(request, 'main/form.html', context)

def add_url(request):
    next_page = request.GET['next']
    sp = next_page.split('/')
    sp = uClass.objects.get(uclass_id=sp[3])

    if request.method == 'POST':
        form = Create_URL(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Class added successfully')
            next_page = request.GET['next']
            return redirect(next_page)

    else:
        form = Create_URL(initial={'uClass':sp})

    context = {'form': form, 'title': 'Add URL'}
    return render(request, 'main/form.html', context)