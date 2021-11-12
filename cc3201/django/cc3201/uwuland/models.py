# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Actions(models.Model):
    playerid = models.OneToOneField('Players', models.DO_NOTHING, db_column='playerid', primary_key=True)
    matchid = models.ForeignKey('Matches', models.DO_NOTHING, db_column='matchid')
    teamid = models.ForeignKey('Teams', models.DO_NOTHING, db_column='teamid', blank=True, null=True)
    firstgoal = models.IntegerField(blank=True, null=True)
    winninggoal = models.IntegerField(blank=True, null=True)
    shotsontargetincgoals = models.IntegerField(blank=True, null=True)
    savesmade = models.IntegerField(blank=True, null=True)
    timeplayed = models.IntegerField(blank=True, null=True)
    positionid = models.IntegerField(blank=True, null=True)
    starts = models.IntegerField(blank=True, null=True)
    substituteon = models.IntegerField(blank=True, null=True)
    substituteoff = models.IntegerField(blank=True, null=True)
    goals = models.IntegerField(blank=True, null=True)
    shotsofftargetincwoodwork = models.IntegerField(blank=True, null=True)
    blockedshots = models.IntegerField(blank=True, null=True)
    penaltiestaken = models.IntegerField(blank=True, null=True)
    penaltygoals = models.IntegerField(blank=True, null=True)
    penaltiessaved = models.IntegerField(blank=True, null=True)
    penaltiesofftarget = models.IntegerField(blank=True, null=True)
    penaltiesnotscored = models.IntegerField(blank=True, null=True)
    directfreekickgoals = models.IntegerField(blank=True, null=True)
    directfreekickontarget = models.IntegerField(blank=True, null=True)
    directfreekickofftarget = models.IntegerField(blank=True, null=True)
    blockeddirectfreekick = models.IntegerField(blank=True, null=True)
    goalsfrominsidebox = models.IntegerField(blank=True, null=True)
    shotsonfrominsidebox = models.IntegerField(blank=True, null=True)
    shotsofffrominsidebox = models.IntegerField(blank=True, null=True)
    blockedshotsfrominsidebox = models.IntegerField(blank=True, null=True)
    goalsfromoutsidebox = models.IntegerField(blank=True, null=True)
    shotsontargetoutsidebox = models.IntegerField(blank=True, null=True)
    shotsofftargetoutsidebox = models.IntegerField(blank=True, null=True)
    blockedshotsoutsidebox = models.IntegerField(blank=True, null=True)
    headedgoals = models.IntegerField(blank=True, null=True)
    headedshotsontarget = models.IntegerField(blank=True, null=True)
    headedshotsofftarget = models.IntegerField(blank=True, null=True)
    headedblockedshots = models.IntegerField(blank=True, null=True)
    leftfootgoals = models.IntegerField(blank=True, null=True)
    leftfootshotsontarget = models.IntegerField(blank=True, null=True)
    leftfootshotsofftarget = models.IntegerField(blank=True, null=True)
    leftfootblockedshots = models.IntegerField(blank=True, null=True)
    rightfootgoals = models.IntegerField(blank=True, null=True)
    rightfootshotsontarget = models.IntegerField(blank=True, null=True)
    rightfootshotsofftarget = models.IntegerField(blank=True, null=True)
    rightfootblockedshots = models.IntegerField(blank=True, null=True)
    othergoals = models.IntegerField(blank=True, null=True)
    othershotsontarget = models.IntegerField(blank=True, null=True)
    othershotsofftarget = models.IntegerField(blank=True, null=True)
    otherblockedshots = models.IntegerField(blank=True, null=True)
    shotsclearedoffline = models.IntegerField(blank=True, null=True)
    shotsclearedofflineinsidearea = models.IntegerField(blank=True, null=True)
    shotsclearedofflineoutsidearea = models.IntegerField(blank=True, null=True)
    goalsopenplay = models.IntegerField(blank=True, null=True)
    goalsfromcorners = models.IntegerField(blank=True, null=True)
    goalsfromthrows = models.IntegerField(blank=True, null=True)
    goalsfromdirectfreekick = models.IntegerField(blank=True, null=True)
    goalsfromsetplay = models.IntegerField(blank=True, null=True)
    goalsfrompenalties = models.IntegerField(blank=True, null=True)
    attemptsopenplayontarget = models.IntegerField(blank=True, null=True)
    attemptsfromcornersontarget = models.IntegerField(blank=True, null=True)
    attemptsfromthrowsontarget = models.IntegerField(blank=True, null=True)
    attemptsfromdirectfreekickontarget = models.IntegerField(blank=True, null=True)
    attemptsfromsetplayontarget = models.IntegerField(blank=True, null=True)
    attemptsfrompenaltiesontarget = models.IntegerField(blank=True, null=True)
    attemptsopenplayofftarget = models.IntegerField(blank=True, null=True)
    attemptsfromcornersofftarget = models.IntegerField(blank=True, null=True)
    attemptsfromthrowsofftarget = models.IntegerField(blank=True, null=True)
    attemptsfromdirectfreekickofftarget = models.IntegerField(blank=True, null=True)
    attemptsfromsetplayofftarget = models.IntegerField(blank=True, null=True)
    attemptsfrompenaltiesofftarget = models.IntegerField(blank=True, null=True)
    goalsasasubstitute = models.IntegerField(blank=True, null=True)
    totalsuccessfulpassesall = models.IntegerField(blank=True, null=True)
    totalunsuccessfulpassesall = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)
    keypasses = models.IntegerField(blank=True, null=True)
    totalsuccessfulpassesexclcrossescorners = models.IntegerField(blank=True, null=True)
    totalunsuccessfulpassesexclcrossescorners = models.IntegerField(blank=True, null=True)
    successfulpassesownhalf = models.IntegerField(blank=True, null=True)
    unsuccessfulpassesownhalf = models.IntegerField(blank=True, null=True)
    successfulpassesoppositionhalf = models.IntegerField(blank=True, null=True)
    unsuccessfulpassesoppositionhalf = models.IntegerField(blank=True, null=True)
    successfulpassesdefensivethird = models.IntegerField(blank=True, null=True)
    unsuccessfulpassesdefensivethird = models.IntegerField(blank=True, null=True)
    successfulpassesmiddlethird = models.IntegerField(blank=True, null=True)
    unsuccessfulpassesmiddlethird = models.IntegerField(blank=True, null=True)
    successfulpassesfinalthird = models.IntegerField(blank=True, null=True)
    unsuccessfulpassesfinalthird = models.IntegerField(blank=True, null=True)
    successfulshortpasses = models.IntegerField(blank=True, null=True)
    unsuccessfulshortpasses = models.IntegerField(blank=True, null=True)
    successfullongpasses = models.IntegerField(blank=True, null=True)
    unsuccessfullongpasses = models.IntegerField(blank=True, null=True)
    successfulflickons = models.IntegerField(blank=True, null=True)
    unsuccessfulflickons = models.IntegerField(blank=True, null=True)
    successfulcrossescorners = models.IntegerField(blank=True, null=True)
    unsuccessfulcrossescorners = models.IntegerField(blank=True, null=True)
    cornerstakeninclshortcorners = models.IntegerField(blank=True, null=True)
    cornersconceded = models.IntegerField(blank=True, null=True)
    successfulcornersintobox = models.IntegerField(blank=True, null=True)
    unsuccessfulcornersintobox = models.IntegerField(blank=True, null=True)
    shortcorners = models.IntegerField(blank=True, null=True)
    throwinstoownplayer = models.IntegerField(blank=True, null=True)
    throwinstooppositionplayer = models.IntegerField(blank=True, null=True)
    successfuldribbles = models.IntegerField(blank=True, null=True)
    unsuccessfuldribbles = models.IntegerField(blank=True, null=True)
    successfulcrossescornersleft = models.IntegerField(blank=True, null=True)
    unsuccessfulcrossescornersleft = models.IntegerField(blank=True, null=True)
    successfulcrossesleft = models.IntegerField(blank=True, null=True)
    unsuccessfulcrossesleft = models.IntegerField(blank=True, null=True)
    successfulcornersleft = models.IntegerField(blank=True, null=True)
    unsuccessfulcornersleft = models.IntegerField(blank=True, null=True)
    successfulcrossescornersright = models.IntegerField(blank=True, null=True)
    unsuccessfulcrossescornersright = models.IntegerField(blank=True, null=True)
    successfulcrossesright = models.IntegerField(blank=True, null=True)
    unsuccessfulcrossesright = models.IntegerField(blank=True, null=True)
    successfulcornersright = models.IntegerField(blank=True, null=True)
    unsuccessfulcornersright = models.IntegerField(blank=True, null=True)
    successfullongballs = models.IntegerField(blank=True, null=True)
    unsuccessfullongballs = models.IntegerField(blank=True, null=True)
    successfullayoffs = models.IntegerField(blank=True, null=True)
    unsuccessfullayoffs = models.IntegerField(blank=True, null=True)
    throughball = models.IntegerField(blank=True, null=True)
    successfulcrossescornersintheair = models.IntegerField(blank=True, null=True)
    unsuccessfulcrossescornersintheair = models.IntegerField(blank=True, null=True)
    successfulcrossesintheair = models.IntegerField(blank=True, null=True)
    unsuccessfulcrossesintheair = models.IntegerField(blank=True, null=True)
    successfulopenplaycrosses = models.IntegerField(blank=True, null=True)
    unsuccessfulopenplaycrosses = models.IntegerField(blank=True, null=True)
    touches = models.IntegerField(blank=True, null=True)
    goalassistcorner = models.IntegerField(blank=True, null=True)
    goalassistfreekick = models.IntegerField(blank=True, null=True)
    goalassistthrowin = models.IntegerField(blank=True, null=True)
    goalassistgoalkick = models.IntegerField(blank=True, null=True)
    goalassistsetpiece = models.IntegerField(blank=True, null=True)
    keycorner = models.IntegerField(blank=True, null=True)
    keyfreekick = models.IntegerField(blank=True, null=True)
    keythrowin = models.IntegerField(blank=True, null=True)
    keygoalkick = models.IntegerField(blank=True, null=True)
    keysetpieces = models.IntegerField(blank=True, null=True)
    duelswon = models.IntegerField(blank=True, null=True)
    duelslost = models.IntegerField(blank=True, null=True)
    aerialduelswon = models.IntegerField(blank=True, null=True)
    aerialduelslost = models.IntegerField(blank=True, null=True)
    groundduelswon = models.IntegerField(blank=True, null=True)
    groundduelslost = models.IntegerField(blank=True, null=True)
    tackleswon = models.IntegerField(blank=True, null=True)
    tackleslost = models.IntegerField(blank=True, null=True)
    lastmantackle = models.IntegerField(blank=True, null=True)
    totalclearances = models.IntegerField(blank=True, null=True)
    headedclearances = models.IntegerField(blank=True, null=True)
    otherclearances = models.IntegerField(blank=True, null=True)
    clearancesofftheline = models.IntegerField(blank=True, null=True)
    blocks = models.IntegerField(blank=True, null=True)
    interceptions = models.IntegerField(blank=True, null=True)
    recoveries = models.IntegerField(blank=True, null=True)
    totalfoulsconceded = models.IntegerField(blank=True, null=True)
    foulsconcededexchandballspens = models.IntegerField(blank=True, null=True)
    totalfoulswon = models.IntegerField(blank=True, null=True)
    foulswonindangerareaincpens = models.IntegerField(blank=True, null=True)
    foulswonnotindangerarea = models.IntegerField(blank=True, null=True)
    foulwonpenalty = models.IntegerField(blank=True, null=True)
    handballsconceded = models.IntegerField(blank=True, null=True)
    penaltiesconceded = models.IntegerField(blank=True, null=True)
    offsides = models.IntegerField(blank=True, null=True)
    yellowcards = models.IntegerField(blank=True, null=True)
    redcards = models.IntegerField(blank=True, null=True)
    goalsconceded = models.IntegerField(blank=True, null=True)
    goalsconcededinsidebox = models.IntegerField(blank=True, null=True)
    goalsconcededoutsidebox = models.IntegerField(blank=True, null=True)
    savesmadefrominsidebox = models.IntegerField(blank=True, null=True)
    savesmadefromoutsidebox = models.IntegerField(blank=True, null=True)
    savesfrompenalty = models.IntegerField(blank=True, null=True)
    catches = models.IntegerField(blank=True, null=True)
    punches = models.IntegerField(blank=True, null=True)
    drops = models.IntegerField(blank=True, null=True)
    crossesnotclaimed = models.IntegerField(blank=True, null=True)
    gkdistribution = models.IntegerField(blank=True, null=True)
    gksuccessfuldistribution = models.IntegerField(blank=True, null=True)
    gkunsuccessfuldistribution = models.IntegerField(blank=True, null=True)
    cleansheets = models.IntegerField(blank=True, null=True)
    teamcleansheet = models.IntegerField(blank=True, null=True)
    errorleadingtogoal = models.IntegerField(blank=True, null=True)
    errorleadingtoattempt = models.IntegerField(blank=True, null=True)
    challengelost = models.IntegerField(blank=True, null=True)
    shotsonconceded = models.IntegerField(blank=True, null=True)
    shotsonconcededinsidebox = models.IntegerField(blank=True, null=True)
    shotsonconcededoutsidebox = models.IntegerField(blank=True, null=True)
    positioninformation = models.IntegerField(blank=True, null=True)
    turnovers = models.IntegerField(blank=True, null=True)
    dispossessed = models.IntegerField(blank=True, null=True)
    bigchances = models.IntegerField(blank=True, null=True)
    bigchancesfaced = models.IntegerField(blank=True, null=True)
    passforward = models.IntegerField(blank=True, null=True)
    passbackward = models.IntegerField(blank=True, null=True)
    passleft = models.IntegerField(blank=True, null=True)
    passright = models.IntegerField(blank=True, null=True)
    unsuccessfulballtouch = models.IntegerField(blank=True, null=True)
    successfulballtouch = models.IntegerField(blank=True, null=True)
    takeonsoverrun = models.IntegerField(blank=True, null=True)
    touchesopenplayfinalthird = models.IntegerField(blank=True, null=True)
    touchesopenplayoppbox = models.IntegerField(blank=True, null=True)
    touchesopenplayoppsixyards = models.IntegerField(blank=True, null=True)
    team1 = models.CharField(max_length=40, blank=True, null=True)
    team2 = models.CharField(max_length=40, blank=True, null=True)
    shot_eff = models.FloatField(blank=True, null=True)
    passes_eff = models.FloatField(blank=True, null=True)
    tackle_eff = models.FloatField(blank=True, null=True)
    dribble_eff = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actions'
        unique_together = (('playerid', 'matchid'),)


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


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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


class KpopIdols(models.Model):
    stage_name = models.CharField(max_length=50, blank=True, null=True)
    full_name = models.CharField(max_length=50, blank=True, null=True)
    korean_name = models.CharField(max_length=50, blank=True, null=True)
    k_stage_name = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField()
    k_group = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    birthplace = models.CharField(max_length=50, blank=True, null=True)
    other_group = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kpop_idols'


class Matches(models.Model):
    matchid = models.IntegerField(primary_key=True)
    teamhomeid = models.ForeignKey('Teams', models.DO_NOTHING, related_name='teamhomeid', db_column='teamhomeid', blank=True, null=True)
    teamawayid = models.ForeignKey('Teams', models.DO_NOTHING, related_name='teamawayid', db_column='teamawayid', blank=True, null=True)
    teamhomeformation = models.IntegerField(blank=True, null=True)
    teamawayformation = models.IntegerField(blank=True, null=True)
    resultofteamhome = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'matches'


class Players(models.Model):
    playerid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'players'


class Teams(models.Model):
    teamid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'teams'
