from django import forms

from models import Supplier

class SupplierForm(forms.ModelForm):
	address=forms.CharField(widget=forms.Textarea(attrs={'rows':2,'cols':20}))
	remark=forms.CharField(widget=forms.Textarea(attrs={'rows':2,'cols':20}))
	class Meta:
		model=Supplier
#		fields=('code','name','address','product','contact','phone','fax','remark')
		exclude=['create_by','create_date','edit_by','edit_date']
