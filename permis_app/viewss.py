from django.shortcuts import render, redirect, get_object_or_404

from permis_app.decorators import forSociete
from .forms import SocieteForm ,User_appForm, DmandeForm
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.db.models import Max
 
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from permis import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from . tokens import generateToken

# Create your views here.
@forSociete
def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        a = request.user 
        user = User_app.objects.get(username=a)
        u = user.id
        context = {
            'ph' : user.photo,
            'nb_ms' : Notification.objects.filter(status=False,id_user=u).count(),
            'ms' : Notification.objects.filter(status=False,id_user=u),
        }
        return render(request,'user_soc/pages/test.html',context)


def voir(request):
    if request.method == 'POST':
        idd = request.POST['op']  
        a = request.user 
        user = User_app.objects.get(username=a)
        u = user.id
        dem = Demande.objects.filter(id=idd)
        context = {
            'ph' : user.photo,
            'dem' : dem,
            'nb_ms' : Notification.objects.filter(status=False,id_user=u).count(),
            'ms' : Notification.objects.filter(status=False,id_user=u),
        }
        return render(request,'user_soc/pages/registerr.html',context)
    return redirect('homme_u') 

def renouvel(request):
    if request.method == 'POST':
        a = request.user 
        b = User_app.objects.get(username=a)
        c = Societe.objects.get(id_user_id=b.id)
        codei = 200000 if Demande.objects.count()== 0 else Demande.objects.aggregate(maxx=Max('codePermis'))["maxx"]+1
        dem = DmandeForm(request.POST,request.FILES)
        n = request.POST['idd']  
        k = Demande.objects.get(id=n)
        demand = Demande(TypeDemande='renouvellement',denomination=k.denomination,siege=k.siege,numIMM=k.numIMM,
        nomPrenom=k.nomPrenom,Nationalite=k.Nationalite,Employeur=c.Nom,lieu_nais=k.lieu_nais,
        cnss=k.cnss,numPass=k.numPass,id_soc_id=c.id,dateExpPass=k.dateExpPass,
        email=k.email,codePermis=codei,numTel=k.numTel,dateNaissance=k.dateNaissance,
        descPoste=k.descPoste,expose=k.expose,photo=k.photo,TypePermis=k.TypePermis)           
        demand.save()
        sv = Demande.objects.get(codePermis=codei)
        s = User_app.objects.get(type_user='a')
        nt = Notification(id_user_id=s.id,sujet=f"renouvellement du permis : {a}",description="permis",id_soc=c.id,id_dem_id=sv.id)
        nt.save()
        messages.success(request,'Demande envoyée avec succès')
        return redirect('homme_u') 
    return redirect('homme_u') 
def registerr(request):
    if request.method == 'POST':
        codei = 200000 if Demande.objects.count()== 0 else Demande.objects.aggregate(maxx=Max('codePermis'))["maxx"]+1
        dem = DmandeForm(request.POST,request.FILES)
        n = request.POST['numIMM']  
        if dem.is_valid():
            co = dem.save() 
            co.codePermis = codei
            co.save()
            a = request.user 
            b = User_app.objects.get(username=a)
            c = Societe.objects.get(id_user_id=b.id)
            config = Demande.objects.get(numIMM=n)
            config.id_soc_id=c.id
            config.Employeur=c.Nom
            config.save()
            demm = Demande.objects.get(numIMM=n)
            s = User_app.objects.get(type_user='a')
            nt = Notification(id_user_id=s.id,sujet=f"demande du permis : {a}",description="permis",id_soc=c.id,id_dem_id=demm.id)
            nt.save()
            messages.success(request,'Demande envoyée avec succès')
            return redirect('homme_u') 
    a = request.user 
    user = User_app.objects.get(username=a)
    u = user.id
    socc = Societe.objects.filter(id_user=u).first()
    demande = Demande.objects.filter(id_soc_id=socc.id,TypeDemande='Nouvaux')
    demande1 = Demande.objects.all()
    
    context = {
        'ph' : user.photo,
        'id' : socc.id,
        'dem':demande,
        'dem1':demande1,
        'nb_ms' : Notification.objects.filter(status=False,id_user=u).count(),
        'ms' : Notification.objects.filter(status=False,id_user=u),
        'Dmande' : DmandeForm(),
    }
    return render(request,'user_soc/pages/register.html',context)
def detail(request,id_n,id_d):
    nt = Notification.objects.get(id=id_n)
    dem = Demande.objects.filter(id=id_d)
    a = request.user 
    user = User_app.objects.get(username=a)
    u = user.id
    context = {
        'nb_ms' : Notification.objects.filter(status=False,id_user=u).count(),
        'ms' : Notification.objects.filter(status=False,id_user=u),
        # 'Dmande' : DmandeForm(),
        'dem':dem,
        'nt' :nt,
    }
    return render(request,'user_soc/pages/detaill.html',context)

def reponse(request,id_n,id_d):
    dem_id = Demande.objects.get(id=id_d)
    if request.method == 'POST':
        book_save = DmandeForm(request.POST,request.FILES,instance=dem_id)
        if book_save.is_valid():
            book_save.save()
            s = User_app.objects.get(type_user='a')
            nt = Notification(id_user_id=s.id,sujet="completion du demande permis ",description="permis",id_soc=dem_id.id_soc_id,id_dem_id=id_d)
            nt.save()
            return redirect('homme_u')
    else:
        dem_modifier = DmandeForm(instance=dem_id)
        nt = Notification.objects.get(id=id_n)
        dem = Demande.objects.filter(id=id_d)
        a = request.user 
        user = User_app.objects.get(username=a)
        u = user.id
        context = {
            'ph' : user.photo,
            'nt' : nt,
            'dem' : dem,
            'Dmande' : dem_modifier,
            'nb_ms' : Notification.objects.filter(status=False,id_user=u).count(),
            'ms' : Notification.objects.filter(status=False,id_user=u),
            # 'Dmande' : DmandeForm(),
        }
        return render(request,'user_soc/pages/reponce.html',context)
# def detaills(request,id_user):
#     # if request.method == 'POST':
#     #     msg = request.POST['msg']
#     #     my_sc = Societe.objects.get(id=id_user)
#     #     subject = "ERREUR , Incomplet"
#     #     message = "Bienvenue "+ my_sc.Nom + "\n merci d'avoir choisi le site.\n "+msg
#     #     from_email = settings.EMAIL_HOST_USER
#     #     to_list = [my_sc.gmail]
#     #     send_mail(subject, message, from_email, to_list, fail_silently=False)
#     #     return redirect('test')
#     sc = Societe.objects.get(id=id_user)
#     scs = Societe.objects.filter(id=id_user)
#     aa = sc.id_user_id
#     bb = sc.id
#     user = User_app.objects.get(type_user='d')
#     u = user.id
#     context = {
#         'detaill' : scs,
#         'idt' : aa,
#         'id_sc' : bb,
#         'id_user' : id_user,
#         'nb_ms' : Notification.objects.filter(status=False,id_user_id=u).count(),
#         'ms' : Notification.objects.filter(status=False,id_user_id=u),
#     }
#     return render(request,'user_soc/pages/detaill.html',context)