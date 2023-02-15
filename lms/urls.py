from django.urls import path

from . import views

urlpatterns = [
  path('reg/', views.RegisterView.as_view()),
  path('login/',views.LoginView.as_view()),
  
  path('librarian/',views.LibView.as_view()),
  path('libid/<int:id>', views.LibListView.as_view()),
  
  
  path('logout/',views.LogoutView.as_view()),
#   #user
  path('ureg/', views.UserRegisterView.as_view()),
  
  
  
  path('ulogin/', views.UserLoginView.as_view()),
  
  
  path('udel/<int:uid>', views.UserDeleteView.as_view()),
  
#   # path('users/<int:uid>/', views.UserView.as_view()),
  
#   # Books
  path('breg/', views.BookRegisterView.as_view()),
  
  path('books/<int:bid>',views.BookDeleteView.as_view()),
  path('getbooks/<int:bid>',views.BookListView.as_view()),
  path('getallbooks/',views.AllBooksView.as_view()),
  path('getallusers/',views.AllUserView.as_view()),
  
  path('search/',views.StudentListView.as_view()),
  path('issue/',views.IssueBookView.as_view()),
  path('issuedbooks/',views.IssueBookListView.as_view()),
  path('returnbook/<int:oid>',views.BookReturnView.as_view()),
 
  
  # path('issue/<int:bid_id>',views.IssueBookByidView.as_view()),
  
  
  
  
  
  
 
]