#_author_ = "allencth"

from django.conf.urls import url
from MMW import views


urlpatterns = [
    # url(r'^$', views.index, name="index"),
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^login/$', views.LoginView.as_view(), name="login"),
    url(r'^logout/$', views.LogoutView.as_view(), name="logout"),
    url(r'^userinfo/$', views.UserInfoView.as_view(), name="userinfo"),
    url(r'^whoiam/$', views.WhoIAmView.as_view(), name="whoiam"),
    url(r'^communication/$', views.communication.as_view(), name="communication"),
    url(r'^dailyactivity/$', views.DailyactivityView.as_view(), name="dailyactivity"),
    url(r'^myhome/$', views.MyHomeView.as_view(), name="myhome"),
    url(r'^activity/$', views.ActivityView.as_view(), name="activity"),
    url(r'^mydailyactivity/$', views.MyDailyActivityView.as_view(), name="mydailyactivity"),
    url(r'^supports/$', views.SupportsView.as_view(), name="support"),
    url(r'^weeklysupport/$', views.WeeklySupportView.as_view(), name="weeklysupport"),
    url(r'^register/$', views.RegisterView.as_view(), name="register"),
    url(r'^feeling/$', views.FellingView.as_view(), name="feeling"),
    url(r'^importance/$', views.ImportanceView.as_view(), name="importance"),
    # only for test
    url(r'^base/$', views.BaseView.as_view(), name="base"),
    url(r'^extend/$', views.ExtendView.as_view(), name="base"),
    url(r'^health/$', views.HealthView.as_view(),name="health"),
    url(r'^program/$', views.ProgramView.as_view(), name='program'),
    url(r'^equipment/$', views.EquipmentView.as_view(), name='equipment'),
    url(r'^short_term/$', views.ShortTermView.as_view(), name='short_term'),
    url(r'^long_term/$', views.LongTermView.as_view(), name='long_term'),
    url(r'^bucket_list/$', views.BucketListView.as_view(), name='bucket_list'),
    url(r'^mydream/$', views.MyDreamView.as_view(), name="mydream"),
    url(r'^wish/$', views.HowIWishView.as_view(), name="wish"),
    url(r'^congratulations/$', views.CongratulationsView.as_view(), name="congratulations"),
    url(r'^usermanual/$', views.UserManualView.as_view(), name="usermanual"),
]
