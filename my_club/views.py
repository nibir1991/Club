from django.shortcuts import render, get_object_or_404
from .models import member
from django.views.generic import ListView, DetailView,CreateView
from .forms import RegForm
from django.urls import reverse_lazy,reverse 
from django.http import HttpResponseRedirect

def home(request):
    members=member.objects.all
    return render(request, 'index.html',{'members':members})


class ShowProfile(DetailView):
    model=member
    template_name='profile.html'
    def get_context_data(self,*args,**kwargs):
        profile=member.objects.all ()
        context = super (ShowProfile, self).get_context_data(*args,**kwargs)
        context ['profile']=profile
        return context



class Register(CreateView):
    model = member 
    form_class=RegForm
    template_name= 'registration.html'        
