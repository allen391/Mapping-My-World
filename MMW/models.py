

from django.db import models
import json
from django.contrib.auth.models import User

# Create your models here.


class WhoIAm(models.Model):
    user = models.OneToOneField(User)
    text1 = models.TextField("what is important to me?", max_length=128)
    text2 = models.TextField("What do i like about myself?", max_length=128)
    text3 = models.TextField("What do other people like about me?", max_length=64)
    text4 = models.TextField("How to best support me:", max_length=128)

    class Meta:
            verbose_name = "Who I Am"
            verbose_name_plural = "Who I Am"

    @property
    def name(self):
        return self.user.userinfo.name

    def email(self):
        return self.user.userinfo.email


class WhoIAmHistory(models.Model):
    user = models.ForeignKey(User)
    text1 = models.TextField(max_length=128, null=True)
    text2 = models.TextField(max_length=128, null=True)
    text3 = models.TextField(max_length=128, null=True)
    text4 = models.TextField(max_length=128, null=True)
    time = models.DateTimeField(auto_now=True)

    class Meta:
            verbose_name = "WhoIAmHistory"
            verbose_name_plural = "WhoIAmHistory"

    @property
    def name(self):
        return self.user.userinfo.name

    def email(self):
        return self.user.userinfo.email


class Communication(models.Model):
    user = models.OneToOneField(User)
    text1 = models.TextField("How i want to be involved:", max_length=128)
    text2 = models.TextField("Who i want to help me in my NDIS planning meeting", max_length=128)
    text3 = models.TextField("What my NDIS representative needs to know about how i communication:", max_length=128)
    text4 = models.TextField("Who makes the final decisions", max_length=128)

    class Meta:
            verbose_name = "The way I communicate and make decisions"
            verbose_name_plural = "The way I communicate and make decisions"

    @property
    def name(self):
        return self.user.userinfo.name

    def email(self):
        return self.user.userinfo.email


class CommunicationHistory(models.Model):
    user = models.ForeignKey(User)
    text1 = models.TextField(max_length=128)
    text2 = models.TextField(max_length=128)
    text3 = models.TextField(max_length=128)
    text4 = models.TextField(max_length=128)
    time = models.DateTimeField(auto_now=True)

    @property
    def name(self):
        return self.user.userinfo.name

    def email(self):
        return self.user.userinfo.email


class Importance(models.Model):
    user = models.OneToOneField(User)
    my_family = models.TextField("How i want to be involved:", max_length=128)
    work_school = models.TextField("How i want to be involved:", max_length=128)
    very_close_top = models.TextField("Who i want to help me in my NDIS planning meeting", max_length=128)
    very_close_bottom = models.TextField("What my NDIS representative needs to know about how i communication:", max_length=128)
    very_close_left = models.TextField("Who makes the final decisions", max_length=128)
    very_close_right = models.TextField("Who makes the final decisions", max_length=128)
    friends = models.TextField("Who makes the final decisions", max_length=128)
    home_supporters = models.TextField("Who makes the final decisions", max_length=128)

    class Meta:
            verbose_name = "Important people to me"
            verbose_name_plural = "Important people to me"


class MyHome(models.Model):
    user = models.OneToOneField(User)
    text1 = models.TextField("What type of home i live in?", max_length=20)
    text2 = models.TextField("The people i usually live with:", max_length=20)
    text3 = models.TextField("Who helps me at home?", max_length=20)
    text4 = models.TextField("What do they help me with？", max_length=128)
    text5 = models.TextField("Do i use any equipment or other things to help me at home?", max_length=64)

    class Meta:
            verbose_name = "My Home"
            verbose_name_plural = "My Home"

    @property
    def name(self):
        return self.user.userinfo.name

    def email(self):
        return self.user.userinfo.email
# class


