from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserProfileManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users must have an email')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
class Role(models.TextChoices):
    EMPLOYEE = "EMPLOYEE", "Employee"
    EMPLOYER = "EMPLOYER", "Employer"

class UserProfile(AbstractBaseUser, PermissionsMixin):

    role = models.CharField(max_length=100, choices=Role.choices, default =Role.EMPLOYEE)
    email = models.EmailField(max_length=255, unique=True)
    firstName =models.CharField(max_length=250, null=True)
    lastName =models.CharField(max_length=250, null=True)
    companyName =models.CharField(max_length=1000, null=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email