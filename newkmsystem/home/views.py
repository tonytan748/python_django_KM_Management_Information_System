from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from models import UserContent

@login_required
def index(request):
	user=request.session.get('user')
	contents=UserContent.objects.filter(user=user)
	all_content=UserContent.objects.all()
	if request.method=="POST":
		id=request.POST.get('id')
		rights=request.POST.getlist('rights')
		usercontent=UserContent.objects.get(id=id)
		usercontent.rights=','.join(rights)
		usercontent.save()
		return 
	return render(request,'home/index.html',{'contents':contents,'all_content':all_content})
