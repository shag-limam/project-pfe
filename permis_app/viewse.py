from django.shortcuts import render, redirect, get_object_or_404

from permis_app.decorators import forDirectionGeneralEmploi, forDirectionGeneralTravail
from .forms import SocieteForm ,User_appForm,DmandevForm
from .models import *
from django.contrib.auth import authenticate,login,logout

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
@forDirectionGeneralTravail
def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        a = request.user 
        user = User_app.objects.get(username=a)
        aviss = Demande.objects.all()
        soc = Societe.objects.all()
        notif = Notification.objects.filter(id_user_id=user.id)
        con = 0
        con1 = 0
        con2 = 0
        for w in notif:
            for n in aviss:
                if n.avis == None:
                    if w.id_dem_id == n.id:
                        con = con + 1
                elif n.avis == "":
                    if w.id_dem_id == n.id:
                        con1 = con1 + 1
                else:
                    if w.id_dem_id == n.id:
                        con2 = con2 + 1
        u = user.id
        context = {
            'ph' : user.photo,
            'con' : con,
            'con1' : con1,
            'con2' : con2,
            'nb_ms' : Notification.objects.filter(status=False,id_user=u).count(),
            'ms' : Notification.objects.filter(status=False,id_user=u),
        }
        return render(request,'type_b/pages/test.html',context)
    
