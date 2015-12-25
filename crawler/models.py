from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import models as auth_models


class CustomUserManager(auth_models.BaseUserManager):
    def create_user(self, email, user_name, password):

        user = self.model(
                email=CustomUserManager.normalize_email(email),
                user_name=user_name,
        )
        user.is_staff = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, user_name, password):

        user = self.model(
                email=CustomUserManager.normalize_email(email),
                user_name=user_name,
        )
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class UserProfile(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    """ Model for user profile """

    email = models.EmailField(verbose_name='E-Mail', unique=True)
    user_name = models.CharField(verbose_name='User Name', max_length=20, unique=True)
    is_staff = models.BooleanField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', ]

    objects = CustomUserManager()

    def get_full_name(self):
        return self.user_name

    def get_short_name(self):
        return self.user_name

    def __unicode__(self):
        return self.email

    def is_staff(self):
        return self.is_staff


class NewsItem(models.Model):
    """
    Model for News which needs to be crawl
    """
    user_name = models.ForeignKey(UserProfile)
    title = models.CharField(max_length=255)
    hacker_news_url = models.URLField(max_length=255, unique=True)
    url = models.URLField(max_length=255)
    posted_on = models.DateTimeField()
    upvotes = models.IntegerField()
    comments = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title



