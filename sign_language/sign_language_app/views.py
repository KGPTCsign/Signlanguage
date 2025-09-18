from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View

from sign_language_app.models import *

# Create your views here.
class admin_dash(View):
    def get(self,request):
        return render(request,'administration/admindash.html')
class Login_View(View):
    def get(self,request):
        return render(request,'administration/login.html')
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            obj = LoginTable.objects.get(username = username,password = password)
            request.session['user_id'] = obj.id
            if obj.usertype == 'admin':
                return HttpResponse('''<script>alert('Login successful');window.location='/admin_dash '</script>''')  
            elif obj.user_type == 'teacher':
                return HttpResponse('''<script>alert('Login successful');window.location='/teacherhome/ '</script>''')
            elif obj.user_type == 'student':
              return HttpResponse('''<script>alert('Login successful');window.location='/'</script>''')  
        except LoginTable.DoesNotExist:
            return HttpResponse('''<script>alert('Invalid username or password');window.location='/'</script>''')
       
 
class View_Complaints(View):
    def get(self,request):
        e=ComplaintTable.objects.all()
        return render(request,'administration/view_Complaints.html',{'user':e})
class send_replay(View):
    def post(self,request,id):
        complaint =ComplaintTable.objects.get(id=id)
        reply_text = request.POST.get('replay')
        complaint.reply = reply_text
        complaint.save()
        return HttpResponse('''<script>alert('Invalid username or password');window.location='/complaints'</script>''')
       
   
        
    
class View_Feedback(View):
    def get(self,request):
        d=FeedbackTable.objects.all()
        return render(request,'administration/view_feedback.html',{'user':d})

    
class View_User(View):
    def get(self,request):
        c=UserTable.objects.all()
        return render(request,'administration/view_user.html',{'user':c})
    
class Send_Complaints(View):
    def get(self,request):
        return render(request,'User/send_complaint.html')

class Send_Feedback(View):
    def get(self,request):
        return render(request,'User/send_feedback.html')
    
class User_Registration(View):
    def get(self,request):
        return render(request,'User/user registration.html')
    
class Approve_user(View):
    def get(self,request,login_id):
        obj=LoginTable.objects.get(id=login_id)

        print(obj,'???????????')
        obj.usertype = "user"
        obj.save()
        return HttpResponse('''<script>alert("Successfully Approved");window.location="/admin_dash";</script>''')
class Reject_user(View):
    def get(self,request,login_id):
        obj=LoginTable.objects.get(id=login_id)
        obj.usertype = "rejected"
        obj.save()
        return HttpResponse('''<script>alert("Successfully Rejected");window.location="/admin_dash";</script>''')