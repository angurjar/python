from django.conf import settings
from django.core.mail import send_mail
def send_account_acitivation_email(email,email_token):
    subject='your account needs to  be verified'
    email_from=settings.EMAIL_HOST_USER
    message=f'hi click on the activite your account https://127.0.0.1/activate/{email_token}'
    send_mail(subject,message,email_token,[email])