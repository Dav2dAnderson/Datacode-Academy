from celery import shared_task

from django.core.mail import send_mail

# from courses.models import Notification

@shared_task
def welcome_text_email(email, username):
    subject = f"Assalomu alaykum, {username}"
    message = f"{username}, Siz muvaffaqiyatli ro'yxatdan o'tdingiz."
    send_mail(subject, message, "dav2danderson@gmail.com", [email])

