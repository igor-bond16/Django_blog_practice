#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 11:19:21 2020

@author: igor
"""

from django import forms
from .models import Friend,Message 

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name','mail','gender','age','birthday']
        
class FindForm(forms.Form):
    find = forms.CharField(label='Find',required=False)
    
class CheckForm(forms.Form):
    str = forms.CharField(label='Message')
    
    def clean(self):
        cleaned_data = super().clean()
        str = cleaned_data['str']
        if(str.lower().startswith('no')):
            raise forms.ValidationError('You input NO')
            
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['title','content','friend']            
            
            
            
   