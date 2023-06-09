from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .utils.user_manager import UserManager


class User(AbstractBaseUser):
    # See https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#specifying-a-custom-user-model
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    birthdate = models.DateField(blank=True, null=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Account(models.Model):
    username = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=50)  # "personal" or "business"
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    business_name = models.CharField(max_length=100, blank=True, null=True)
    initial = models.CharField(max_length=1, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_display_name(self):
        if self.type == "personal":
            return f"{self.first_name} {self.last_name}"

        return self.business_name

    def __str__(self):
        return self.username


class Pin(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    image_url = models.URLField(max_length=200)
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return f"Pin {self.id} by {self.author.username}"
