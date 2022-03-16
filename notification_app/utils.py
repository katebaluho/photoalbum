from media_app.models import Media
from notification_app.models import Notification


def get_email_top_photo():
    emails = Media.objects.values_list('user__email').order_by('-counter_views')[:3]
    values = []
    [values.extend(element) for element in set(emails)]
    return values


def get_last_message_info():
    notice = Notification.objects.last()
    result = {'title': notice.title, 'message': notice.message}
    return result
