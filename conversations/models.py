from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from core.models import TimeStampedModel

# Create your models here.


class Conversation(TimeStampedModel):
    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='users', blank=True, verbose_name=_('Participants'))

    def __str__(self) -> str:
        usernames = []
        for user in self.participants.all():
            usernames.append(user.username)
        return f"Conversation with {', '.join(usernames)} on {self.created.date()}"

    class Meta:
        verbose_name = _('Conversation')
        verbose_name_plural = _('Conversations')

    def count_messages(self):
        return self.messages.count()
    count_messages.short_description = _("Number of Messages")

    def count_participants(self):
        return self.participants.count()
    count_participants.short_description = _("Number of Participants")


class Message(TimeStampedModel):

    message = models.TextField(verbose_name=_('Message'))

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, verbose_name=_('User'))

    conversation = models.ForeignKey(
        Conversation, on_delete=models.CASCADE, verbose_name=_('Conversation'), related_name='messages')

    def __str__(self) -> str:
        return f"{self.user}: {self.message}"

    class Meta:
        verbose_name = _('Message')
        verbose_name_plural = _('Messages')
