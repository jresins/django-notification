from django.contrib import admin

from notification.models import NoticeType, NoticeSetting, NoticeQueueBatch
from notification.models import Notice


class NoticeTypeAdmin(admin.ModelAdmin):
    list_display = ["label", "display", "description", "default"]


class NoticeSettingAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "notice_type", "medium", "send"]

class NoticeAdmin(admin.ModelAdmin):
    list_display = ['message', 'notice_type', 'recipient', 'unseen', 'added']
    raw_id_fields = ('recipient',)

admin.site.register(NoticeQueueBatch)
admin.site.register(NoticeType, NoticeTypeAdmin)
admin.site.register(NoticeSetting, NoticeSettingAdmin)
admin.site.register(Notice, NoticeAdmin)