from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
	def create_user(self, username, email, first_name=None, last_name=None, password=None):
		if not username:
			raise ValueError('User name is required!')
		if not email:
			raise ValueError('Email must be provided!')
		if not password:
			raise ValueError('Password can not be empty!')

		user = self.model(
			username=username,
			email=email,
			first_name=first_name,
			last_name=last_name
		)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, username, email, first_name=None, last_name=None, password=None):
		user = self.create_user(
			username,
			email,
			first_name=first_name,
			last_name=last_name,
			password=password
		)
		user.staff = True
		user.admin = True
		user.save(using=self._db)
		return user

	def create_staffuser(self, username, email, first_name=None, last_name=None, password=None):
		user = self.create_user(
			username,
			email,
			first_name=first_name,
			last_name=last_name,
			password=password
		)
		user.staff = True
		user.save(using=self._db)
		return user


class User(AbstractBaseUser):
	username = models.CharField(max_length=120, unique=True, null=True)
	email = models.EmailField(max_length=255, unique=True, null=True)
	first_name = models.CharField(max_length=100, blank=True, null=True)
	last_name = models.CharField(max_length=300, blank=True, null=True)
	admin = models.BooleanField(default=False)
	staff = models.BooleanField(default=False)
	active = models.BooleanField(default=True)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	objects = UserManager()

	def __str__(self, *args, **kwargs):
		return self.username

	def has_perm(self, perm, obj=None, *args, **kwargs):
		return True
	
	def has_module_perms(self, app_label, *args, **kwargs):
		return True

	@property
	def get_fullname(self, *args, **kwargs):
		return f'{self.first_name} {self.last_name}'

	@property
	def is_admin(self, *args, **kwargs):
		return self.admin

	@property
	def is_staff(self, *args, **kwargs):
		return self.staff

	@property
	def is_active(self, *args, **kwargs):
		return self.active

