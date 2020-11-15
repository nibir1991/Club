from django import forms
from .models import member

class RegForm(forms.ModelForm):
    class Meta:
        model=member
        fields=('name','category','position','description','address','photo','fees')

        widgets={

            'name':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.TextInput(attrs={'class':'form-control'}),
            'position':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'address':forms.Textarea(attrs={'class':'form-control'}),
            'photo':forms.FileInput(attrs={'class':'form-control'}),
            

        }