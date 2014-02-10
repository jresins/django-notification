#coding:utf-8
#pull data such as the unseen notices for on site notification
from notification.models import Notice

def unseen_notices(request):
    """
    return a list of unseen notices for current user
    """
    if request.user.is_authenticated():
        qs = Notice.notices_for(request.user, unseen=True)
        return {'unseen_notices': qs}
    else:
        return {}

def unseen_notices_count(request):
    """
    return the count of unseen notices for current user
    """
    if request.user.is_authenticated():
        qs = Notice.unseen_count_for(request.user)
        return {'unseen_notices_count': qs}
    else:
        return {}