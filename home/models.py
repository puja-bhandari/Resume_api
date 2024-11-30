from django.db import models

state_choice=((('India','India'), ('Nepal','Nepal'), ('America','America')))

class resumeHome(models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField(max_length=100)
    dob= models.DateField(auto_now=False)
    state= models.CharField(choices=state_choice, max_length=50)
    gender= models.CharField(max_length=50)
    location= models.CharField(max_length=50)
    image= models.ImageField(upload_to="image", blank=False)
    rdoc= models.FileField(upload_to="rdoc",blank=False)

    def __str__(self):
        return self.name