def detail(request,id_user,id_n,id_d):
    # config = Notification.objects.get(id=id_n)
    # config.status=True
    # config.save()
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        a = request.user 
        user = User_app.objects.get(username=a)
        aviss = Demande.objects.all()
        soc = Societe.objects.all()
        notif = Notification.objects.filter(id_user_id=user.id)
        con = 0
        con1 = 0
        con2 = 0
        for w in notif:
            for n in aviss:
                if n.avis == None:
                    if w.id_dem_id == n.id:
                        con = con + 1
                elif n.avis == "":
                    if w.id_dem_id == n.id:
                        con1 = con1 + 1
                else:
                    if w.id_dem_id == n.id:
                        con2 = con2 + 1
        u = user.id
        context = {
            'ph' : user.photo,
            'con' : con,
            'con1' : con1,
            'con2' : con2,
            'nb_ms' : Notification.objects.filter(status=False,id_user=u).count(),
            'ms' : Notification.objects.filter(status=False,id_user=u),
        }
    d = Demande.objects.filter(id=id_d)
    sc = Societe.objects.get(id=id_user)
    aa = sc.id_user_id
    if request.method == 'POST':
        msg = request.POST['msg']
        config = Demande.objects.get(id=id_d)
        config.avis=msg
        config.statut='b'
        config.save()
        s = User_app.objects.get(type_user='c')
        ss = s.id
        nt = Notification(id_user_id=ss,sujet="avis sur la demande",description="",id_soc=id_user,id_dem_id=id_d)
        nt.save()
        messages.success(request,"L'operation a été couronnée de succès")
        # return redirect('homme_b')
        return render(request,'type_b/pages/test.html',context)

    scs = Societe.objects.filter(id=id_user)
    bb = sc.id
    a = request.user 
    userr = User_app.objects.get(id=aa)
    user = User_app.objects.get(username=a)
    u = user.id
    v = Notification.objects.get(id=id_n)
    d = Demande.objects.filter(id=id_d)
    context = {
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
    return render(request,'type_b/pages/detail.html',context)


# user-C
@forDirectionGeneralEmploi
def indexc(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        a = request.user 
        user = User_app.objects.get(username=a)
        u = user.id
        trv = Travailleur.objects.all()
        per = Permis.objects.filter(renouveler=True)
        cpt = 0
        i = 0
        iid = 0
        for m in trv:
            cpt+=1
            iid = 0
            for n in per:
                if m.id == n.id_trvl_id and iid == 0:
                    i+=1
                    break
                    
        
        context = {
            'ph' : user.photo,
            'cpt' : cpt,
            'i' : i,
            'nb_ms' : Notification.objects.filter(status=False,id_user=u).count(),
            'ms' : Notification.objects.filter(status=False,id_user=u),
        }
        return render(request,'type_c/pages/test.html',context)

def imprimer(request,id_d):
    # if request.method == 'POST':
    #     dateE = request.POST['dateExpiration']
    #     dateD = request.POST['dateDeDelivrance']
    #     Demande.objects.get(id=id_d).update(dateExpiration=dateE,dateDeDelivrance=dateD)
    #     return redirect('homme_c')
    d = Demande.objects.get(id=id_d)
    d.statut='c'
    d.save()
    a = request.user 
    user = User_app.objects.get(username=a)
    u = user.id
    context = {
        'ph' : user.photo,
        'nb_ms' : Notification.objects.filter(status=False,id_user=u).count(),
        'ms' : Notification.objects.filter(status=False,id_user=u),
        'id_d' : id_d,
    }
    return render(request,'type_c/pages/valide.html',context)
def valid(request,id_d):
    a = request.user 
    user = User_app.objects.get(username=a)
    u = user.id
    d = Demande.objects.get(id=id_d)
    context = {
        'customers' : d,
        'ph' : user.photo,
        'nb_ms' : Notification.objects.filter(status=False,id_user=u).count(),
        'ms' : Notification.objects.filter(status=False,id_user=u),
    }
    if request.method == 'POST':
        dateE = request.POST['dateExpiration']
        dateD = request.POST['dateDeDelivrance']
        config = Demande.objects.get(id=id_d)
        config.dateExpiration=dateE
        config.dateDeDelivrance=dateD
        config.save()
        dem = Demande.objects.get(id=id_d)
        if dem.TypeDemande == 'Nouvaux':
            trs = Travailleur.objects.filter(numTel=dem.numTel).exists()
            if not trs :
                nt = Travailleur(id_soc=dem.id_soc,nomPrenom=dem.nomPrenom,email=dem.email,
                                numTel=dem.numTel,numPass=dem.numPass,dateNaissance=dem.dateNaissance,
                                Nationalite=dem.Nationalite,descPoste=dem.descPoste,photo=dem.photo)
                nt.save()
                ntt = Permis(id_trvl_id=nt.id,TypePermis=dem.TypePermis,dateDeDelivrance=dem.dateDeDelivrance,
                            etatRetrait=dem.etatRetrait,renouveler=False,dateExpiration=dem.dateExpiration)
                ntt.save()
                return render(request,'type_c/pages/permis.html',context)
            else:
                messages.warning(request, "erreur")
                return redirect('homme_c')
        else:
            tr = Travailleur.objects.filter(numTel=dem.numTel).exists()
            trs = Travailleur.objects.get(numTel=dem.numTel)
            if not tr  :
                messages.warning(request, "erreur")
                return redirect('homme_c')
            else:
                if dem.TypeDemande == 'Nouvaux':
                    ntt = Permis(id_trvl_id=trs.id,codePermis=d.codePermis,TypePermis=dem.TypePermis,dateDeDelivrance=dem.dateDeDelivrance,
                                etatRetrait=dem.etatRetrait,dateExpiration=dem.dateExpiration)
                    ntt.save()
                    # messages.success(request,"L'operation a été couronnée de succès")
                    return render(request,'type_c/pages/permis.html',context)
                else:
                    ntt = Permis(id_trvl_id=trs.id,codePermis=d.codePermis,TypePermis=dem.TypePermis,dateDeDelivrance=dem.dateDeDelivrance,
                                etatRetrait=dem.etatRetrait,renouveler=True,dateExpiration=dem.dateExpiration)
                    ntt.save()
                    # messages.success(request,"L'operation a été couronnée de succès")
                    return render(request,'type_c/pages/permis.html',context)
       
    
def detailc(request,id_user,id_n,id_d):
    # config = Notification.objects.get(id=id_n)
    # config.status=True
    # config.save()
    d = Demande.objects.filter(id=id_d)
    sc = Societe.objects.get(id=id_user)
    aa = sc.id_user_id
    # if request.method == 'POST':
    #     msg = request.POST['msg']
    #     config = Demande.objects.get(id=id_d)
    #     config.avis=msg
    #     config.save()
    #     s = User_app.objects.get(type_user='c')
    #     ss = s.id
    #     nt = Notification(id_user_id=ss,sujet="avis sur la demande",description="",id_soc=id_user,id_dem_id=id_d)
    #     nt.save()
    #     return redirect('homme_b')
    scs = Societe.objects.filter(id=id_user)
    bb = sc.id
    a = request.user 
    userr = User_app.objects.get(id=aa)
    user = User_app.objects.get(username=a)
    u = user.id
    v = Notification.objects.get(id=id_n)
    d = Demande.objects.filter(id=id_d)
    context = {
        'users' : user.photo,
        'ph' : user.photo,
        'idt' : aa,
        'id_sc' : bb,
        'dem' : d,
        'id_user' : id_user,
        'v' : id_n,
        'vd' : id_d,
        'DmandevForm':DmandevForm(),
        'nb_ms' : Notification.objects.filter(status=False,id_user_id=u).count(),
        'ms' : Notification.objects.filter(status=False,id_user_id=u),
    }
    return render(request,'type_c/pages/detail.html',context)

def status(request):
    a = request.user 
    user = User_app.objects.get(username=a)
    u = user.id
    context = {
        'ph' : user.photo,
        'status' : Demande.objects.all(),
        'nb_ms' : Notification.objects.filter(status=False,id_user_id=u).count(),
        'ms' : Notification.objects.filter(status=False,id_user_id=u),
    }
    return render(request,'user_soc/pages/homme.html',context)

def travailleur(request):
    a = request.user 
    user = User_app.objects.get(username=a)
    u = user.id
    tr = Travailleur.objects.all()
    test = None
    if tr :
        test = True
    else:
        test = False
    context = {
        'ph' : user.photo,
        'trvl' : tr,
        'test' : test,
        'nb_ms' : Notification.objects.filter(status=False,id_user_id=u).count(),
        'ms' : Notification.objects.filter(status=False,id_user_id=u),
    }
    return render(request,'user_soc/pages/travailleurs.html',context)

def hystorique(request):
    a = request.user 
    user = User_app.objects.get(username=a)
    u = user.id
    if user.type_user == 'd':
        his = Hystorique.objects.filter(id_user_id=u)
    else:
        his = Hystorique.objects.filter(type_user__in=['a','b','c'])
    context = {
        'ph' : user.photo,
        'hystorique' :his,
        'nb_ms' : Notification.objects.filter(status=False,id_user_id=u).count(),
        'ms' : Notification.objects.filter(status=False,id_user_id=u),
    }
    if user.type_user == 'a':
        return render(request,'type_a/pages/hystorique.html',context)
    elif user.type_user == 'b':
        return render(request,'type_b/pages/hystorique.html',context)
    elif user.type_user == 'c':
        return render(request,'type_c/pages/hystorique.html',context)
    elif user.type_user == 'd':
        return render(request,'user_soc/pages/hystorique.html',context)
    else:
        return redirect('login')
