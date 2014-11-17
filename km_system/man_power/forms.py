from django import forms
from models import ManPower

class ManPowerForm(frmo.ModelForm):
	
	class Meta:
		model=ManPower
		exclude=('time100','time100salary','time125','time125salary','time150','time150salary','time200','time200salary','timeremark','is_payed','payed_period')



