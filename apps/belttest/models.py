from __future__ import unicode_literals

from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.

class UserManager(models.Manager):
	def login_validator(self, postData):
		errors = {}
		if not len(postData['email']) or len(postData['password']) < 8:
			errors['email']="Please enter valid credentials."
		return errors

	def basic_validator(self, postData):
		errors = {}
# VALIDATING THE NAME
		if len(postData['name']) == 0:
			errors['name']="Please enter your name"
# VALIDATING username
		if len(postData['alias']) == 0:
			errors['alias']="Please enter your username"
# VALIDATING EMAIL
		if not EMAIL_REGEX.match(postData['email']):
			errors['email']="Please enter a valid email"
# VALIDATING PASSWORD
		if len(postData['password']) == 0:
			errors['password']="Please enter a password"
		else:
			if len(postData['password']) < 8:
				errors['password']= "Password must be at least 8 characters."

			if not any([letter.isupper() for letter in postData['password']]):
				errors['password1']= "Password must contain at least one uppercase letter."

			if not any([letter.isdigit() for letter in postData['password']]):
				errors['password2']= "Password must contain at least one number."

			if not any([letter in "!@#$%^&*()-_=+~`\"'<>,.?/:;\}{][|" for letter in postData['password']]):
				errors['password3']= "Password must contain at least one special character."

			if postData['password'] != postData['passconf']:
				errors['password4']= 'Password and confirmation fields must match.'
		return errors


class User(models.Model):
	name = models.CharField(max_length=255)
	alias = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	dob = models.DateField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()
	def __repr__(self):
		return ("<User object: id:{} {} {}>".format(self.id, self.name, self.alias))

class Friend(models.Model):
	user = models.ForeignKey(User, related_name = "friender")
	friend = models.ForeignKey(User, related_name = "friendee")






























