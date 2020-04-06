from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.http import JsonResponse
# from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView
from myapp import forms
from myapp.models import FireRecords


class FireRecordListView(ListView):
    """
    This is simple class to list all records on results page
    """
    model = FireRecords
    template_name = 'record_list.html'
    context_object_name = 'records'

class FireRecordDetail(DetailView):
    """
    This is simple class to view deatils of specific record
    """
    model = FireRecords
    template_name = 'record_detail.html'
    context_object_name = 'record'

class FireRecordDelete(DeleteView):
    """
    This is simple class for delete existing record from our database
    """
    model = FireRecords
    context_object_name = 'record'
    template_name = 'record_delete.html'
    success_url = reverse_lazy('list')

def recieve_data_from_rpi(request):
    message, status_code = "Somthing went wrong", 400
    if request.method == "POST":
        data = request.data
        status = data.get('status')
        FireRecords.objects.create(Alarm_status=status)
        message, status_code = "Data created", 201
    return JsonResponse(
        {'message': message}, status=status_code)

def home_page_view(request):
    """
    A simple method to display home page
    """
    return render(request, "home_page.html")

def about_page_view(request):
    """
    A simple method to display about page
    """
    return render(request, "about.html")

# def SignUP(request):
#     """
#     Here I used built in Regestration module
#     """
#     form = forms.RegisterForm()
#     if request.method == 'POST':
#         form = forms.RegisterForm(data=request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.set_password(user.password)
#             user.save()
#             return HttpResponseRedirect('/signin')
#         else:
#             messages.error(request, form.errors)
#     return render(request,'registeration.html',{'form':form})

# def sign_out(request):
#     """
#     Django built in logout function
#     """
#     logout(request)
#     return HttpResponseRedirect('/')

# def Sign_in(request):
#     """
#     Django built in login method using authenticate
#     """
#     if request.method == "POST":
#         name = request.POST['un']
#         pswd = request.POST['pwd']
#         user = authenticate(username=name, password=pswd)
#         if user:
#             if user.is_active:
#                 login(request,user)
#                 return HttpResponseRedirect('/')
#         else:
#             messages.error(request, 'Please enter valid keyword ')
#             return render(request,'login.html')
#     return render(request,'login.html')
