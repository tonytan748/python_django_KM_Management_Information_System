import datetime
import json

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
			return render(request,'item/item_list.html',{'object_list':item,'status':status})
	print "title..."
	item=Item.objects.all()
	return render(request,'item/item_list.html',{'object_list':item})

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
		word=request.POST.get('search')
		print word
		word=str(word).upper()
		if word.strip():
			result=Item.objects.filter(Q(code__icontains=word)|Q(name__icontains=word)|Q(supplier__icontains=word)|Q(large_uom__icontains=word)|Q(med_uom__icontains=word)|Q(sml_uom__icontains=word))
			if result:
				return render(request,'item/item_list.html',{'object_list':result,'status':'search success.'})
			return HttpResponseRedirect('/item',{'object_list':Item.objects.all(),'status':'Cannot find it, please try again'})
		return HttpResponseRedirect('/item',{'status':'nothing to find.'})
	return HttpResponseRedirect('/item',{'status':'Nothing.'})


