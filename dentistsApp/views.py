from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import User
from .models import Dentist
from dentistsApp.forms import UserForm, DentistForm, MatchForm
import logging, logging.config
import sys

def index(request):
    users_list = User.objects.all()
    dentist_list = Dentist.objects.all()
    context = {'users_list': users_list, 'dentists_list': dentist_list}
    return render(request, 'dentistsApp/index.html', context)

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid(): # All validation rules pass
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            selected_dentist = form.cleaned_data['dentist']
            post = User.objects.create(first_name=first_name, last_name=last_name, email=email, dentist=selected_dentist)
            return HttpResponseRedirect('/') # Redirect after POST
    else:
        form = UserForm() # Unbound form
    return render(request, 'dentistsApp/add_user.html'
        , {
            'form': form,
        }
    )

def create_dentist(request):
        if request.method == 'POST':
            form = DentistForm(request.POST)
            if form.is_valid(): # All validation rules pass
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                email = form.cleaned_data['email']
                license_number = form.cleaned_data['license_number']
                post = Dentist.objects.create(first_name=first_name, last_name=last_name, email=email, license_number=license_number)
                return HttpResponseRedirect('/') # Redirect after POST
        else:
            form = DentistForm() # Un unbound form
        return render(request, 'dentistsApp/add_dentist.html'
            , {
                'form': form,
            }
        )

def user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'dentistsApp/user.html', {'user': user})

def dentist(request, dentist_id):
    dentist = get_object_or_404(Dentist, pk=dentist_id)
    return render(request, 'dentistsApp/dentist.html', {'dentist': dentist})

def patients(request, dentist_id):
    dentist = Dentist.objects.get(id=dentist_id)
    users_list = User.objects.filter(dentist = dentist)
    context = {'users_list': users_list, 'dentist': dentist}
    return render(request, 'dentistsApp/patients.html', context)

def match(request):
    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid(): # All validation rules pass
            user = form.cleaned_data['user']
            dentist = form.cleaned_data['dentist']
            return HttpResponseRedirect('/match/user/' + str(user.id) + '/dentist/' + str(dentist.id))
    else:
        form = MatchForm() # Unbound form
    return render(request, 'dentistsApp/match.html'
        , {
            'form': form,
        }
    )

def match_result(request, user_id, dentist_id):
    user = get_object_or_404(User, pk=user_id)
    dentist = get_object_or_404(Dentist, pk=dentist_id)
    context = {'user': user, 'dentist': dentist}
    if request.method == 'POST':
        user.dentist = dentist
        user.save()
        return HttpResponseRedirect('/user/' + str(user.id))
    return render(request, 'dentistsApp/match_result.html', context)
