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
# import jwt,datetime
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

 
        
#Librarian View
class LibView(APIView):
    
    def get(self, request):
        token = request.headers['Authorization']
        # token = request.COOKIES.get('jwt')

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
      # If an id is provided in the GET request, retrieve the Todo item by that id
      try:
        # Check if the todo item the user wants to update exists
        queryset = librarian.objects.get(id=id)
      except librarian.DoesNotExist:
        # If the todo item does not exist, return an error response
        return Response({'errors': 'This Librarian does not exist.'}, status=400)

      # Serialize todo item from Django queryset object to JSON formatted data
      read_serializer = UserSerializer(queryset)

     else:
      # Get all todo items from the database using Django's model ORM
      queryset = librarian.objects.all()

      # Serialize list of todos item from Django queryset object to JSON formatted data
      read_serializer =UserSerializer(queryset, many=True)

    # Return a HTTP response object with the list of todo items as JSON
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
        # token = request.headers['Authorization']
        
        # # token = request.COOKIES.get('jwt')

        # if not token:
        #     raise AuthenticationFailed('Unauthenticated User')

        # try:
        #     payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        
        # except jwt.ExpiredSignatureError :
        #     raise AuthenticationFailed('Unauthenticated User')

        serializer = RegBookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)  
    
#Delete Book
class BookDeleteView(APIView):
    def delete(self,request,bid=None):
        # token = request.COOKIES.get('jwt')

        # if not token:
        #     raise AuthenticationFailed('Unauthenticated User')

        # try:
        #     payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        
        # except jwt.ExpiredSignatureError :
        #     raise AuthenticationFailed('Unauthenticated User')

        try:
      # Check if the todo item the user wants to update exists
            item = books.objects.get(bid=bid)
        except books.DoesNotExist:
      # If the todo item does not exist, return an error response
            return Response({'errors': 'This todo item does not exist.'}, status=400)

    # Delete the chosen todo item from the database
        item.delete()
        

    # Return a HTTP response notifying that the todo item was successfully deleted
        return Response('Success')
    
#Get Books by Id        
class BookListView(APIView):
    def get(self,request,bid=None):
     if id:
      # If an id is provided in the GET request, retrieve the Todo item by that id
      try:
        # Check if the todo item the user wants to update exists
        queryset = books.objects.get(bid=bid)
      except books.DoesNotExist:
        # If the todo item does not exist, return an error response
        return Response({'errors': 'This Book item does not exist.'}, status=400)

      # Serialize todo item from Django queryset object to JSON formatted data
      read_serializer = RegBookSerializer(queryset)

     else:
      # Get all todo items from the database using Django's model ORM
      queryset = books.objects.all()

      # Serialize list of todos item from Django queryset object to JSON formatted data
      read_serializer = RegBookSerializer(queryset, many=True)

    # Return a HTTP response object with the list of todo items as JSON
     return Response(read_serializer.data)
 
#get All books

class AllBooksView(APIView):
    def get(self,request,bid=None):
      queryset = books.objects.all()

      # Serialize list of todos item from Django queryset object to JSON formatted data
      read_serializer = RegBookSerializer(queryset, many=True)

    # Return a HTTP response object with the list of todo items as JSON
      return Response(read_serializer.data)
  
  
class AllUserView(APIView):
    def get(self,request,bid=None):
      queryset = users.objects.all()

      # Serialize list of todos item from Django queryset object to JSON formatted data
      read_serializer = RegUserSerializer(queryset, many=True)

    # Return a HTTP response object with the list of todo items as JSON
      return Response(read_serializer.data)  


#Reg User        
class UserRegisterView(APIView):
    def post(self,request):
        # token = request.COOKIES.get('jwt')

        # if not token:
        #     raise AuthenticationFailed('Unauthenticated User')

        # try:
        #     payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        
        # except jwt.ExpiredSignatureError :
        #     raise AuthenticationFailed('Unauthenticated User')

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
        
        # token = request.COOKIES.get('jwt')

        # if not token:
        #     raise AuthenticationFailed('Unauthenticated User')

        # try:
        #     payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        
        # except jwt.ExpiredSignatureError :
        #     raise AuthenticationFailed('Unauthenticated User')

        try:
      # Check if the todo item the user wants to update exists
            item = users.objects.get(uid=uid)
        except users.DoesNotExist:
      # If the todo item does not exist, return an error response
            return Response({'errors': 'This todo item does not exist.'}, status=400)

    # Delete the chosen todo item from the database
        item.delete()
        

    # Return a HTTP response notifying that the todo item was successfully deleted
        return Response('Success')
    
 
 
# def store_data(id,uid,bid):

#     user_data = booksd(id=id,uid=uid,bid=bid)

#     user_data.save()

#     return 1


class StudentListView(ListAPIView):
    queryset=books.objects.all()
    serializer_class = RegBookSerializer
    filter_backends= [SearchFilter]
    search_fields=['^bname' , 'bid' , 'author','subject',] 
    
    
    
class IssueBookView(APIView):
    def post(self,request):
        # token = request.COOKIES.get('jwt')

        # if not token:
        #     raise AuthenticationFailed('Unauthenticated User')

        # try:
        #     payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        
        # except jwt.ExpiredSignatureError :
        #     raise AuthenticationFailed('Unauthenticated User')

        serializer = IssueBookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)      
            
class IssueBookListView(APIView):
    def get(self,request,bid=None):
      queryset = booksd.objects.all()

    #   # Serialize list of todos item from Django queryset object to JSON formatted data
    #   read_serializer = RegUserSerializer(queryset, many=True)
      

      # Serialize list of todos item from Django queryset object to JSON formatted data
      read_serializer = IssueBookSerializer(queryset, many=True)

    # Return a HTTP response object with the list of todo items as JSON
      return Response(read_serializer.data)
  
  
class BookReturnView(APIView):
    def delete(self,request,oid=None):
        
        # token = request.COOKIES.get('jwt')

        # if not token:
        #     raise AuthenticationFailed('Unauthenticated User')

        # try:
        #     payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        
        # except jwt.ExpiredSignatureError :
        #     raise AuthenticationFailed('Unauthenticated User')

        try:
      # Check if the todo item the user wants to update exists
            item = booksd.objects.get(oid=oid)
        except booksd.DoesNotExist:
      # If the todo item does not exist, return an error response
            return Response({'errors': 'This todo item does not exist.'}, status=400)

    # Delete the chosen todo item from the database
        item.delete()
        

    # Return a HTTP response notifying that the todo item was successfully deleted
        return Response('Success')  
           
        

       
       
    
           
    
    
    
     


 























    
   
        
    
        
    
