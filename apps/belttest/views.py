# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt
from django.core.urlresolvers import reverse
from django.db.models.base import ObjectDoesNotExist
# Create your views here.
def index(request):
	if "user" in request.session:
		return redirect('/friends')
	return render(request, "belttest/index.html")

def login(request):
	errors = User.objects.login_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect('/')
	else:
		try:
			user = User.objects.get(email=request.POST['email'])

		except ObjectDoesNotExist:
			messages.error(request, "Account does not exist.")
			return redirect('/')

		if user == True:
			if not bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
				messages.error(request, 'Account with those credentials could not be found.')
				return redirect('/')
		else:
			if user:
				request.session['user'] = user.id
				messages.success(request, 'Login Successful!')
				return	redirect('/friends')
				# return redirect(reverse('success',kwargs ={'user_id':user.id}))

def logout(request):
	del request.session['user']
	return redirect('/')

def register(request):
	errors = User.objects.basic_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags= tag)
		return redirect('/')
	else:
		user = User.objects.create()
		user.name = request.POST['name']
		user.alias = request.POST['alias']
		user.email = request.POST['email']
		user.dob =request.POST['dob']
		user.password =bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
		user.save()
		messages.success(request, 'User created. Please login!')
		return redirect('/')

def friends(request):
	all_users = User.objects.exclude(id = request.session['user'])
	my_friends = Friend.objects.filter(user_id = request.session['user'])

	friends_table = []
	for friend in my_friends:
		friends_table.append(friend.friend_id)
	print "friendstable", friends_table

	not_friends = []
	for notfriend in all_users:
		if notfriend.id not in friends_table:
			not_friends.append(notfriend)
	print "notfriendstable", not_friends

	context={
	'user': User.objects.get(id = request.session['user']),
	'friends': Friend.objects.filter(user_id = request.session['user']),
	'not_friends': not_friends,
	}
	return render(request, "belttest/friends.html", context)

def viewprofile(request, user_id):
	context={
	'user':User.objects.get(id = user_id),
	}

	return render(request, "belttest/userprofile.html", context)

def removefriend(request, user_id):
	Friend.objects.get(user_id=request.session['user'], friend_id=user_id).delete()
	return redirect('/')

def addfriend(request, user_id):
	Friend.objects.create(friend_id=user_id, user_id=request.session['user'])
	Friend.objects.create(friend_id=request.session['user'], user_id=user_id)
	return redirect('/')



