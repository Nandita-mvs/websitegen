from django.db.models import fields
from django.forms import ModelForm
from .models import Member
from django import forms
from crispy_forms.layout import Layout, Submit, Row, Column
from crispy_forms.helper import FormHelper

class MemberForm(ModelForm):
    class Meta:
        model=Member
        fields=['firstname',
    'lastname',
    'aboutme',
    'phoneno',
    'emailid',
    'profession',
    'location',
    'linkedinlink',
    'twitterlink',
    'instagramlink',
    'behancelink',
    'githublink',
    'skillstext',
    'skill1',
    'skill1p',
    'skill2',
    'skill2p',
    'skill3',
    'skill3p',
    'skill4',
    'skill4p',
    'project1',
    'work1',
    'project2',
    'work2',
    'project3',
    'work3',
    'project4',
    'work4',
    'project5',
    'work5',
    'project6',
    'work6',
    'photo',
    'resume']
    

