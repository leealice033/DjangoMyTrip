from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.

def adduser(request):
	try:
		user = User.objects.get(username = "test") #以user取得名稱為"test"的資料
	except:
		user = None # 若[test]不存在 則將資料設定為None

	if user != None:
		message = user.username + " 帳號已經建立！ "
		return HttpResponse(message)
	else: #帳號不存在，建立新帳號
		user = User.objects.create_user("test", "test@test.com.tw", "aa000000") #(name, email, pw)
		user.first_name = "AliceTest"
		user.last_name = "Lee"
		user.is_staff = True
		user.save()
		return redirect('/admin/') #if 建立帳號成功，重新導向至admin頁面

def login(request):
	if request.method == 'POST':  #如果是 <login.html> 按登入鈕傳送
		name = request.POST['username'] 
		password = request.POST['password'] #取得表單傳送的帳號、密碼
		user = auth.authenticate(username = name, password = password) #使用者驗證
		if user is not None:
			if user.is_active:
				auth.login(request,user)
				return redirect('/index/') #log in successfully 
			else:
				message = '帳號尚未啓用！'
		else:
			message = '登入失敗！'
	return render(request, "login.html", locals()) #登入失敗則重新導入login 頁面

def logout(request):
	auth.logout(request)  #登出成功清除 Session，重導到<index.html>
	return redirect('/index/')

def index(request):
	return render(request, 'index.html')

