from django.db import models
from django.db.models import CharField
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=100,verbose_name="First Name",default='')
    lastname = models.CharField(max_length=100,verbose_name="Last Name",default='') 

    aboutme = models.CharField(max_length=10000,verbose_name="Few lines about yourself",default='')
    phoneno = models.IntegerField(default=0)
    emailid = models.EmailField(max_length=100,verbose_name="Email Id",default='')
    profession=models.CharField(max_length=100,default='')
    location=models.CharField(max_length=100,default='')
    resume=models.CharField(max_length=5000,default='')

    linkedinlink=models.CharField(max_length=2000,verbose_name="Linkedin URL",default='')
    twitterlink=models.CharField(max_length=2000,verbose_name="Twitter URL",default='')
    instagramlink=models.CharField(max_length=2000,verbose_name="Instagram URL",default='')
    behancelink=models.CharField(max_length=2000,verbose_name="Behance URL",default='')
    githublink=models.CharField(max_length=2000,verbose_name="Github URL",default='')

    skillstext = models.CharField(max_length=10000,verbose_name="Few lines about your skillset",default='')

    skill1=models.CharField(max_length=100,default='')
    skill1p=models.IntegerField(verbose_name="Skill 1 percentage",default=1)

    skill2=models.CharField(max_length=100,default='')
    skill2p=models.IntegerField(verbose_name="Skill 2 percentage",default=1)

    skill3=models.CharField(max_length=100,default='')
    skill3p=models.IntegerField(verbose_name="Skill 3 percentage",default=1)

    skill4=models.CharField(max_length=100,default='')
    skill4p=models.IntegerField(verbose_name="Skill 4 percentage",default=1)   

    project1=models.CharField(max_length=100,verbose_name="Project 1 name",default='')
    work1=models.CharField(max_length=100,verbose_name="Project 1 URL",default='')

    project2=models.CharField(max_length=100,verbose_name="Project 2 name",default='')
    work2=models.CharField(max_length=100,verbose_name="Project 2 URL",default='')

    project3=models.CharField(max_length=100,verbose_name="Project 3 name",default='')
    work3=models.CharField(max_length=100,verbose_name="Project 3 URL",default='')

    project4=models.CharField(max_length=100,verbose_name="Project 4 name",default='')
    work4=models.CharField(max_length=100,verbose_name="Project 4 URL",default='')

    project5=models.CharField(max_length=100,verbose_name="Project 5 name",default='')
    work5=models.CharField(max_length=100,verbose_name="Project 5 URL",default='')

    project6=models.CharField(max_length=100,verbose_name="Project 6 name",default='')
    work6=models.CharField(max_length=100,verbose_name="Project 6 URL",default='')
    
    photo=models.ImageField(upload_to='images',default="images/perfil.png",null=True,blank=True)    
    def __str__(self):
        return self.firstname