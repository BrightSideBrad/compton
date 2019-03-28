from django.shortcuts import render, HttpResponse, redirect
import bcrypt
from .models import User
from .models import Race
import re
from django.contrib import messages
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


# Create your views here.


def loginReg(request):
    return render(request, "races/loginReg.html")

def login(request):
    if request.method == 'GET':
        return redirect('/')
    if request.method == 'POST':
        errors = []
        if (len(request.POST['logemail']) < 1):
           errors.append("Email ***")
        if (len(request.POST['LPassW']) < 1):
            errors.append("Password ***")

    if not errors:
        
        if User.objects.get(email = request.POST['logemail']):
            user = User.objects.get(email = request.POST['logemail'])
            print(user)
            if bcrypt.checkpw(request.POST['LPassW'].encode(), user.password.encode()):
                print("password match")
                request.session['userId'] = user.id
                seshId = request.session['userId']
                request.session['userName'] = user.first_name
                seshName = request.session['userName']
                print(seshId)
                print(request.session['userName'])
                return redirect('/dashboard')
        else:
            errors = []
            errors.append("Incorrect username or password")
            for er in errors:
                messages.error(request, er)

            return redirect('/')

    else:
        #for er in errors:
        #    errors(request, er)
        print(errors)
        for er in errors:
            messages.error(request, er)

        return redirect('/')


def registration(request):
    if request.method == 'POST':
        

        errors = []
        if (len(request.POST['first_name']) < 1):
           errors.append("First Name ***")
        if (len(request.POST['last_name']) < 1):
            errors.append("Last Name ***")
        if (len(request.POST['email']) < 1):
            errors.append("Email ***")
        if (len(request.POST['password']) < 1):
            errors.append("Password ***")
        if (request.POST['password'] != request.POST['conpw']):
            errors.append("You fat fingered your password confirmation...")

        if not errors:
            hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            newUser = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = hashed)
            request.session['userId'] = newUser.id
            print(request.session['userId'])
            request.session['userName'] = newUser.first_name
            

        else:
            #for er in errors:
            #    errors(request, er)
            print(errors)
            for er in errors:
                messages.error(request, er)

            return redirect('/')
        
        return redirect('/dashboard')






def dashboard(request):

    context = {
        "assignments": Race.objects.exclude(workers__id=request.session["userId"]),
        "personal": Race.objects.filter(workers__id=request.session["userId"])
    }
    return render(request, "races/Dashboard.html", context)

def canwork(request, race_id):
    selectedRace = Race.objects.get(id= race_id)
    selectedUser = User.objects.get(id= request.session['userId'])
    print(selectedRace)
    print(selectedUser.first_name)
    selectedUser.events.add(selectedRace)
    return redirect('/dashboard')

def cantwork(request, race_id):
    selectedRace = Race.objects.get(id= race_id)
    selectedUser = User.objects.get(id= request.session['userId'])
    print(selectedRace)
    print(selectedUser.first_name)
    selectedUser.events.remove(selectedRace)
    return redirect('/dashboard')

def assignments(request):
    all_races = Race.objects.all()
    context = {
        "assignments": Race.objects.all().order_by("date")
    }
    return render(request, "races/assignments.html", context)

def add(request):
    return render(request, "races/add.html")

def addrace(request):
    if request.method == 'POST':
        newRace = Race.objects.create(name = request.POST['rName'], city = request.POST['rCity'], state = request.POST['rState'], date = request.POST['rDate'])
        print(newRace)
    return redirect('/assignments')

def edit(request, race_id):
    rId = race_id
    print(rId)
    context = {
        "edits" : Race.objects.get(id=race_id)
    }
    if request.method == 'GET':
        return render(request, "races/edit.html", context)
    if request.method == 'POST':
        c = Race.objects.get(id=rId)
        c.name = request.POST['rName']
        c.date = request.POST['rDate']
        c.city = request.POST['rCity']
        c.state = request.POST['rState']
        c.save()
        return redirect('/assignments')



def signout(request):
    request.session.clear()
    return redirect('/')


def delete(request, race_id):
    rId = race_id
    print(rId)
    if request.method == 'GET':
        c = Race.objects.get(id=rId)
        c.delete()
    return redirect('/assignments')