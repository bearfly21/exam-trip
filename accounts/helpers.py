from django.core.mail import send_mail
from django.conf import settings

def send_confirmation_token(email,token):
    path = f"http://127.0.0.1:8000/auth/confirm-email/{token}"
    message = f"Welcome to Hamsafar!\nPlease confirm your email by clicking the link below:\n{path}"

    try:
        send_mail(
            subject="hamsafar.tj",
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )
        return {
            'is_sent':True,
            'message':'Token sended successfully!'
        }
    except Exception as e:
        return {
            'is_sent':False,
            'message':str(e)
        }
    
