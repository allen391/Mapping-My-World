

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class WhoIAm(models.Model):
    user = models.OneToOneField(User)
    text1 = models.TextField("what is important to me?", max_length=128, null=True)
    text2 = models.TextField("What do i like about myself?", max_length=128, null=True)
    text3 = models.TextField("What do other people like about me?", max_length=64, null=True)
    text4 = models.TextField("How to best support me:", max_length=128,null=True)


class Communication(models.Model):
    user = models.OneToOneField(User)
    text1 = models.TextField("How i want to be involved:", max_length=128, null=True)
    text2 = models.TextField("Who i want to help me in my NDIS planning meeting", max_length=128, null=True)
    text3 = models.TextField("What my NDIS representative needs to know about how i communication:", max_length=128,null=True)
    text4 = models.TextField("Who makes the final decisions", max_length=128, null=True)
#
#
# class MyHome(models.Model):
#     user = models.OneToOneField(User)
#     text1 = models.TextField("What type of home i live in?", max_length=20)
#     text2 = models.TextField("The people i usually live with:", max_length=20)
#     text3 = models.TextField("Who helps me at home?", max_length=20)
#     text4 = models.TextField("What do they help me with？", max_length=128)
#     text5 = models.TextField("Do i use any equipment or other things to help me at home?", max_length=64)
#
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







