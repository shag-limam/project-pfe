from math import fabs
from tkinter import FALSE
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw


class User_app(AbstractUser):
    photo = models.ImageField(upload_to='photo_user',null=True,blank=True)
    type_user = models.CharField(max_length=250,default='d',blank=True,unique=False)
    pass

class Societe(models.Model):
    region_list = [
        ('senegale','sengale'),
        ('maroc','maroc'),
        ('algerie','algerie'),
        ('libya','libya'),
    ]
    id_user = models.ForeignKey(User_app,on_delete=models.CASCADE,null=True,blank=True)
    Nom = models.CharField(max_length=250,unique=True)
    NumeroRC = models.ImageField(upload_to='NumeroRC',null=True,blank=True)
    NumeroCNSS = models.ImageField(upload_to='NumeroCNSS',null=True,blank=True)
    region = models.CharField(max_length=50,choices=region_list,null=False,blank=False)
    nbreEmployee = models.IntegerField(null=False,blank=False)
    secteurActivite = models.CharField(max_length=250)
    FormeJuridique = models.CharField(max_length=250)
    adresse = models.CharField(max_length=250,null=False,unique=False)
    gmail = models.EmailField(max_length=250,null=True,unique=False)
    contact = models.IntegerField(null=True,unique=False)
    valide = models.BooleanField(default=False)
  
class Travailleur(models.Model):
    id_soc = models.ForeignKey(Societe,on_delete=models.CASCADE,null=True,blank=True)
    nomPrenom = models.CharField(max_length=250,unique=False)
    email = models.CharField(max_length=250,unique=True)
    numTel = models.CharField(max_length=250,unique=True)
    numPass = models.CharField(max_length=250,unique=True)
    dateNaissance = models.DateTimeField()
    Nationalite = models.CharField(max_length=250,unique=False)
    descPoste = models.CharField(max_length=250,unique=False)
    photo = models.ImageField(upload_to='photo',null=True,blank=True)
    
class Permis(models.Model):
    id_trvl = models.ForeignKey(Travailleur,on_delete=models.CASCADE,null=True,blank=True)
    TypePermis = models.CharField(max_length=250,unique=False)
    dateDeDelivrance = models.DateTimeField()
    etatRetrait = models.CharField(max_length=250,unique=False)
    renouveler = models.BooleanField(default=False)
    dateExpiration = models.DateTimeField()
    codePermis = models.IntegerField(unique=True)
   
class Infraction(models.Model):
    id_trvl = models.ForeignKey(Travailleur,on_delete=models.CASCADE,null=True,blank=True)
    NomSociete = models.CharField(max_length=250,unique=False)
    dateInfraction = models.DateTimeField()
    descInfraction = models.CharField(max_length=250,unique=False)
     
class Demande(models.Model):
    type = [
        ('A','A'),
        ('B','B'),
        ('C','C'),
    ]
    type_demande = [
        ('Nouvaux','Nouvaux'),
        ('renouvellement','renouvellement'),
    ]
    Nationalite_e = [
        ('Maroc','Maroc'),
        ('Algerie','Algerie'),
        ('Tunisi','Tunisi'),
        ('Libya','Libya'),
        ('Senegal','Senegal'),
        ('Mali','Mali'),
        ('France','France'),
    ]
    id_soc = models.ForeignKey(Societe,on_delete=models.CASCADE,unique=False,null=True,blank=True)
    dateDemandes = models.DateTimeField(default=timezone.now)
    TypePermis = models.CharField(max_length=250,choices=type,null=False,unique=False)
    Nationalite = models.CharField(max_length=250,choices=Nationalite_e,unique=False)
    denomination = models.CharField(max_length=250,unique=False)
    qr_code = models.ImageField(upload_to='qr_codes',blank=True)
    Employeur = models.CharField(max_length=250,null=True,blank=True)
    cnss = models.CharField(max_length=250,unique=False)
    lieu_nais = models.CharField(max_length=250,unique=False)
    siege = models.CharField(max_length=250,unique=False)
    numIMM = models.IntegerField(null=False,unique=False)
    nomPrenom = models.CharField(max_length=250,unique=False)
    numPass = models.CharField(max_length=250,unique=False)
    dateExpPass =  models.DateTimeField()
    email = models.CharField(max_length=250,null=False,unique=False)
    numTel= models.IntegerField(null=False,unique=False)
    dateNaissance = models.DateTimeField()
    descPoste = models.CharField(max_length=250,null=True,unique=False)
    expose = models.ImageField(upload_to='photo_passport',null=True,blank=True)
    photo =  models.ImageField(upload_to='photo',null=True,blank=True)
    statut = models.CharField(max_length=250,null=True,blank=True,unique=False)
    codePermis = models.IntegerField(max_length=250,null=True,blank=True,unique=True)
    TypeDemande = models.CharField(max_length=250,default='Nouvaux',choices=type_demande,null=False,unique=False)
    dateDeDelivrance = models.DateTimeField(null=True,blank=True)
    etatRetrait = models.CharField(max_length=250,blank=True,null=False,unique=False)
    dateExpiration = models.DateTimeField(null=True,blank=True)
    avis = models.CharField(max_length=250,null=True,blank=True,unique=False)
    
    def __str__(self):
        return str(self.id_soc)
    
    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.id_soc)
        canvas = Image.new('RGB', (290 , 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fnum = f'qr_code-{self.id_soc}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fnum, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)

class Notification(models.Model):
    id_user = models.ForeignKey(User_app,on_delete=models.CASCADE,null=True,blank=True) 
    sujet = models.CharField(max_length=250)
    status = models.BooleanField(default=False)
    description = models.CharField(max_length=250)
    date = models.DateTimeField(default=timezone.now)
    id_soc = models.CharField(max_length=250,blank=True,null=True)
    id_dem = models.ForeignKey(Demande,on_delete=models.CASCADE,null=True,blank=True) 
    
class Hystorique(models.Model):
    id_user = models.ForeignKey(User_app,on_delete=models.CASCADE,null=True,blank=True)
    Nom = models.CharField(max_length=250)  
    type_user = models.CharField(max_length=250,blank=True)  
    datecon = models.CharField(max_length=250)
    datedecon = models.CharField(max_length=250)
    tmps = models.CharField(max_length=250,blank=True,null=True)