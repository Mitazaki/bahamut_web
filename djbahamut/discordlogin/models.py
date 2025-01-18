from django.db import models

# Create your models here.
class DiscordUser(models.Model):
    discord_id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=255)
    avatar = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    mfa_enabled = models.BooleanField()
    locale = models.CharField(max_length=255)
    flags = models.IntegerField()
    public_flags = models.BigIntegerField()
    last_login = models.DateTimeField()
    
    def __str__(self):
        return self.username