from django.dispatch import receiver
from django.contrib.auth.models import User
from accounts.tasks import welcome_text_email
from allauth.account.signals import user_signed_up

@receiver(user_signed_up)
def send_welcome_email(request, user, **kwargs):
    welcome_text_email(user.email, user.username)