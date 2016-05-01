from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
import uuid
from django.dispatch import receiver
from django.db.models.signals import post_save

class EmailUserManager(BaseUserManager):

    def create_user(
        self,
        email,
        password=None,
        ):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
        #authenticate using url but only if password != null,
        #move login view and registration template to newuser
        #if cookie for that user, log into that user

    def create_superuser(
        self,
        email,
        password,
        ):

        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class EmailUser(AbstractBaseUser):

    email = models.EmailField(verbose_name='email address',
                              max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    token = models.UUIDField(blank=True, null=True)


    objects = EmailUserManager()

    USERNAME_FIELD = 'email'


    def get_full_name(self):

        # The user is identified by their email address

        return self.email

    def get_short_name(self):

        # The user is identified by their email address f35c

        return self.email

    def __str__(self):  # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        '''Does the user have a specific permission?'''

        # Simplest possible answer: Yes, always

        return True

    def has_module_perms(self, app_label):
        '''Does the user have permissions to view the app `app_label`?'''

        # Simplest possible answer: Yes, always

        return True

    @property
    def is_staff(self):
        '''Is the user a member of staff?'''

        # Simplest possible answer: All admins are staff

        return self.is_admin


# put in its own file to minimise side-effects
@receiver(post_save, sender=EmailUser)
def generate_token(sender, instance, created, **kwargs):
	if created:
		instance.token = uuid.uuid1().hex
		instance.save()
