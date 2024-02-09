from django.db import models
from usermanagement.common.models import BaseModel

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager as BUM, PermissionsMixin, Group, GroupManager, Permission
# from guardian.models import
from django.utils.translation import gettext_lazy as _



class UserTypesChoices(models.TextChoices):
    STAFF = '1', 'staff'
    CUSTOMER = '2', 'customer'
    SUPERVISOR = '3', 'supervisor'



class BaseUserManager(BUM):
    def create_user(self, email, is_active=True, is_admin=False, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(email=self.normalize_email(email.lower()), is_active=is_active, is_admin=is_admin)

        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.full_clean()
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=email,
            is_active=True,
            is_admin=True,
            password=password,
        )

        user.is_superuser = True
        user.save(using=self._db)

        return user


# class PermissionsMixin(BM):
#     groups = models.ManyToManyField(
#         BaseGroup,
#         verbose_name=_("groups"),
#         blank=True,
#         help_text=_(
#             "The groups this user belongs to. A user will get all permissions "
#             "granted to each of their groups."
#         ),
#         related_name="user_set",
#         related_query_name="user",
#     )

class Company(BaseModel):
    title = models.CharField(max_length=155)

    def __str__(self):
        return str(self.title)


class CompanyGroups(models.Model):
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING)

    permissions = models.ManyToManyField(
        Permission,
        verbose_name=_("permissions"),
        blank=True,
    )

    class Meta:
        verbose_name = _("company group")
        verbose_name_plural = _("company groups")

    def __str__(self):
        return f"{self.company} - {self.group}"



class BaseUser(BaseModel, AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(verbose_name="email address", unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    type = models.CharField(max_length=50, choices=UserTypesChoices.choices, default='2')
    is_staff = models.BooleanField(default=False)
    last_company_logged_in = models.ForeignKey(Company, on_delete=models.DO_NOTHING)

    objects = BaseUserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email


class Process(models.Model):
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    created_by = models.ForeignKey(BaseUser, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        permissions = [('dg_can_view_process', 'OBP can view process'), ('dg_can_start_process', 'OBP can start process')]

    def __str__(self):
        return str(self.name)


class Route(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        permissions = [('dg_can_get_route', 'OBP can get route'), ('dg_can_post_route', 'OBP can post route')]

    def __str__(self):
        return str(self.name)


# class CustomPermission(models.Model):
#     description = models.CharField(max_length=255)
#     company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
#     groups = models.ForeignKey(Group, on_delete=models.DO_NOTHING)

