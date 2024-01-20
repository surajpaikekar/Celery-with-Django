from django.core.mail import send_mail


def send_mail_without_celery():
    send_mail(
        "celery email body",
        "celery email msg body",
        "sender@gmail.com",
        ['reciever@gmail.com'],
        fail_silently=False
    )
    print("mail has successfully sent")
    return None