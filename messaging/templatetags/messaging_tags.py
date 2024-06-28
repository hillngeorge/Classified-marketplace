from django import template
from messaging.models import Message

register = template.Library()

@register.simple_tag
def unread_messages_count(user):
    return Message.objects.filter(receiver=user, is_read=False).count()
