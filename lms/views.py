from django.shortcuts import render


import json
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from .serializers import UserSerializer
from .serializers import RegUserSerializer
from .serializers import RegBookSerializer
from .serializers import IssueBookSerializer
import jwt, datetime
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from rest_framework.filters import SearchFilter
from django.http import HttpResponse
import requests

#Tables
from .models import librarian
from .models import users
from .models import books
from .models import booksd




# # Create your views here.

# #Librarian Registration  
class RegisterView(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data) 
      
#Librarian Login 
 
class LoginView(APIView):
    def post(self,request):
        email = request.data['email']
        password = request.data['password']

        user=librarian.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        
        payload={
            'id': user.id,
            'exp':datetime.datetime.utcnow() +datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        
        token= jwt.encode(payload,'secret',algorithm='HS256')   
        
        response = Response()  

        response.set_cookie('jwt',token)  
        
        response.data={
            'jwt': token,
            'email': email , 

        } 
        return response

 
        
#Librarian Logged in Details
class LibView(APIView):
    
    def get(self, request):
        token = request.headers['Authorization']

        if not token:
            raise AuthenticationFailed()

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        
        except jwt.ExpiredSignatureError :
            raise AuthenticationFailed('Unauthenticated User')
        
        user=librarian.objects.filter().first()
        
        user=librarian.objects.filter(id=payload['id']).first()
        serializer =UserSerializer(user)
        return Response(serializer.data)

#Lib by Id

class LibListView(APIView):
    def get(self,request,id=None):
     if id:
      try:
        queryset = librarian.objects.get(id=id)
      except librarian.DoesNotExist:
        return Response({'errors': 'This Librarian does not exist.'}, status=400)

      read_serializer = UserSerializer(queryset)

     else:
      queryset = librarian.objects.all()

      read_serializer =UserSerializer(queryset, many=True)

     return Response(read_serializer.data)
   
#Librarian Logout    
class LogoutView(APIView):
    def post(self,request):
         response=Response()
         response.delete_cookie('jwt')
         response.data={
             'message':'succcess'
         }    
         return response



#Add Book
class BookRegisterView(APIView):
    def post(self,request):
        

        serializer = RegBookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)  
    
#Delete Book
class BookDeleteView(APIView):
    def delete(self,request,bid=None):
        

        try:
            item = books.objects.get(bid=bid)
        except books.DoesNotExist:
            return Response({'errors': 'This todo item does not exist.'}, status=400)

        item.delete()
        

        return Response('Success')
    
#Get Books by Id        
class BookListView(APIView):
    def get(self,request,bid=None):
     if id:
      try:
        queryset = books.objects.get(bid=bid)
      except books.DoesNotExist:
        return Response({'errors': 'This Book item does not exist.'}, status=400)

      read_serializer = RegBookSerializer(queryset)

     else:
      queryset = books.objects.all()

      read_serializer = RegBookSerializer(queryset, many=True)

     return Response(read_serializer.data)
 
#get All books

class AllBooksView(APIView):
    def get(self,request,bid=None):
      queryset = books.objects.all()

      read_serializer = RegBookSerializer(queryset, many=True)

      return Response(read_serializer.data)
  
  
class AllUserView(APIView):
    def get(self,request,bid=None):
      queryset = users.objects.all()

      read_serializer = RegUserSerializer(queryset, many=True)

      return Response(read_serializer.data)  


#Reg User        
class UserRegisterView(APIView):
    def post(self,request):
        

        serializer = RegUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)   

#Login User


class UserLoginView(APIView):
    def post(self,request):
        email = request.data['uemail']
        password = request.data['upassword']

        user=users.objects.filter(uemail=email).first()
        print(user.upassword)
        if user is None:
            raise AuthenticationFailed('User not found!')

        if user.upassword != password:
            raise AuthenticationFailed('incoorect password')
     
        queryset=users.objects.get(uemail=email)
        read_serializer = RegUserSerializer(queryset)
    
        return Response(read_serializer.data)
        

#Delete User
class UserDeleteView(APIView):
    def delete(self,request,uid=None):
        
        try:
            item = users.objects.get(uid=uid)
        except users.DoesNotExist:
            return Response({'errors': 'This todo item does not exist.'}, status=400)

        item.delete()
        

        return Response('Success')
    
 


class StudentListView(ListAPIView):
    queryset=books.objects.all()
    serializer_class = RegBookSerializer
    filter_backends= [SearchFilter]
    search_fields=['^bname' , 'bid' , 'author','subject',] 
    
    
    
class IssueBookView(APIView):
    def post(self,request):
        

        serializer = IssueBookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)      
            
class IssueBookListView(APIView):
    def get(self,request,bid=None):
      queryset = booksd.objects.all()

   

      read_serializer = IssueBookSerializer(queryset, many=True)

      return Response(read_serializer.data)
  

class BookUpdateView(APIView): 
    def put(self, request, bid=None):
        try:
            item=books.objects.get(bid=bid)
        except books.DoesNotExist:
            return Response({'errors' : 'Books does not exist'},status=400)    
        update_serializer =RegBookSerializer(item,data=request.data)
        
        
        if update_serializer.is_valid():
            item_object =update_serializer.save()
            
            read_serializer = RegBookSerializer(item_object)
            
            return Response(read_serializer.data,status=200)
        
        return Response(update_serializer.errors,status=400)
        
      

  
  
class BookReturnView(APIView):
    def delete(self,request,oid=None):
        
       
        try:
            item = booksd.objects.get(oid=oid)
        except booksd.DoesNotExist:
            return Response({'errors': 'This todo item does not exist.'}, status=400)

        item.delete()
        

        return Response('Success')  
           
        

       
       
    
           
    
    
    
     


 























    
   
        
    
        
    
