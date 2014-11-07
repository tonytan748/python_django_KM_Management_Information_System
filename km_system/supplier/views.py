import datetime
import json

from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.db.models import Q

from models import Supplier
from forms import SupplierForm

@login_required
def SupplierListView(request):
	if request.method=='POST':
		print request.POST.get('supplier_id')
		sid=request.POST.get('supplier_id')
		if sid:
			try:
				supplier_update=Supplier.objects.get(id=int(sid))
				supplier_update.code=request.POST.get('code').upper()
				supplier_update.name=request.POST.get('name').upper()
				supplier_update.address=request.POST.get('address').upper()
				supplier_update.product=request.POST.get('product').upper()
				supplier_update.contact=request.POST.get('contact').upper()
				supplier_update.phone=request.POST.get('phone').upper()
				supplier_update.fax=request.POST.get('fax').upper()
				supplier_update.remark=request.POST.get('remark').upper()
				supplier_update.edit_by=str(request.user).upper()
				supplier_update.edit_date=str(datetime.datetime.now()).upper()
				supplier_update.save()
				print "saved... ..."
				status='edit success'
			except Exception as e:
				status='please try again.'
				print str(e)
			supplier=Supplier.objects.all()
			return render(request,'supplier/supplier_list.html',{'object_list':supplier,'status':status})
	print "title..."
	supplier=Supplier.objects.all()
	return render(request,'supplier/supplier_list.html',{'object_list':supplier})

@login_required
def add_supplier(request):
	if request.method=='POST':
		form=SupplierForm(request.POST)
		if form.is_valid():
			item=form.save(commit=False)
			print item
			ma=str(max((int(i.code[-3:]) for i in Supplier.objects.all()))+1)
			item.code=str(item.code).upper() + ' ' + ma
			item.name=(item.name).upper()
			item.address=(item.address).upper()
			item.product=(item.product).upper()
			item.contact=(item.contact).upper()
			item.phone=(item.phone).upper()
			item.fax=(item.fax).upper()
			item.reamrk=(item.remark).upper()
			item.create_by=str(request.user).upper()
			item.create_date=str(datetime.datetime.now())
			item.edit_by=''
			item.edit_date=''
			item.save()
			return HttpResponseRedirect('/supplier',{'status':'this item add already'})
	else:
		form=SupplierForm()
	return render(request,'supplier/supplier_add.html',{'form':form})

@login_required
def del_supplier(request,pk):
	if pk:
		item=Supplier.objects.get(pk=pk)
		item.delete()
		return HttpResponseRedirect('/supplier',{'status':'Delete success!'})
	else:
		supplier=Supplier.objects.all()
		return render(request,'supplier/supplier_list.html',{'object_list':supplier,'status':'please try again!'})

@login_required
def search_supplier(request):
	if request.method=='POST':
		word=request.POST.get('search')
		print word
		word=str(word).upper()
		if word.strip():
			result=Supplier.objects.filter(Q(code__icontains=word)|Q(name__icontains=word)|Q(address__icontains=word)|Q(product__icontains=word)|Q(contact__icontains=word)|Q(create_by__icontains=word)|Q(edit_by__icontains=word))
			if result:
				return render(request,'supplier/supplier_list.html',{'object_list':result,'status':'search success.'})
			return HttpResponseRedirect('/supplier',{'object_list':Supplier.objects.all(),'status':'Cannot find it, please try again'})
		return HttpResponseRedirect('/supplier',{'status':'nothing to find.'})
	return HttpResponseRedirect('/supplier',{'status':'Nothing.'})


