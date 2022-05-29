from datetime import date
from time import time
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
import datetime
from .models import *
     

# @receiver(user_logged_in)
# def log_user_login(sender, request, user, **kwargs):
#     nt = Hystorique(Nom=user.username,datecon=now.strftime("%d-%m-%y %H:%M:%S"),url=request.META.get('HTTP_REFERER'))
#     nt.save()


# @receiver(user_login_failed)
# def log_user_login_failed(sender, credentials, request, **kwargs):
#     nt = Hystorique(Nom=credentials.get('username'),datedecon=now.strftime("%d-%m-%y %H:%M:%S"),url=request.META.get('HTTP_REFERER'))
#     nt.save()

@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    now = datetime.datetime.now()
    userc = User_app.objects.get(username=user.username)
    nt = Hystorique(id_user_id=userc.id,Nom=user.username,type_user=userc.type_user,datecon=user.last_login.strftime("%d-%m-%y %H:%M:%S"),datedecon=now.strftime("%d-%m-%y %H:%M:%S"))
    nt.save()