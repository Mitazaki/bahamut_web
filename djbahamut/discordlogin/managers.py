from django.contrib.auth import models

class DiscordUserOAuth2Manager(models.UserManager):
    def create_new_discord_user(self,user):
        print('Inside Discord User Manager')
        discordtag = '%s#%s' % (user['username'], user['discriminator'])
        new_user = self.create(
            discord_id=user['id'],
            username=user['username'],
            avatar=user['avatar'],
            email=user['email'],
            mfa_enabled=user['mfa_enabled'],
            locale=user['locale'],
            flags=user['flags'],
            public_flags=user['public_flags']
        )
        return new_user