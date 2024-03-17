from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from .managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

NULLABLE = {
    "null": True,
    "blank": True
}


class UserRoles(models.TextChoices):
    ADMIN = "Admin"
    USER = "User"


class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=50, verbose_name='имя пользователя')
    last_name = models.CharField(max_length=50, verbose_name='фамилия пользователя')
    phone = models.CharField(max_length=15, verbose_name='телефон пользователя')
    email = models.EmailField(unique=True, verbose_name="почта пользователя")
    role = models.CharField(max_length=10, default=UserRoles.USER, choices=UserRoles.choices, verbose_name="роли")
    image = models.ImageField(upload_to="profile_images", verbose_name="фото пользователя", **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name="активность пользователя")

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    # @property
    # def is_superuser(self):
    #     return self.is_admin

    # @property
    # def is_staff(self):
    #     return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
