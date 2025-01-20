from django.db import models
from .managers import DiscordUserOAuth2Manager

# Create your models here.
class DiscordUser(models.Model):
    objects = DiscordUserOAuth2Manager()

    discord_id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=255)
    avatar = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    mfa_enabled = models.BooleanField()
    locale = models.CharField(max_length=255)
    flags = models.IntegerField()
    public_flags = models.BigIntegerField()
    last_login = models.DateTimeField(null=True)
    
    def is_authenticated(self,request):
        return True

    def __str__(self):
        return self.username