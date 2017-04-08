from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
import uuid

# Create your views here.

#def index(request):
#    return render(request, 'mmw/index.html', {})


class IndexView(TemplateView):
    template_name = "mmw/index.html"


class LoginView(TemplateView):
    template_name = "mmw/register_after.html"

    def post(self, request):
        print("you already upload details")
        print("username" + request.POST["name"])
        print("email" + request.POST["email"])
        name = request.POST["name"]
        email = request.POST['email']
        instance = models.UserInfo.objects.filter(email=email).first()
        if email == '' or name == '':
            return render(request, "mmw/index.html", {"emailusernamenone": True})
        if instance:
            if instance.name == name:
                print("correct username and email")
                user = instance.user
            else:
                print("wrong username")
                return render(request, "mmw/index.html", {"error": True})
        else:
            print("you are new user")
            user = User.objects.create_user(username=uuid.uuid4().hex[0:10])
            print("user created")
            instance = models.UserInfo.objects.create(user=user, name=name, email=email)
            print("info has been saved id: %d" %instance.id)
        instance2 = models.WhoIAm.objects.filter(user=user).first()
        login(request, user)
        return render(request, "mmw/whoiam.html", {"whoiam": instance2, "userinfo": instance})


class RegisterView(TemplateView):
    template_name = "mmw/index.html"

    def post(self, request):
        print("you uploaded username and email")
        print("username" + request.POST["name"])
        print("email" + request.POST["email"])
        name = request.POST["name"]
        email = request.POST["email"]
        if email == '':
            return render(request, "mmw/index.html", {"emailnone": True})
        instance = models.UserInfo.objects.filter(email=email).first()
        if instance:
            print("this email has been registered")
            return render(request, "mmw/index.html", {"registered": True})
        else:
            print("allow to use this email")
            user = User.objects.create_user(username=uuid.uuid4().hex[0:10])
            print("user created")
            instance = models.UserInfo.objects.create(user=user, name=name, email=email)
            print("information has been saved id: %d" %instance.id)
            return render(request, "mmw/index.html", {"success": True})


class UserInfoView(LoginRequiredMixin, TemplateView):
    template_name = "mmw/userinfo.html"
    login_url = "/"


class WhoIAmView(LoginRequiredMixin, TemplateView):
    login_url = "/"
    template_name = "mmw/register_after.html"

    def get(self, request):
        whoiam, created = models.WhoIAm.objects.get_or_create(user=request.user)
        print(whoiam.text1)
        return render(request, "mmw/whoiam.html", {"whoiam": whoiam})

    def post(self, request):
        print("你上传了个人信息")
        text1 = request.POST["text1"]
        text2 = request.POST["text2"]
        text3 = request.POST["text3"]
        text4 = request.POST["text4"]
        print(text1)
        instance = models.WhoIAm.objects.filter(user=request.user).first()
        if instance is not None:
            instance.text1 = text1
            instance.text2 = text2
            instance.text3 = text3
            instance.text4 = text4
            instance.save()
            return render(request, "mmw/communication.html", {})
        else:
            whoiam = models.WhoIAm.objects.create(user=request.user, text1=text1, text2=text2, text3=text3, text4=text4)
            whoiam.save()
            return render(request, "mmw/communication.html", {})


class ImportanceView(LoginRequiredMixin, TemplateView):
    login_url = "/"
    template_name = "mmw/importance.html"


class communication(LoginRequiredMixin, TemplateView):
    template_name = "mmw/communication.html"
    login_url = "/"

    def get(self, request):
        communication, created = models.Communication.objects.get_or_create(user=request.user)
        return render(request, "mmw/communication.html", {"communication": communication})

    def post(self, request):
        print("你上传了个人信息")
        text1 = request.POST["text1"]
        text2 = request.POST["text2"]
        text3 = request.POST["text3"]
        text4 = request.POST["text4"]
        print(text1)
        instance = models.Communication.objects.filter(user=request.user).first()
        if instance is not None:
            instance.text1 = text1
            instance.text2 = text2
            instance.text3 = text3
            instance.text4 = text4
            instance.save()
            return render(request, "mmw/importance.html", {})
        else:
            communication = models.Communication.objects.create(user=request.user, text1=text1, text2=text2, text3=text3, text4=text4)
            communication.save()
            return render(request, "mmw/importance.html", {})


class DailyactivityView(TemplateView):
    template_name = "mmw/dailyactivity.html"


class FellingView(TemplateView):
    template_name = "mmw/whoiam.html"


class LogoutView(TemplateView):
    template_name = "mmw/index.html"
    def get(self, request):
        logout(request)
        return render(request, "mmw/index.html", {"logout": True})


class MyHomeView(TemplateView):
    template_name = "mmw/myhome.html"


class ActivityView(TemplateView):
    template_name = "mmw/activity.html"


class MyDailyActivityView(TemplateView):
    template_name = "mmw/mydailyactivity.html"


class SupportsView(TemplateView):
    template_name = "mmw/supports.html"


class WeeklySupportView(TemplateView):
    template_name = "mmw/weeklysupport.html"


class BaseView(TemplateView):
    template_name = "base.html"

class ExtendView(TemplateView):
    template_name = "mmw/activity.html"