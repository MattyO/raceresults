from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf

from common.helpers import resolve_http_method
from common.forms import UserRegistrationForm, RaceForm
from common.models import Race

def index(request):
    return render(request, "index.html")

@login_required
def user_profile(request):
    #org = Org.objects.get(owner=request.user)
    c={"current_user":request.user}
    return render(request, "accounts/profile.html", c)



def races(request):
    #c = { 'org': Org.objects.get(owner=request.user) }
    c = {}

    def get():
        c = {'races': Race.objects.all()}

        #c.update({'race_form': RaceForm()})
        return render(request, 'races/index.html', c)

    def post():
        race_form = RaceForm(request.POST)
        c = {'race_form':race_form }

        if race_form.is_valid():
            race_form.save()
            return redirect("user_profile")
        else:
            print 'race results is not valid'

        return render(request, 'races/new.html', c)

    return resolve_http_method(request, [get, post])

def single_race(request, id):
    def get():
        c = {'race': Race.objects.get(pk=id) }
        return render(request, 'races/single.html', c)

    return resolve_http_method(request, [get])

def register(request):
    new_user_form = UserRegistrationForm()
    c = { "registration_form": new_user_form }
    c.update(csrf(request))

    def get():
        return render(request, 'registration/register.html', c)

    def post():
        new_user_form = UserRegistrationForm(request.POST)
        c.update({ "registration_form": new_user_form })
        if new_user_form.is_valid():
            new_user_form.save()
            return redirect("login")
        return render(request, 'registration/register.html', c)

    return resolve_http_method(request, [get, post])
