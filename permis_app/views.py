from distutils.command.config import config
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SocieteForm ,User_appForm ,EditProfileForm
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .decorators import notLoggedUsers,allowedUsers,forDirectionStrategiquesPolitiquesEmploi,forDirectionGeneralTravail,forDirectionGeneralEmploi,forSociete
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from permis import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from . tokens import generateToken

def incoherent(request,id_user,id_n,id_d):
    l = Societe.objects.get(id=id_user)
    if request.method == 'POST':
        msg = request.POST['msg']
        nt = Notification(id_user_id=l.id_user_id,sujet="incoherent",description=msg,id_dem_id=id_d)
        nt.save()
    return redirect('test')

def exploiter(request,id_soc,id_dem):
    b = User_app.objects.get(type_user='b')
    config = Demande.objects.get(id=id_dem)
    config.statut='a'
    config.save()
    nt = Notification(id_user_id=b.id,sujet="exploiter",description="",id_soc=id_soc,id_dem_id=id_dem)
    nt.save()
    messages.success(request,"L'operation a été couronnée de succès")
    return redirect('test')
# def logi_n(request):
#     if not request.user.is_authenticated:
#         if request.method == 'POST':
#             nom = request.POST['username']
#             mots_pass = request.POST['password']
#             user = authenticate(request,username=nom,password=mots_pass)
#             if user is not None:
#                 if user.is_staff == True:
#                     if user.type_user == 'a':
#                         login(request,user)
#                         return redirect('test')
#                     elif user.type_user == 'd':
#                         login(request,user)
#                         return redirect('homme_u')
#                     elif user.type_user == 'b':
#                         login(request,user)
#                         return redirect('homme_b')
#                     elif user.type_user == 'c':
#                         login(request,user)
#                         return redirect('homme_c')
#                     else:
#                         messages.error(request, "vous n'avez pas le droit ")  
#                         return redirect('login') 
#                 else:
#                     messages.error(request, "vous n'avez pas confirmé votre email")  
#                     return redirect('login')  
#             else:
#                 messages.error(request, "n'exist pas")
#                 return redirect('login')         
#         else:    
#             return render(request,'type_a/pages/login.html')  
#     else :
#         return render(request,'type_a/pages/login.html')
def logi_n(request):
        if request.method == 'POST':
            nom = request.POST['username']
            mots_pass = request.POST['password']
            user = authenticate(request,username=nom,password=mots_pass)
            group = None
            if user is not None:
                        login(request,user)
            if request.user.groups.exists():
               group =  request.user.groups.all()[0].name
            if group == 'Groupe_B':
               return redirect('DirectionGeneralTravail')
            if group == 'Groupe_A':
                return redirect('DirectionStrategiquesPolitiquesEmploi')
            if group == 'Groupe_C':
                return redirect('DirectionGeneralEmploi')
            if group == 'Groupe_D':
                return redirect('Societe')
            else:
                messages.info(request, "vous n'avez pas le droit ")  
        context = {}
        return render(request,'Auth/login.html',context) 
