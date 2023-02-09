from django.test import TestCase
import unittest
import requests
import json
# Create your tests here.

#Librarian Registration
class TestLibrarian(unittest.TestCase):
    def test_Liblogin1(self):

        res = requests.post('http://127.0.0.1:8000/api/login/',
                         {
    
    "email" : "lib1@gmail.com",
    "password" : "1245"
} 
                            )

        content = json.loads(res.content)
        print(content)
        
        
        
    
    
    
    
    
    
    
    def test_Liblogin(self):

        res = requests.post('http://127.0.0.1:8000/api/login/',{

            "email": "lib1@gmail.com",

            "password": "12345"

        })

        content = json.loads(res.content)

        print(content)

        assert "jwt" in content
        
        
    

        

            
        

    def test_register(self):
        t=requests.post('http://127.0.0.1:8000/api/reg/',
                        
                        
                        {
    "name" : "Lib5",
    "email" : "lib5@gmail.com",
    "password" : "12345"
}
                        
                        )
        content = json.loads(t.content)

        print(content)

        self.assertEqual(content["email"], ["librarian with this email already exists."])
        

 

        