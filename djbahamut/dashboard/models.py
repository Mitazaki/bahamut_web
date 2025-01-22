# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ApplicationCooldown(models.Model):
    memberid = models.BigIntegerField(primary_key=True)  # The composite primary key (memberid, for_guild) found, that is not supported. The first column is selected.
    for_guild = models.BigIntegerField()
    last_app = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'application_cooldown'
        unique_together = (('memberid', 'for_guild'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthTokens(models.Model):
    selector = models.CharField(max_length=12, blank=True, null=True)
    token = models.CharField(max_length=64, blank=True, null=True)
    userid = models.CharField(max_length=70)
    expires = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_tokens'


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bounties(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    syndicate = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bounties'


class ClanApplications(models.Model):
    userid = models.PositiveBigIntegerField(primary_key=True)
    blizzid = models.TextField(blank=True, null=True)
    for_guild = models.BigIntegerField()
    threadid = models.PositiveBigIntegerField(blank=True, null=True)
    channelid = models.PositiveBigIntegerField(blank=True, null=True)
    expire_time = models.DateTimeField()
    warning_sent = models.IntegerField()
    interaction = models.BigIntegerField(blank=True, null=True)
    approved = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clan_applications'


class ClanClViews(models.Model):
    m_id = models.BigIntegerField(primary_key=True)
    cl_dmid = models.BigIntegerField()
    cl_member_id = models.BigIntegerField()
    cl_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clan_cl_views'


class ClanComments(models.Model):
    com_id = models.AutoField(primary_key=True)
    com_dcid = models.CharField(max_length=50)
    com_comment = models.TextField()
    com_time = models.IntegerField()
    com_by = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'clan_comments'


class ClanData(models.Model):
    data_server = models.CharField(primary_key=True, max_length=70)
    data_botname = models.CharField(max_length=32)
    data_game_id = models.CharField(max_length=20, blank=True, null=True)
    data_link_id = models.BigIntegerField(blank=True, null=True)
    data_link_role_ping = models.TextField(blank=True, null=True)
    data_exempts = models.TextField()
    data_app_enable = models.IntegerField()
    data_activity_enable = models.IntegerField()
    data_app_expire = models.IntegerField(blank=True, null=True)
    data_app_alliance = models.IntegerField()
    data_app_ally_roles = models.TextField()
    data_divchar = models.CharField(max_length=1)
    data_stacard_color = models.CharField(max_length=20)
    data_stat_all = models.BigIntegerField(blank=True, null=True)
    data_stat_members = models.BigIntegerField(blank=True, null=True)
    data_stat_other = models.BigIntegerField(blank=True, null=True)
    data_stat_online = models.BigIntegerField(blank=True, null=True)
    data_welcome_title = models.CharField(max_length=256)
    data_welcome_desc = models.CharField(max_length=4096)
    data_welcome_img = models.CharField(max_length=2048)
    data_welcome_fieldname = models.CharField(max_length=256)
    data_welcome_fieldvalue = models.CharField(max_length=1024)
    data_welcome_footname = models.CharField(max_length=256)
    data_welcome_footvalue = models.CharField(max_length=1024)
    data_welcome_icon = models.CharField(max_length=2048)
    data_lfg_prefix = models.CharField(max_length=50, blank=True, null=True)
    data_lfg_chan = models.BigIntegerField(blank=True, null=True)
    data_lfg_ping = models.BigIntegerField(blank=True, null=True)
    data_xp_mod = models.FloatField()
    data_xp_adj_txt = models.CharField(max_length=20)
    data_xp_adj_vc = models.CharField(max_length=20)
    data_xp_bonus = models.IntegerField()
    data_xp_muted = models.IntegerField()
    data_xp_alone = models.IntegerField()
    data_xp_booster = models.IntegerField()
    data_chan_logs = models.BigIntegerField(blank=True, null=True)
    data_chan_modlogs = models.BigIntegerField(blank=True, null=True)
    data_chan_tasks = models.BigIntegerField(blank=True, null=True)
    data_chan_levelup = models.BigIntegerField(blank=True, null=True)
    data_chan_welcome = models.BigIntegerField(blank=True, null=True)
    data_chan_wftime = models.BigIntegerField(blank=True, null=True)
    data_chan_cetus = models.BigIntegerField(blank=True, null=True)
    data_chan_earth = models.BigIntegerField(blank=True, null=True)
    data_chan_deimos = models.BigIntegerField(blank=True, null=True)
    data_chan_fortuna = models.BigIntegerField(blank=True, null=True)
    data_chan_invite = models.BigIntegerField(blank=True, null=True)
    data_chan_bounties = models.BigIntegerField(blank=True, null=True)
    data_role_member = models.BigIntegerField(blank=True, null=True)
    data_role_guest = models.BigIntegerField(blank=True, null=True)
    data_role_applicant = models.BigIntegerField(blank=True, null=True)
    data_role_level = models.BigIntegerField(blank=True, null=True)
    data_role_clan_member = models.BigIntegerField(blank=True, null=True)
    data_role_welcome = models.BigIntegerField(blank=True, null=True)
    data_role_research = models.BigIntegerField(blank=True, null=True)
    data_task_memleft = models.CharField(max_length=70)
    data_task_memverify = models.CharField(max_length=70)
    data_task_incomplete = models.CharField(max_length=70)
    data_task_complete = models.CharField(max_length=70)
    data_task_research = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clan_data'


class ClanDataWelcomechans(models.Model):
    data_id = models.AutoField(primary_key=True)
    data_server = models.BigIntegerField()
    data_desc = models.CharField(max_length=256)
    data_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'clan_data_welcomechans'


class ClanMemberAcLogs(models.Model):
    log_id = models.BigAutoField(primary_key=True)
    log_time = models.BigIntegerField(blank=True, null=True)
    log_reason = models.TextField()
    log_mid = models.BigIntegerField(blank=True, null=True)
    log_type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clan_member_ac_logs'


class ClanMembersLogs(models.Model):
    log_id = models.BigAutoField(primary_key=True)
    log_discordid = models.CharField(max_length=50, blank=True, null=True)
    log_discordname = models.CharField(max_length=50, blank=True, null=True)
    log_discordnick = models.CharField(max_length=70, blank=True, null=True)
    log_gamename = models.CharField(max_length=50, blank=True, null=True)
    log_type = models.TextField(blank=True, null=True)
    log_desc = models.TextField(blank=True, null=True)
    log_admin = models.CharField(max_length=50, blank=True, null=True)
    log_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clan_members_logs'


class ClanModnotes(models.Model):
    modnotes_id = models.BigAutoField(primary_key=True)
    modnotes_guild_id = models.BigIntegerField(blank=True, null=True)
    modnotes_member_id = models.BigIntegerField()
    modnotes_member_name = models.CharField(max_length=32)
    modnotes_note = models.TextField(blank=True, null=True)
    modnotes_moderator_id = models.BigIntegerField(blank=True, null=True)
    modnotes_moderator_name = models.CharField(max_length=32, blank=True, null=True)
    modnotes_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'clan_modnotes'


class ClanRanks(models.Model):
    rank_id = models.IntegerField(primary_key=True)
    rank_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'clan_ranks'


class ClanReqact(models.Model):
    ra_rank = models.IntegerField(primary_key=True)
    ra_days = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clan_reqact'


class ClanRewards(models.Model):
    rewards_server = models.PositiveBigIntegerField()
    rewards_level = models.BigIntegerField()
    rewards_role = models.PositiveBigIntegerField()
    rewards_conditionalrole = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clan_rewards'


class ClanRoles(models.Model):
    role_id = models.CharField(primary_key=True, max_length=70)
    role_color = models.CharField(max_length=10)
    role_created_at = models.IntegerField()
    role_icon = models.TextField(blank=True, null=True)
    role_name = models.CharField(max_length=100)
    role_position = models.IntegerField()
    role_updated = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clan_roles'


class ClanXp(models.Model):
    member_id = models.CharField(primary_key=True, max_length=255)
    xp_amount = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clan_xp'


class ClanXpBak(models.Model):
    member_id = models.CharField(primary_key=True, max_length=255)
    xp_amount = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clan_xp_bak'


class ClanXpLogs(models.Model):
    id_code = models.CharField(primary_key=True, max_length=100)
    member_server = models.BigIntegerField()
    member_id = models.BigIntegerField()
    member_name = models.CharField(max_length=70)
    xp_type = models.IntegerField()
    xp_channel_id = models.CharField(max_length=70)
    xp_channel_name = models.TextField()
    xp_time = models.BigIntegerField()
    xp_day = models.CharField(max_length=10)
    xp_mins = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clan_xp_logs'


class ClanXpOld(models.Model):
    member_id = models.BigIntegerField(primary_key=True)
    member_server = models.BigIntegerField()
    xp_amount = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'clan_xp_old'


class DiscordKeepalive(models.Model):
    post_id = models.BigIntegerField(primary_key=True)
    post_time = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'discord_keepalive'


class DiscordloginDiscorduser(models.Model):
    discord_id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=255)
    avatar = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    mfa_enabled = models.IntegerField()
    locale = models.CharField(max_length=255)
    flags = models.IntegerField()
    public_flags = models.BigIntegerField()
    last_login = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discordlogin_discorduser'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GuildMembers(models.Model):
    guild_id = models.BigIntegerField(primary_key=True)  # The composite primary key (guild_id, member_id) found, that is not supported. The first column is selected.
    member_id = models.BigIntegerField()
    member_name = models.CharField(max_length=255)
    member_joined = models.DateTimeField()
    member_created = models.DateTimeField()
    is_bahamut_admin = models.IntegerField()
    can_manage_server = models.IntegerField()
    is_server_owner = models.IntegerField()
    game_id = models.CharField(max_length=35, blank=True, null=True)
    verified = models.IntegerField(blank=True, null=True)
    task_inv_interaction = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guild_members'
        unique_together = (('guild_id', 'member_id'),)


class GuildMembersBackup(models.Model):
    guild_id = models.BigIntegerField(primary_key=True)  # The composite primary key (guild_id, member_id) found, that is not supported. The first column is selected.
    member_id = models.BigIntegerField()
    member_name = models.CharField(max_length=255)
    member_joined = models.DateTimeField()
    member_created = models.DateTimeField()
    is_bahamut_admin = models.IntegerField()
    can_manage_server = models.IntegerField()
    is_server_owner = models.IntegerField()
    game_id = models.CharField(max_length=30, blank=True, null=True)
    verified = models.IntegerField(blank=True, null=True)
    task_inv_interaction = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guild_members_backup'
        unique_together = (('guild_id', 'member_id'),)


class Guilds(models.Model):
    guild_id = models.BigIntegerField(primary_key=True)
    guild_name = models.CharField(max_length=255)
    guild_icon = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guilds'


class JobRewards(models.Model):
    job = models.OneToOneField('Jobs', models.DO_NOTHING, primary_key=True)  # The composite primary key (job_id, name, type) found, that is not supported. The first column is selected.
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    count = models.IntegerField(blank=True, null=True)
    chance = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_rewards'
        unique_together = (('job', 'name', 'type'),)


class Jobs(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    bounty = models.ForeignKey(Bounties, models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    min_level = models.IntegerField(blank=True, null=True)
    max_level = models.IntegerField(blank=True, null=True)
    rotation = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jobs'


class MentionChans(models.Model):
    guild_id = models.BigIntegerField(primary_key=True)  # The composite primary key (guild_id, channel_id) found, that is not supported. The first column is selected.
    channel_id = models.BigIntegerField()
    mention_id = models.BigIntegerField()
    add_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mention_chans'
        unique_together = (('guild_id', 'channel_id'),)


class Messages(models.Model):
    msgid = models.BigIntegerField(primary_key=True)
    msgchan = models.CharField(max_length=100)
    msgauthor = models.CharField(max_length=100)
    msgcontent = models.TextField()
    msghigh = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'messages'


class PartyChannels(models.Model):
    guild_id = models.BigIntegerField(primary_key=True)  # The composite primary key (guild_id, channel_id) found, that is not supported. The first column is selected.
    channel_id = models.BigIntegerField()
    owner_id = models.BigIntegerField()
    lfg_id = models.BigIntegerField(blank=True, null=True)
    interaction_id = models.BigIntegerField(blank=True, null=True)
    is_open = models.IntegerField(blank=True, null=True)
    area = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_channels'
        unique_together = (('guild_id', 'channel_id'),)


class SuggestChans(models.Model):
    guild_id = models.BigIntegerField(primary_key=True)  # The composite primary key (guild_id, channel_id) found, that is not supported. The first column is selected.
    channel_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'suggest_chans'
        unique_together = (('guild_id', 'channel_id'),)


class XpAmounts(models.Model):
    job = models.OneToOneField(Jobs, models.DO_NOTHING, primary_key=True)  # The composite primary key (job_id, xp_amount) found, that is not supported. The first column is selected.
    xp_amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'xp_amounts'
        unique_together = (('job', 'xp_amount'),)


class XpCatBlacklist(models.Model):
    voice_channel_id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'xp_cat_blacklist'


class XpChanBlacklist(models.Model):
    chan_channel_id = models.BigIntegerField(primary_key=True)  # The composite primary key (chan_channel_id, chan_server) found, that is not supported. The first column is selected.
    chan_server = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'xp_chan_blacklist'
        unique_together = (('chan_channel_id', 'chan_server'),)


class XpRoleBlacklist(models.Model):
    role_id = models.BigIntegerField(primary_key=True)
    role_server = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'xp_role_blacklist'
