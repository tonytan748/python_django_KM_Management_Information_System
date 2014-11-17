from django.db import models
from django.contrib.auth.models import User

class UserContent(models.Model):
	user=models.ForeignKey(User)
	content=models.CharField(max_length=20)
	url=models.URLField(max_length=100)
	rights=models.CharField(max_length=120,default='read')
	
	def __unicode__(self):
		return "%s--%s" % (self.user,self.content)
	
	class Meta:
		ordering=('user',)