class UserInfo(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    # date = models.DateField(null=True, blank=True)
    whoiam = models.OneToOneField(WhoIAm, null=True)
    communication = models.OneToOneField(Communication, null=True)

    def __str__(self):
        return "%s " % self.user
    class Meta:
            verbose_name = "User Info"
            verbose_name_plural = "User Info"

def update_userinfo():
    for userinfo in UserInfo.objects.all():
        user = userinfo.user
        try:
            whoiam = user.whoiam
            userinfo.whoiam_id = whoiam.id
            userinfo.save()
            communication = user.communication
            userinfo.communication = communication.id
            communication.save()
        except:
            pass


class Program(models.Model):
    user = models.OneToOneField(User)
    data = models.TextField("My programs and therapy supports: ")

    class Meta:
            verbose_name = "My program and therapy supports"
            verbose_name_plural = "My program and therapy supports"

class Equipment(models.Model):
    user = models.OneToOneField(User)
    data = models.TextField("My programs and therapy supports: ")

    class Meta:
            verbose_name = "My equipment, aid or modification supports"
            verbose_name_plural = "My equipment, aid or modification supports"


class Wish(models.Model):
    user = models.OneToOneField(User)
    data = models.TextField("My wish:")

    class Meta:
            verbose_name = "How I wish my week looked"
            verbose_name_plural = "How I wish my week looked"


class Short_term(models.Model):
    user = models.OneToOneField(User)
    text = models.TextField("What would you like to achieve in the next 12months? ")

    class Meta:
            verbose_name = "My short term dreams and goals：next 12 months"
            verbose_name_plural = "My short term dreams and goals：next 12 months"

class Long_term(models.Model):
    user = models.OneToOneField(User)
    text = models.TextField("What would you like to achieve in the next five years? ")
    class Meta:
            verbose_name = "My long term dreams and goals: the future"
            verbose_name_plural = "My long term dreams and goals: the future"


class Bulk_list(models.Model):
    user = models.OneToOneField(User)
    text = models.TextField("If you had one ultimate wish, what would it be？")
    class Meta:
            verbose_name = "My ultimate bucket list"
            verbose_name_plural = "My ultimate bucket list"



class WeeklySupport(models.Model):
    user = models.OneToOneField(User)
    text = models.TextField("If you had one ultimate wish, what would it be？", default=json.dumps([]))


class Health(models.Model):
    user = models.OneToOneField(User)
    text = models.TextField("My health and wellbeing", default=json.dumps([]))
    class Meta:
            verbose_name = "My health and wellbeing"
            verbose_name_plural = "My health and wellbeing"


class Activity(models.Model):
    DATA = {
        'monday': {
            'morning': {
                "now": "",
                "working": "",
                "notworking": "",
            },
            'afternoon': {
                "now": "",
                "working": "",
                "notworking": "",
            },
            'evening': {
                "now": "",
                "working": "",
                "notworking": "",
            },
         },
        'tuesday': {
            'morning': {
                "now": "",
                "working": "",
                "notworking": "",
            },
            'afternoon': {
                "now": "",
                "working": "",
                "notworking": "",
            },
            'evening': {
                "now": "",
                "working": "",
                "notworking": "",
            },
         },
        'wednesday': {
            'morning': {
                "now": "",
                "working": "",
                "notworking": "",
            },
            'afternoon': {
                "now": "",
                "working": "",
                "notworking": "",
            },
            'evening': {
                "now": "",
                "working": "",
                "notworking": "",
            },
         },
        'thursday': {
            'morning': {
                "now": "",
                "working": "",
                "notworking": "",
            },
            'afternoon': {
                "now": "",
                "working": "",
                "notworking": "",
            },
            'evening': {
                "now": "",
                "working": "",
                "notworking": "",
            },
         },
        'friday': {
            'morning': {
                "now": "",
                "working": "",
                "notworking": "",
            },
            'afternoon': {
                "now": "",
                "working": "",
                "notworking": "",
            },
            'evening': {
                "now": "",
                "working": "",
                "notworking": "",
            },
         },
        'saturday': {
            'morning': {
                "now": "",
                "working": "",
                "notworking": "",
            },
            'afternoon': {
                "now": "",
                "working": "",
                "notworking": "",
            },
            'evening': {
                "now": "",
                "working": "",
                "notworking": "",
            },
         },
        'sunday': {
            'morning': {
                "now": "",
                "working": "",
                "notworking": "",
            },
            'afternoon': {
                "now": "",
                "working": "",
                "notworking": "",
            },
            'evening': {
                "now": "",
                "working": "",
                "notworking": "",
            },
         },
    }
    user = models.OneToOneField(User)
    data = models.TextField("My Activity", default=json.dumps(DATA))
    do = models.TextField(default="")
    havenotdo = models.TextField(default="")

    class Meta:
            verbose_name = "My daily activities"
            verbose_name_plural = "My daily activities"
