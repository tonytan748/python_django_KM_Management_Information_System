import datetime
import json
import xlwt
import StringIO

from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.db.models import Q

from models import Subcon
from forms import SubconForm

@login_required
def subcon_list(request):
	if request.method=='POST':
		print request.POST.get('item_id') ,'------'
		sid=request.POST.get('item_id')
		if sid:
			try:
				item_update=Subcon.objects.get(id=int(sid))
				item_update.code=item_update.code
				item_update.name=request.POST.get('name').upper()
				item_update.tel=request.POST.get('tel')
				item_update.fax=request.POST.get('fax')
				item_update.contact=request.POST.get('contact').upper()
				item_update.address=request.POST.get('address').upper()
				item_update.scope_of_work=request.POST.get('scope_of_work').upper()
				item_update.gst_verification=request.POST.get('gst_verification')
				item_update.gst_reg_no=request.POST.get('gst_reg_no').upper()
				item_update.remark=request.POST.get('remark').upper()
				item_update.edit_by=str(request.user).upper()
				item_update.edit_date=str(datetime.datetime.now()).upper()
				item_update.save()
				print "saved... ..."
				status='edit success'
			except Exception as e:
				status='please try again.'
				print str(e)
			item=Subcon.objects.all()
			form=SubconForm()
			return HttpResponseRedirect('../subcon',{'object_list':item,'status':status,'form':form})
	print "title..."
	item=Subcon.objects.all()
	form=SubconForm()
	return render(request,'sub_contractor/subcon_list.html',{'object_list':item,'form':form})

@login_required
def add_item(request):
	if request.method=='POST':
		form=SubconForm(request.POST)
		if form.is_valid():
			item=form.save(commit=False)
			print item
			if Subcon.objects.all():
				ma=str((max(int(i.code[-3:]) for i in Subcon.objects.all()))+1001)[1:]
				print ma
			else:
				ma='001'
			item.code=str(item.code).upper()+ma
			item.name=str(item.name).upper()
			item.contact=str(item.contact).upper()
			item.address=str(item.address).upper()
			print "code:%s,name:%s,contact:%s,address:%s,gst_verification:%s" % (item.code,item.name,item.contact,item.address,item.gst_verification)
			if item.gst_verification is False:
				item.gst_reg_no=""
			item.reamrk=(item.remark).upper()
			item.create_by=str(request.user).upper()
			item.create_date=str(datetime.datetime.now())
			item.edit_by=''
			item.edit_date=''
			item.save()
			return HttpResponseRedirect('/subcon',{'status':'this item add already'})
	else:
		form=SubconForm()
	return render(request,'sub_contractor/subcon_list.html',{'form':form,'object_list':Subcon.objects.all()})

@login_required
def del_item(request,pk):
	if pk:
		item=Subcon.objects.get(pk=pk)
		item.delete()
		return HttpResponseRedirect('/subcon',{'status':'Delete success!'})
	else:
		item=Subcon.objects.all()
		form=SubconForm()
		return render(request,'sub_contractor/subcon_list.html',{'object_list':item,'status':'please try again!','form':form})

@login_required
def search_item(request):
	if request.method=='POST':
		word=request.POST.get('search_name')
		print word
		if word=="":
			return HttpResponseRedirect('/subcon',{'status':'nothing to find.','object_list':Subcon.objects.all(),'form':SubconForm()})
		else:
			word=str(word).upper()
			result=Subcon.objects.filter(Q(name__icontains=word)|Q(code__icontains=word)|Q(contact__icontains=word)|Q(address__icontains=word)|Q(scopr_of_work__icontains=word))
		if result:
			return render(request,'sub_contractor/subcon_list.html',{'object_list':result,'status':'search success.','form':SubconForm()})
		return HttpResponseRedirect('/subcon',{'status':'nothing to find.','object_list':Subcon.objects.all(),'form':SubcomForm()})
	return HttpResponseRedirect('/subcon',{'status':'Nothing.'})

@login_required
def export_item_list(request):
	wb=xlwt.Workbook(encoding="utf-8")
	sheet=wb.add_sheet('SUB CON LIST')
	sheet.write(0,0,'CODE')
	sheet.write(0,1,'NAME')
	sheet.write(0,2,'TEL')
	sheet.write(0,3,'FAX')
	sheet.write(0,4,'CONTACT')
	sheet.write(0,5,'ADDRESS')
	sheet.write(0,6,'SCOPE_OF_WORK')
	sheet.write(0,7,'GST_VERIFICATION')
	sheet.write(0,8,'GST_REG_NO')
	sheet.write(0,9,'REMARK')
	sheet.write(0,10,'CREATE BY')
	sheet.write(0,11,'CREAE DATE')
	sheet.write(0,12,'EDIT BY')
	sheet.write(0,13,'EDIT DATE')

	row=1
	for item in Subcon.objects.all():
		sheet.write(row,0,item.code)
		sheet.write(row,1,item.name)
		sheet.write(row,2,item.tel)
		sheet.write(row,3,item.fax)
		sheet.write(row,4,item.contact)
		sheet.write(row,5,item.address)
		sheet.write(row,6,item.scope_of_work)
		sheet.write(row,7,item.gst_verification)
		sheet.write(row,8,item.gst_reg_no)
		sheet.write(row,9,item.remark)
		sheet.write(row,10,item.create_by)
		sheet.write(row,11,"")
		sheet.write(row,12,item.edit_by)
		sheet.write(row,13,"")
		row=row+1
#	response = HttpResponse(mimetype='application/vnd.ms-excel')
	response = HttpResponse(content_type='application/vnd.ms-excel')
	response['Content-Disposition']="attachment;filename=SUBCON_LIST.xls"
	output=StringIO.StringIO()
	wb.save(output)
	output.seek(0)
	response.write(output.getvalue())
	return response
		
