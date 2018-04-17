from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
	
class BlogPost(models.Model):
	title = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	last_edit_date = models.DateTimeField('date last edited')
	author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, editable=False)
	content = models.TextField(null=True)
	
	class Meta:
		ordering = [ 'pub_date' ]
		
	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse('blog:post_detail', kwargs={ 'pk' : self.pk })