from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from models import UserContent,UserLog

@login_required
def index(request):
	user=request.user
	print user
	contents=UserContent.objects.filter(user=user)
	print contents
	for i in contents:
		print i.url,i.content
	all_content=UserContent.objects.all()
	if request.method=="POST":
		id=request.POST.get('id')
		rights=request.POST.getlist('rights')
		usercontent=UserContent.objects.get(id=id)
		usercontent.rights=','.join(rights)
		usercontent.save()
		logtext="Change user {0} right to: {1}".format(user,usercontent.right)
		log=UserLog.objects.update_or_create(user=user,log=logtext)
	return render(request,'home/index.html',{'contents':contents,'all_content':all_content})

@login_required
def delete_content(request,id):
	user=request.session.get('user')
	if user.is_superuser:
		if request.method=='POST':
			content=UserContent.objects.get(id=id)
			content.delete()
			logtext="Delete user {0} right".format(user)
			log=UserLog.objects.update_or_create(user=user,log=logtext)
	return index(request)
		