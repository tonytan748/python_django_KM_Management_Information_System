from django import forms

from models import Kinds,Item

class KindsForm(forms.ModelForm):
	class Meta:
		model=Kinds
		exclude=['create_by','create_date','edit_by','edit_date']

class ItemForm(forms.ModelForm):
	name=forms.CharField(widget=forms.Textarea(attrs={'rows':2,'cols':30}))
	remark=forms.CharField(widget=forms.Textarea(attrs={'rows':2,'cols':30}))
	class  Meta:
		model=Item
		exclude=['code','create_by','create_date','edit_by','edit_date']

