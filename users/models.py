from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from .managers import UserManager
from .utils import get_filename


class User(AbstractBaseUser, PermissionsMixin):
    """Custom User model for the app."""
    TEACHER = 1

    ROLE_CHOICES = (
        (TEACHER, 'Teacher'),
    )

    school = models.ForeignKey('schools.School', on_delete=models.CASCADE)
    role = models.SmallIntegerField(choices=ROLE_CHOICES, default=TEACHER)
    email = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, default='', db_index=True)
    phone = models.CharField(max_length=25, default='')
    room_number = models.CharField(max_length=10, default='')
    subjects = models.TextField(default='', help_text='List of subject assigned to a teacher')
    profile_picture = models.FileField(upload_to=get_filename, null=True, blank=True)
    date_registered = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    objects = UserManager()

    class Meta:
        ordering = ['last_name']
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'.strip()

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'.strip()

    @property
    def is_staff(self):
        return self.is_superuser

    @property
    def get_user_color(self):
        user_name = self.name
        color = '#' + hex(hash(user_name))[-6:]
        return color

    @property
    def profile_picture_url(self):
        if self.profile_picture and hasattr(self.profile_picture, 'url'):
            return self.profile_picture.url
        else:
            return False
