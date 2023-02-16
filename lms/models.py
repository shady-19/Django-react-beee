from django.db import models,models
from django.db import models
from datetime import datetime , timedelta
from django.contrib.auth.models import AbstractUser 


# Create your models here.
class librarian(AbstractUser):
    id = models.AutoField(
    primary_key=True
  )
    name= models.CharField(max_length=255)   
    email= models.CharField(max_length=255,unique=True)
    password= models.CharField(max_length=1255)
    username=None
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    
    class  Meta:
        db_table = 'librarian'
        
        
class users(models.Model):
    uid = models.AutoField(
    primary_key=True
  )
    uname= models.CharField(max_length=255)   
    uemail= models.CharField(max_length=255,unique=True)
    upassword= models.CharField(max_length=255)    
    
    class  Meta:
        db_table = 'users'  
          


class books(models.Model):
    bid = models.AutoField(
    primary_key=True
  )
    #on Access Number, Title, Author, Subject, Keyword
    bname= models.CharField(max_length=255,unique=True)   
    author= models.CharField(max_length=255)
    # title= models.CharField(max_length=255)
    subject= models.CharField(max_length=255)
    about= models.CharField(max_length=1255)
    
    class  Meta:
        db_table = 'books'   
        
        
        
class booksd(models.Model):
    oid = models.AutoField(
    primary_key=True
  )
   
    #on Access Number, Title, Author, Subject, Keyword
    
    issued=models.DateTimeField(default=datetime.now().date(), blank=True)
    expiry = models.DateTimeField(default= datetime.now() + timedelta(days=30))
    
    uid=models.ForeignKey(users, on_delete=models.CASCADE)
    bid=models.ForeignKey(books, on_delete=models.CASCADE)
    id=models.ForeignKey(librarian ,  on_delete=models.CASCADE)
    
    
    
    class  Meta:
        db_table = 'booksd'
        
        
        
        
        
            
