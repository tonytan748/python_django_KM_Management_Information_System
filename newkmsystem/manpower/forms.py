from django import forms
from models import ManPower,Employee,Project,Salary,Shift
from django.contrib.admin import widgets

SHIFT_CHOICES=(('abc','def'),('ghi','gkl'))

class ManPowerForm(forms.ModelForm):
	employee=forms.ModelChoiceField(queryset=Employee.objects.all())
	project=forms.ModelChoiceField(queryset=Project.objects.all())
	time_in=forms.DateTimeField(widget=widgets.AdminSplitDateTime())
	time_out=forms.DateTimeField(widget=widgets.AdminSplitDateTime())
	lunch=forms.IntegerField(initial=1)
	shift=forms.ModelChoiceField(queryset=Shift.objects.all(),initial={'name':'D1'})

	class Meta:
		model=ManPower
		fields=['employee','project','time_in','time_out','lunch','shift','working_time']





