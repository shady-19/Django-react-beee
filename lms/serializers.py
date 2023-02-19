from rest_framework import serializers
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


from rest_framework.views import APIView,Response
from rest_framework.exceptions import AuthenticationFailed
import re
import requests
from .models import librarian
from .models import users
from .models import books
from .models import booksd



# #Librarian
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = librarian
        fields = ['id','name','email','password',]
        extra_kwargs = {
            'password' : {'write_only': True}
        }
        
        
    def create(self, validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance      


#User
class RegUserSerializer(serializers.ModelSerializer):
    upassword = serializers.CharField(write_only=True)
    class Meta:
        model = users
        fields = ['uid','uname','uemail','upassword',]      
        
        
    def create(self, validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance     

# #books



class RegBookSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = books
        fields = ['bid','bname','author','subject','about',]      
        
        
    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance  
    
#Issued Books   
class IssueBookSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = booksd
        fields = ['bid' , 'id' , 'uid','oid', 'issued' , 'expiry']      
        
        
    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance  
        
    








    
    

