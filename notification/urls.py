from django.conf.urls import patterns, url

from notification.views import notice_settings, NoticeList


urlpatterns = patterns(
    "",
    url(r"^$", NoticeList.as_view(), name="notification_list"),
    url(r"^settings/$", notice_settings, name="notification_notice_settings"),
)
