from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from sign_language_app.forms import *
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
        phoneNo = request.POST.get('phoneNo')
        try:
            obj = LoginTable.objects.get(username=username,password=password)
            request.session['user_id'] = obj.id
            if obj.usertype == 'admin':
                return HttpResponse('''<script>alert('Login successful');window.location='/admin_dash '</script>''')  
            elif obj.usertype == 'user':
              return HttpResponse('''<script>alert('Login successful');window.location='/userdash'</script>''')  
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
        return HttpResponse('''<script>alert('replyed succesfully');window.location='/complaints'</script>''')
       
   
        
    
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
        c=ComplaintTable.objects.filter(userid__loginid_id=request.session['user_id'])
        return render(request,'User/send_complaint.html',{'user':c})
    
class Send_Comp(View):
    def get(self,request):
        # c=ComplaintTable.objects.filter(userid__loginid_id=request.session['user_id'])
        return render(request,'User/send_comp.html')
    def post(self,request):
        complaint=request.POST['complaint']
        obj=ComplaintTable()
        obj.complaint=complaint
        print(request.session['user_id'])
        obj.userid=UserTable.objects.get(loginid_id=request.session['user_id'])
        obj.reply='Pending'
        obj.save()
        return redirect('user_complaints')

class Send_Feedback(View):
    def get(self,request):
        c=FeedbackTable.objects.filter(userid__loginid_id=request.session['user_id'])
        return render(request,'User/send_feedback.html',{'user':c})
    
class Send_feed(View):
    def get(self,request):
         return render(request,'User/send_feed.html')
    def post(self,request):
        feedback=request.POST['feedback']
        obj=FeedbackTable()
        obj.feedback=feedback
        print(request.session['user_id'])
        obj.userid=UserTable.objects.get(loginid_id=request.session['user_id'])
        obj.reply='Pending'
        obj.save()
        return redirect('user_feedback')


class User_Registration(View):
    def get(self,request):
        return render(request,'User/user registration.html')
    def post(self,request):
        c=UserForm(request.POST)
        if c.is_valid():
            reg=c.save(commit=False)
            user=LoginTable.objects.create(username=reg.email, password=request.POST['password'], usertype='pending')
            reg.loginid=user
            reg.save()
        return HttpResponse('''<script>alert('Registered succesfully');window.location='/'</script>''')

    
class Approve_user(View):
    def get(self,request,login_id):
        obj=LoginTable.objects.get(id=login_id)

        print(obj,'???????????')
        obj.usertype = "user"
        obj.save()
        return HttpResponse('''<script>alert("Successfully Approved");window.location="/view_user";</script>''')
class Reject_user(View):
    def get(self,request,login_id):
        obj=LoginTable.objects.get(id=login_id)
        obj.usertype = "rejected"
        obj.save()
        return HttpResponse('''<script>alert("Successfully Rejected");window.location="/view_user";</script>''')
class UserDash(View):
    def get(self,request):
        return render(request,'User/userdash.html')