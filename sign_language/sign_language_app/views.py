from django.shortcuts import render
from django.views import View

# Create your views here.
class Login_View(View):
    def get(self,request):
        return render(request,'admin/login.html')
    
class Send_replay(View):
    def get(self,request):
        return render(request,'admin/send replay.html')
    
class View_Complaints(View):
    def get(self,request):
        return render(request,'admin/view complaints.html')
    
class View_Feedback(View):
    def get(self,request):
        return render(request,'admin/view feedback.html')
    
class View_User(View):
    def get(self,request):
        return render(request,'admin/view user.html')
    
class Send_Complaints(View):
    def get(self,request):
        return render(request,'User/send_complaint.html')

class Send_Feedback(View):
    def get(self,request):
        return render(request,'User/send_feedback.html')
    
class User_Registration(View):
    def get(self,request):
        return render(request,'User/user registration.html')