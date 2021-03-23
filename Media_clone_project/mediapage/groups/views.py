from django.shortcuts import render

from django.contrib.auth.mixins import (LoginRequiredMixin,
										PermissionRequiredMixin)
from django.urls import reverse
from django.views import generic
from . models import Group,GroupMember
from django.shortcuts import get_object_or_404
from django.contrib import messages
from . import models

class CreateGroup(LoginRequiredMixin,generic.edit.CreateView):
	fields = ['name','description']
	model = Group

class SingleGroup(generic.detail.DetailView):
	model = Group

class ListGroup(generic.list.ListView):
	model = Group

class JoinGroup(LoginRequiredMixin,generic.base.RedirectView):

	def get_redirect_url(self,*args,**kwargs):
		return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})

	def get(self,request,*args,**kwargs):
		group = get_object_or_404(Group,slug=self.kwargs.get('slug'))

		try:
			GroupMember.objects.create(user=self.request.user,group=group)
		except:
			messages.warning(self.request,('Warning already a member!'))
		else:
			messages.success(self.request, 'You are now a member!')

		return super().get(request,*args,**kwargs)

class LeaveGroup(LoginRequiredMixin,generic.base.RedirectView):

	def get_redirect_url(self,*args,**kwargs):
		return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})

	def get(self,request,*args,**kwargs):

		try:
			membership = models.GroupMember.objects.filter(
				user=self.request.user,
				group__slug=self.kwargs.get('slug')).get()

		except models.GroupMember.DoesNotExist:
			messages.warning(self.request, 'Sorry you are not in this group!')

		else:
			membership.delete()
			messages.success(self.request, 'You are left the group!')
		return super().get(request,*args,**kwargs)