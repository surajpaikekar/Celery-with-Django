from celery import shared_task
from time import sleep


from django.core.mail import send_mail

@shared_task
def send_mail_through_celery():
    send_mail(
        "celery email body",
        "celery email msg body",
        "sender@gmail.com",
        ['reciever@gmail.com'],
        fail_silently=False
    )
    print("mail has successfully sent")
    return None

@shared_task
def sleepy(duration):
    sleep(duration)
    return None