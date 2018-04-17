# resources for browser navigation and webpage rendering
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse

# views used in this file
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.base import TemplateView

# authentication and login resources
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

# forms used in this file
from .forms import CreateUserForm, CreatePostForm

# models used in this file
from django.contrib.auth.models import User
from blog.models import BlogPost

from django.utils import timezone
import datetime
now = datetime.datetime.now()

# INDEX  VIEW
# ===========

class AjaxableResponseMixin:
	def form_invalid(self, form):
		response = super().form_invalid(form)
		if self.request.is_ajax():
			return JsonResponse(form.errors, status=400)
		else:
			return response

	def form_valid(self, form):
		response = super().form_valid(form)
		if self.request.is_ajax():
			data = {
				'pk': BlogPost.object.pk,
			}
			return JsonResponse(data)
		else:
			return response
	def get_queryset(self):
		if self.request.is_ajax():
			data = {
				'pk': BlogPost.object.pk,
			}
			return JsonResponse(data)
		else:
			return BlogPost.objects.order_by('-pub_date')
    


# imports used: List View, BlogPost
class HomePage(AjaxableResponseMixin, ListView):
	model = BlogPost
	template_name = 'index.html'
		
	def get_queryset(self):
		return BlogPost.objects.order_by('-pub_date')
		


# AUTHOR LIST VIEW
# ================

# imports used : ListView, User
class UserList(ListView):
	model = User
	template_name = 'user_list.html'
	


# USER ACCOUNT VIEWS
# ==================

# called when user asks to create account
# imports used: views.View, forms.CreateUserForm, User, authenticate, HttpResponse, render
class CreateAccountView(View):
	form_class = CreateUserForm
	initial = { 'key' : 'value'}
	template_name = 'new_account.html'
	
	def get(self, request):
		form = self.form_class(initial=self.initial)
		if request.user.is_authenticated:
			#TODO Give user option to logout or return to profile
			return HttpResponse("You are already logged in.")
		return render(request, self.template_name, { 'form' : form })
	
	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			form.save()

# used to show an authenticated user the posts they have written and edit them
# imports used: LoginRequiredMixin, ListView, BlogPost
class UserProfileView(LoginRequiredMixin, ListView):
	model = BlogPost
	template_name = 'profile.html'
	
	def get_queryset(self):
		qs = super(UserProfileView, self).get_queryset()
		return qs.filter(author=self.request.user).order_by('-pub_date')

# used to show a list of posts written by a user
# imports used: ListView, BlogPost
class AuthorView(ListView):
	model = BlogPost
	template_name = 'author_detail.html'
	
	def get_queryset(self):
		qs = super(AuthorView, self).get_queryset()
		return BlogPost.objects.filter(author__username__contains=self.kwargs['author']).order_by('-pub_date')


# BLOG POST VIEWS
# ===============

# imports used: view.DetailView, model.BlogPost
class PostDetail(DetailView):
	model = BlogPost

# imports used: views.CreateView, model.BlogPost, render, form.CreatePostForm
class BlogPostCreate(LoginRequiredMixin, CreateView):
	template_name = 'create_post.html'
	form_class = CreatePostForm
	initial = { 'key' : 'value'}
	
	def get(self, request):
		form = self.form_class(initial=self.initial)
		return render(request, self.template_name, { 'form' : form })
	
	def form_valid(self, form):
		form.instance.author = self.request.user
		form.instance.pub_date = now
		form.instance.last_edit_date = now
		return super().form_valid(form)
		if form.is_valid():
			form.save()

# imports used: LoginRequiredMixin, view.UpdateView, model.BlogPost, 
class BlogPostEdit(LoginRequiredMixin, UpdateView):
	model = BlogPost
	fields = ('title', 'content')
	template_name = 'edit_post.html'
	
	def get_queryset(self):
		qs = super(BlogPostEdit, self).get_queryset()
		return qs.filter(author=self.request.user)
		
	def form_valid(self, form):
		form.instance.last_edit_date = now
		return super().form_valid(form)
		if form.is_valid():
			form.save()
	
# imports used: LoginRequiredMixin, view.DeleteView, model.BlogPost
class BlogPostDelete(LoginRequiredMixin, DeleteView):
	model = BlogPost
	template_name = 'delete_post.html'
	
	def get_queryset(self):
		qs = super(BlogPostDelete, self).get_queryset()
		return qs.filter(author=self.request.user)
	success_url='/blog/'
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