def logou_t(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        add_Societe = SocieteForm(request.POST,request.FILES)
        n = request.POST['Nom']  
        m = request.POST['username'] 
        add_User = User_appForm(request.POST,request.FILES) 
        if add_User.is_valid():
            user=add_User.save()
            group = Group.objects.get(name="Groupe_D")
            user.groups.add(group) 
        id_user = User_app.objects.get(username=m) 
        id_u = id_user.id
        if add_Societe.is_valid():
            add_Societe.save()
        Societe.objects.filter(Nom=n).update(id_user=id_u)
        b = User_app.objects.get(type_user='a')
        l = Societe.objects.get(Nom=n)
        nt = Notification(id_user=b,sujet=f"demande du societe : {n}",description="societe",id_soc=l.id)
        nt.save()
        my_user = User_app.objects.get(username=m)
        return redirect('login')  
    # userp = User_app.objects.all()
    # a = request.user 
    # user = User_app.objects.get(username=a)
    # u = user.id
    context = {
        # 'userp' : userp,
        # 'ph' : user.photo,
        # 'nb_ms' : Notification.objects.filter(status=False,id_user_id=u).count(),
        # 'ms' : Notification.objects.filter(status=False,id_user_id=u),
        'User' : User_appForm(),
        'Societe' : SocieteForm(),
    }
    return render(request,'Auth/register.html',context)
@forDirectionStrategiquesPolitiquesEmploi
def test(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        a = request.user 
        user = User_app.objects.get(username=a)
        u = user.id
        userp = User_app.objects.all()
        socv = Societe.objects.filter(valide=True).count()
        socn = Societe.objects.filter(valide=False).count()
        soc = Societe.objects.all().count()
        dem = Demande.objects.all().count()
        
        
        context = {
            'socv' : socv,
            'socn' : socn,
            'soc' : soc,
            'dem' : dem,
            'userp' : userp,
            'ph' : user.photo,
            'nb_ms' : Notification.objects.filter(status=False,id_user_id=u).count(),
            'ms' : Notification.objects.filter(status=False,id_user_id=u),
        }
        return render(request,'type_a/pages/test.html',context)

def detaill(request,id_user,id_n,id_d):
    # config = Notification.objects.get(id=id_n)
    # config.status=True
    # config.save()
    sc = Societe.objects.get(id=id_user)
    if request.method == 'POST':
        msg = request.POST['msg']
        nt = Notification(id_user_id=sc.id_user_id,sujet="incomplet",description=msg,id_dem_id=id_d)
        nt.save()
        # my_sc = Societe.objects.get(id=id_user)
        # # soc = Societe.objects.get(id=id_user)
        # # nt = Notification(id_user_id=soc.id_user,sujet="incomplet",description=msg,id_soc=id_user,id_dem_id=id_d)
        # subject = "ERREUR , Incomplet"
        # message = "Bienvenue "+ my_sc.Nom + "\n merci d'avoir choisi le site.\n "+msg
        # from_email = settings.EMAIL_HOST_USER
        # to_list = [my_sc.gmail]
        # send_mail(subject, message, from_email, to_list, fail_silently=False)
        # return redirect('test')
    
    scs = Societe.objects.filter(id=id_user)
    aa = sc.id_user_id
    bb = sc.id
    a = request.user 
    user = User_app.objects.get(username=a)
    userr = User_app.objects.get(id=aa)
    u = user.id
    v = Notification.objects.get(id=id_n)
    if id_d == "None":
        context = {
            'users' : user.photo,
            'ph' : user.photo,
            'idt' : aa,
            'id_sc' : bb,
            'id_user' : id_user,
            'v' : id_n,
            'detaill' : scs,
            'nb_ms' : Notification.objects.filter(status=False,id_user_id=u).count(),
            'ms' : Notification.objects.filter(status=False,id_user_id=u),
        }
    else:
        dem = Demande.objects.get(id=id_d)
        trs = Travailleur.objects.filter(numTel=dem.numTel).exists()
        if dem.TypeDemande == 'renouvellement':
            if trs :
                mes = "Valider"
            else:
                mes = "Non valider"
        else:
            if trs :
                mes = "Non valider"
            else:
                mes = "Valider"
        d = Demande.objects.filter(id=id_d)
        context = {
            'mes':mes,
            'users' : user.photo,
            'ph' : user.photo,
            'idt' : aa,
            'id_sc' : bb,
            'dem' : d,
            'id_user' : id_user,
            'v' : id_n,
            'vd' : id_d,
            'nb_ms' : Notification.objects.filter(status=False,id_user_id=u).count(),
            'ms' : Notification.objects.filter(status=False,id_user_id=u),
        }
    
    if v.description == 'permis':
        return render(request,'type_a/pages/detail.html',context)
    elif v.description == 'societe':
        return render(request,'type_a/pages/detaill.html',context)
    else:
        return render(request,'type_a/pages/test.html',context)
        

def valide(request,id_u,id_sc):
    my_user = User_app.objects.get(id=id_u)
    my_sc = Societe.objects.get(id=id_sc)
    subject = "Bienvenue sur Permis de travaill"
    message = "Bienvenue "+ my_sc.Nom + "\n merci d'avoir choisi le site.\n Pour demander des permis, vous devez confirmer votre e-mail.\n merci \n\n\n ahmedou programmeur"
    from_email = settings.EMAIL_HOST_USER
    to_list = [my_sc.gmail]
    send_mail(subject, message, from_email, to_list, fail_silently=False)
    current_site = get_current_site(request) 
    email_suject = "confirmez votre email , Connectez-vous !"
    messageConfirm = render_to_string("emailConfimation.html", {
        'name': my_user.username,
        'domain':current_site.domain,
        'uid':urlsafe_base64_encode(force_bytes(my_user.pk)),
        'token': generateToken.make_token(my_user)
    })       
    email = EmailMessage(
        email_suject,
        messageConfirm,
        settings.EMAIL_HOST_USER,
        [my_user.email]
    )
    email.fail_silently = False
    email.send()
    return redirect('test')

def incomplet(request,id_u):
    my_user = User_app.objects.get(id=id_u)
    messages.success(request, 'Your account has been successfully created. we have sent you an email You must comfirm in order to activate your account.')
    subject = "Welcome to django-application donaldPro"
    message = "Welcome "+ my_user.username + "\n thank for chosing Dprogrammeur website for test login.\n To order login you need to comfirm your email account.\n thanks\n\n\n donald programmeur"
    from_email = settings.EMAIL_HOST_USER
    to_list = [my_user.email]
    send_mail(subject, message, from_email, to_list, fail_silently=False)
    current_site = get_current_site(request) 
    email_suject = "confirm your email DonaldPro Django Login!"
    messageConfirm = render_to_string("emailConfimation.html", {
        'name': my_user.username,
        'domain':current_site.domain,
        'uid':urlsafe_base64_encode(force_bytes(my_user.pk)),
        'token': generateToken.make_token(my_user)
    })       
    email = EmailMessage(
        email_suject,
        messageConfirm,
        settings.EMAIL_HOST_USER,
        [my_user.email]
    )
    email.fail_silently = False
    email.send()
    return render(request,'type_a/pages/test.html')

def nactivate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        my_user = User_app.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        my_user = None
    messages.success(request, "L'activation a échoué, veuillez réessayer")
    return redirect('login')
    
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        my_user = User_app.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        my_user = None
    if my_user is not None and generateToken.check_token(my_user, token):
        my_user.is_staff = True    
        soc = Societe.objects.get(id_user_id=my_user.id)
        soc.valide = True
        soc.save()
        my_user.save()
        messages.success(request, "Votre compte est activé vous pouvez vous connecter en remplissant le formulaire ci-dessous.")
        return redirect("login")
    else:
        messages.success(request, "L'activation a échoué, veuillez réessayer")
        return redirect('login')

def view_profile(request):
    a = request.user 
    user = User_app.objects.get(username=a)
    u = user.id
    args = {
        'user': request.user,
        'ph' : user.photo,
        'nb_ms' : Notification.objects.filter(status=False,id_user_id=u).count(),
        'ms' : Notification.objects.filter(status=False,id_user_id=u),
    }
    if user.type_user == 'a':
        return render(request, 'type_a/pages/profile.html',args)
    elif user.type_user == 'b':
        return render(request, 'type_b/pages/profile.html',args)
    elif user.type_user == 'c':
        return render(request, 'type_c/pages/profile.html',args)
    elif user.type_user == 'd':
        return render(request, 'user_soc/pages/profile.html',args)
    else :
        logout(request)
        return redirect('login')


def edit_profile(request):
    a = request.user 
    user = User_app.objects.get(username=a)
    u = user.id
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES,instance=request.user)
        
        if form.is_valid():
            form.save()
            args = {
                'ph' : user.photo,
                'nb_ms' : Notification.objects.filter(status=False,id_user_id=u).count(),
                'ms' : Notification.objects.filter(status=False,id_user_id=u),
            }
            if user.type_user == 'a':
                return render(request, 'type_a/pages/profile.html',args)
            elif user.type_user == 'b':
                return render(request, 'type_b/pages/profile.html',args)
            elif user.type_user == 'c':
                return render(request, 'type_c/pages/profile.html',args)
            elif user.type_user == 'd':
                return render(request, 'user_soc/pages/profile.html',args)
            else :
                logout(request)
                return redirect('login') 
        
    else:
        form = EditProfileForm(instance=request.user)
        args = {
            'form':form,
            'ph' : user.photo,
            'nb_ms' : Notification.objects.filter(status=False,id_user_id=u).count(),
            'ms' : Notification.objects.filter(status=False,id_user_id=u),
        }
        if user.type_user == 'a':
            return render(request, 'type_a/pages/edit_profile.html',args)
        elif user.type_user == 'b':
            return render(request, 'type_b/pages/edit_profile.html',args)
        elif user.type_user == 'c':
            return render(request, 'type_c/pages/edit_profile.html',args)
        elif user.type_user == 'd':
            return render(request, 'user_soc/pages/edit_profile.html',args)
        else :
            logout(request)
            return redirect('login') 

def change_password(request):
    a = request.user 
    user = User_app.objects.get(username=a)
    u = user.id
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            args = {
                'ph' : user.photo,
                'nb_ms' : Notification.objects.filter(status=False,id_user_id=u).count(),
                'ms' : Notification.objects.filter(status=False,id_user_id=u),
            }
            if user.type_user == 'a':
                return render(request, 'type_a/pages/profile.html',args)
            elif user.type_user == 'b':
                return render(request, 'type_b/pages/profile.html',args)
            elif user.type_user == 'c':
                return render(request, 'type_c/pages/profile.html',args)
            elif user.type_user == 'd':
                return render(request, 'user_soc/pages/profile.html',args)
            else :
                logout(request)
                return redirect('login')              
    else:
        form = PasswordChangeForm(user=request.user)
        args = {
            'form': form,
            'ph' : user.photo,
            'nb_ms' : Notification.objects.filter(status=False,id_user_id=u).count(),
            'ms' : Notification.objects.filter(status=False,id_user_id=u),
        }
        if user.type_user == 'a':
            return render(request, 'type_a/pages/change_password.html',args)
        elif user.type_user == 'b':
            return render(request, 'type_b/pages/change_password.html',args)
        elif user.type_user == 'c':
            return render(request, 'type_c/pages/change_password.html',args)
        elif user.type_user == 'd':
            return render(request, 'user_soc/pages/change_password.html',args)
        else :
            logout(request)
            return redirect('login') 
    