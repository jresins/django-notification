#coding:utf-8
from django.utils.translation import ugettext
from notification.backends import BaseBackend

class OnSiteBackend(BaseBackend):
    # from notification.models import Notice
    spam_sensitivity = 2

    def can_send(self, user, notice_type):
        can_send = super(OnSiteBackend, self).can_send(user, notice_type)
        # if can_send and notice_type.on_site:
        if can_send:
            return True
        return False

    def deliver(self, recipient, notice_type, extra_context):
        # TODO: require this to be passed in extra_context
        # Notice import should place here to avoid circular import
        # sender field should be removed due to system notice
        from notification.models import Notice

        notice = Notice.objects.create(recipient=recipient, notice_type=notice_type)

        context = self.default_context()
        context.update({
            "recipient": recipient,
            # "sender": sender,
            "notice_type": ugettext(notice_type.display),
            "notice": notice
        })
        context.update(extra_context)

        messages = self.get_formatted_messages(['notice.html'], notice_type.label, context)
        notice.message = messages['notice.html']
        notice.save()