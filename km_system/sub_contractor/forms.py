from django import forms

from models import Subcon

class SubconForm(forms.ModelForm):
	address=forms.CharField(widget=forms.Textarea(attrs={'rows':2,'cols':30}))
	remark=forms.CharField(widget=forms.Textarea(attrs={'rows':2,'cols':30}))
	class  Meta:
		model=Subcon
		exclude=['create_by','create_date','edit_by','edit_date']

