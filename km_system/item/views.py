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

from models import Kinds,Item
from forms import KindsForm,ItemForm
from supplier.models import Supplier

@login_required
def ItemListView(request):
	if request.method=='POST':
		print request.POST.get('item_id') ,'------'
		sid=request.POST.get('item_id')
		if sid:
			try:
				item_update=Item.objects.get(id=int(sid))
				item_update.code=item_update.code
				item_update.name=request.POST.get('name').upper()
				item_update.supplier=Supplier.objects.get(name=request.POST.get('supplier'))
				
				item_update.category=Kinds.objects.get(sub_category=(request.POST.get('category')).split('-')[1])
				item_update.large_uom=request.POST.get('large_uom').upper()
				item_update.large_qty=request.POST.get('large_qty').upper()
				item_update.large_price=request.POST.get('large_price').upper()
				item_update.med_uom=request.POST.get('med_uom').upper()
				item_update.med_qty=request.POST.get('med_qty').upper()
				item_update.med_price=request.POST.get('med_price').upper()
				item_update.sml_uom=request.POST.get('sml_uom').upper()
				item_update.sml_qty=request.POST.get('sml_qty').upper()
				item_update.sml_price=request.POST.get('sml_price').upper()
				item_update.remark=request.POST.get('remark').upper()
				item_update.edit_by=str(request.user).upper()
				item_update.edit_date=str(datetime.datetime.now()).upper()
				item_update.save()
				print "saved... ..."
				status='edit success'
			except Exception as e:
				status='please try again.'
				print str(e)
			item=Item.objects.all()
			supplier_list=Supplier.objects.all()
			return HttpResponseRedirect('../item',{'object_list':item,'status':status,'suppliers':supplier_list})
#			return render(request,'item/item_list.html',{'object_list':item,'status':status,'suppliers':supplier_list})
	print "title..."
	item=Item.objects.all()
	suppliers=Supplier.objects.all()
	return render(request,'item/item_list.html',{'object_list':item,'suppliers':suppliers})

@login_required
def add_item(request):
	if request.method=='POST':
		form=ItemForm(request.POST)
		if form.is_valid():
			item=form.save(commit=False)
			print item
			ma=str((max((int(i.code) for i in Item.objects.all()))+1)+100000)[1:]
			item.code=ma
			item.name=(item.name).upper()
			item.supplier=item.supplier
			item.category=item.category
			item.large_uom=(item.large_uom).upper()
			if item.large_qty is None:
				item.large_qty=0
			item.large_qty=item.large_qty
			if item.large_price is None:
				item.large_price=0.00 
			item.large_price=item.large_price
			item.med_uom=(item.med_uom).upper()
			if item.med_qty is None:
				item.med_qty=0
			item.med_qty=(item.med_qty)
			if item.med_price is None:
				item.med_price=0.00
			item.med_price=(item.med_price)
			item.sml_uom=(item.sml_uom).upper()
			item.sml_qty=item.sml_qty
			item.sml_price=(item.sml_price)
			item.reamrk=(item.remark).upper()
			item.create_by=str(request.user).upper()
			item.create_date=str(datetime.datetime.now())
			item.edit_by=''
			item.edit_date=''
			item.save()
			return HttpResponseRedirect('/item',{'status':'this item add already'})
	else:
		form=ItemForm()
	return render(request,'item/item_add.html',{'form':form})

@login_required
def del_item(request,pk):
	if pk:
		item=Item.objects.get(pk=pk)
		item.delete()
		return HttpResponseRedirect('/item',{'status':'Delete success!'})
	else:
		item=Item.objects.all()
		return render(request,'item/item_list.html',{'object_list':item,'status':'please try again!'})

@login_required
def search_item(request):
	if request.method=='POST':
		word=request.POST.get('search_name')
		code=request.POST.get('search_code')
		supplier=request.POST.get('search_supplier')
		print word
		print code
		print supplier
		if word=="" and code=="" and supplier=="":
			return HttpResponseRedirect('/item',{'status':'nothing to find.','object_list':Item.objects.all()})
		if word:
			word=str(word).upper()
			result=Item.objects.filter(Q(name__icontains=word)|Q(large_uom__icontains=word)|Q(med_uom__icontains=word)|Q(sml_uom__icontains=word))
		if code:
			code=int(code)
			result=Item.objects.filter(Q(code__icontains=code))
		if supplier is None:
			supplier=None
			result=Item.objects.filter(Q(supplier__icontains=supplier))
		if result:
			return render(request,'item/item_list.html',{'object_list':result,'status':'search success.'})
		return HttpResponseRedirect('/item',{'status':'nothing to find.','object_list':Item.objects.all()})
	return HttpResponseRedirect('/item',{'status':'Nothing.'})

