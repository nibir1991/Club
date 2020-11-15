from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import member
from django.views.generic import CreateView,DetailView,UpdatetView
from .forms import RegForm
from django.urls import reverse_lazy,reverse  
# Create your views here.

def home(request):
    members=member.objects.all()
    n=len(members)
    return render(request,'index.html',{'members':members})


class register(CreateView):
    model = member 
    form_class=RegForm
    template_name= 'registration.html' 
    success_url= reverse_lazy('home')


class ShowProfile(DetailView):
    model = member
    template_name='profile.html'
    def get_context_data(self,*args,**kwargs):
        player=member.objects.all ()
        context = super (ShowProfile, self).get_context_data(*args,**kwargs)
        context ['player']=player
        return context

class EditProfile(UpdatetView):
    pass



     
     
