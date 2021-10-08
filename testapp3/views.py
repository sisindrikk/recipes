from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Recipes,User,MyUser
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy


def home(request):
    recipe=Recipes.objects.all()
    return render(request, 'testapp3/home.html', context={'recipe': recipe})


@login_required
def details(request, recipe_id):
    recipe = Recipes.objects.get(id=recipe_id)
    return render(request, 'testapp3/details.html', context={'recipe': recipe})


@login_required
def create(request):
    return render(request, 'testapp3/create.html')

@login_required
def data(request):
    if request.method == "POST" and request.FILES:
        Recipes.objects.create(
            food_item=request.POST["food_item"],
            ingredients=request.POST["ingredients"],
            food_process=request.POST["food_process"],
            recipe_Img=request.FILES["recipe_Img"],

        )
        return HttpResponseRedirect('/testapp3/recipe_list/')
    return render(request, 'testapp3/create.html')



@login_required
def recipe_list(request):
    recipe = Recipes.objects.all()
    return render(request, 'testapp3/list.html',{'recipe': recipe})


def registration(request):
    if request.method == "POST":
        user=User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password'],
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
        )
        user.save()
        return redirect('/testapp3/login/')
    return render(request,'testapp3/registartion.html')


def user_login(request):
    if request.method =='POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('testapp3:home'))
        else:
            return redirect('registration')
    return render(request, 'testapp3/login.html')




def custom_registartion(request):

    if request.method == 'POST':
        #import pdb
        #pdb.set_trace()
        #user=MyUser.objects.create_user(
            email=request.POST['email'],
            password=request.POST['password'],
            date_of_birth =request.POST['date_of_birth'],
            f_name=request.POST['f_name'],
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],


        #user.save()
            return redirect('/testapp3/custom_login/')
    return render(request, 'testapp3/custom_registration.html')


def custom_login(request):
    if request.method =='POST':
        #import pdb
        #pdb.set_trace()
        email= request.POST['email']
        password = request.POST['password']
        date_of_birth = request.POST['date_of_birth']
        user = authenticate(request, email=email, password=password, date_of_birth=date_of_birth)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('testapp3:home'))
        else:
            return redirect('custom_registartion')
    return render(request, 'testapp3/custom_login.html')


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('testapp3:home'))