@login_required
def export_item_list(request):
	wb=xlwt.Workbook(encoding="utf-8")
	sheet=wb.add_sheet('ITEMS')
	sheet.write(0,0,'CODE')
	sheet.write(0,1,'NAME')
	sheet.write(0,2,'SUPPLIER')
	sheet.write(0,3,'CATEGORY')
	sheet.write(0,4,'LARGE UOM')
	sheet.write(0,5,'LARGE QTY')
	sheet.write(0,6,'LARGE PRICE')
	sheet.write(0,7,'MED UOM')
	sheet.write(0,8,'MED QTY')
	sheet.write(0,9,'MED PRICE')
	sheet.write(0,10,'SML UOM')
	sheet.write(0,11,'SML QTY')
	sheet.write(0,12,'SML PRICE')
	sheet.write(0,13,'REMARK')
	sheet.write(0,14,'CREATE BY')
	sheet.write(0,15,'CREAE DATE')
	sheet.write(0,16,'EDIT BY')
	sheet.write(0,17,'EDIT DATE')

	row=1
	for item in Item.objects.all():
		sheet.write(row,0,item.code)
		sheet.write(row,1,item.name)
		sheet.write(row,2,(Supplier.objects.get(name=item.supplier)).name)
#		sheet.write(row,3,(Kinds.objects.get(item.category)).)
		sheet.write(row,3,"")
		sheet.write(row,4,item.large_uom)
		sheet.write(row,5,item.large_qty)
		sheet.write(row,6,item.large_price)
		sheet.write(row,7,item.med_uom)
		sheet.write(row,8,item.med_qty)
		sheet.write(row,9,item.med_price)
		sheet.write(row,10,item.sml_uom)
		sheet.write(row,11,item.sml_qty)
		sheet.write(row,12,item.sml_price)
		sheet.write(row,13,item.remark)
		sheet.write(row,14,item.create_by)
		sheet.write(row,15,"")
		sheet.write(row,16,item.edit_by)
		sheet.write(row,17,"")
		row=row+1
#	response = HttpResponse(mimetype='application/vnd.ms-excel')
	response = HttpResponse(content_type='application/vnd.ms-excel')
	response['Content-Disposition']="attachment;filename=ITEM_LIST.xls"
	output=StringIO.StringIO()
	wb.save(output)
	output.seek(0)
	response.write(output.getvalue())
	return response
		
@login_required
def kinds_list(request):
	if request.method=='POST':
		if request.POST.get('kinds_id'):
			sid=request.POST.get('kinds_id')
			try:
				kinds=Item.objects.get(id=int(sid))
				kinds.main_category=str(request.POST.get('main_category')).upper()
				kinds.sub_category=str(request.POST.get('sub_category')).upper()
				kinds.edit_by=str(request.user).upper()
				kinds.edit_date=str(datetime.datetime.now()).upper()
				kinds.save()
				print "saved... ..."
				status='edit success'
			except Exception as e:
				status='please try again.'
				print str(e)
			kinds_list=Kinds.objects.all()
			form=KindsForm()
			return render(request,'item/kinds_list.html',{'object_list':kinds_list,'status':status,'form':form})
	print "title..."
	kinds_list=Kinds.objects.all()
	form=KindsForm()
	return render(request,'item/kinds_list.html',{'object_list':kinds_list,'form':form})

@login_required
def kinds_add(request):
	if request.method=='POST':
		if request.POST.get('main_category') and request.POST.get('sub_category'):
			form=KindsForm(request.POST)
			form_item=form.save(commit=False)
			form.main_category=(form_item.main_category).upper()
			form.sub_category=(form_item.sub_category).upper()
			print form.sub_category
			form.create_by=str(request.user).upper()
			form.create_date=str(datetime.datetime.now())
			form.save()
			status="add success!"
		else:
			status="please try again!"
		form=KindsForm()
		return HttpResponseRedirect('/item/kinds',{'object_list':Kinds.objects.all(),'form':form,'status':status})
	else:
		form=KindsForm()	
	return HttpResponseRedirect('/item/kinds',{'object_list':Kinds.objects.all(),'form':form})

@login_required
def kinds_delete(request,pk):
	if pk:
		print pk
		try:
			item=Kinds.objects.get(pk=pk)
			item.delete()
		except Exception as e:
			print str(e)
		form=KindsForm()
		return HttpResponseRedirect('/item/kinds',{'object_list':Kinds.objects.all(),'form':form})



