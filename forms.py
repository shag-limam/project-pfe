import imp
from django import forms
from .models import Societe, User_app, Demande
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _

class SocieteForm(forms.ModelForm):
    class Meta:
        model = Societe
        fields = ['Nom','NumeroRC','NumeroCNSS','region','nbreEmployee','secteurActivite',
            'FormeJuridique','adresse','gmail','contact']
        widgets = {
            'Nom': forms.TextInput(attrs={'class':'form-control'}),
            'NumeroRC': forms.FileInput(attrs={'class':'form-file-input form-control'}),
            'NumeroCNSS': forms.FileInput(attrs={'label': 'nn','class':'form-file-input form-control'}),
            'region' : forms.Select(attrs={'class':'form-control'}),
            'nbreEmployee': forms.NumberInput(attrs={'class':'form-control'}),
            'secteurActivite': forms.TextInput(attrs={'class':'form-control'}),
            'FormeJuridique': forms.TextInput(attrs={'class':'form-control'}),
            'adresse': forms.TextInput(attrs={'class':'form-control'}),
            'gmail': forms.TextInput(attrs={'class':'form-control'}),
            'contact': forms.NumberInput(attrs={'class':'form-control'}),        
        }
        labels = {
            'NumeroRC': _('Numero de Commerce'),
            'NumeroCNSS': _('Numero de declaration'),
            'region': _('Région'),
            'nbreEmployee': _("Nombre d'employe"),
            'secteurActivite': _("Secteur d'activite"),
            'FormeJuridique': _('Forme Juridique'),
            'adresse': _('Adresse'),
            'gmail': _('Gmail'),
            'contact': _('Contact'),    
        }

class DmandeForm(forms.ModelForm):
    class Meta:
        model = Demande
        fields = ['TypeDemande','denomination','siege','numIMM','nomPrenom','Nationalite','lieu_nais','cnss',
            'numPass','dateExpPass','email','numTel','dateNaissance','descPoste','expose',
            'photo','TypePermis','etatRetrait']
        widgets = {
            'TypeDemande': forms.Select(attrs={'class':'form-control'}),
            'denomination': forms.TextInput(attrs={'class':'form-control'}),
            'siege' : forms.TextInput(attrs={'class':'form-control'}),
            'numIMM': forms.NumberInput(attrs={'class':'form-control'}),
            'nomPrenom': forms.TextInput(attrs={'class':'form-control'}),
            'Nationalite': forms.Select(attrs={'class':'form-control'}),
            'lieu_nais': forms.TextInput(attrs={'class':'form-control'}),
            'cnss': forms.TextInput(attrs={'class':'form-control'}),
            'numPass': forms.TextInput(attrs={'class':'form-control'}),
            'dateExpPass': forms.DateInput(attrs={'type': 'date','class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'numTel': forms.NumberInput(attrs={'type': 'number','class':'form-control'}), 
            'dateNaissance': forms.DateInput(attrs={'type': 'date','class':'form-control'}),
            'descPoste': forms.Textarea(attrs={'type':'textarea','class':'form-control'}),
            'expose': forms.FileInput(attrs={'class':'form-file-input form-control'}),
            'photo': forms.FileInput(attrs={'class':'form-file-input form-control'}),
            'TypePermis': forms.Select(attrs={'class':'form-control'}),
            'etatRetrait': forms.TextInput(attrs={'class':'form-control'}),     
        }
        labels = {
            'TypeDemande': _('Type de demande'),
            'denomination': _('Denomination'),
            'siege': _("Siege"),
            'numIMM': _("Numero NNI"),
            'nomPrenom': _('Nom et Prenom'),
            'Nationalite': _('Nationalite'),
            'lieu_nais': _('Lieu de nassance'),
            'cnss': _('Caisse Nationale de Securité Sociale '),
            'numPass': _('Numero du passeport'),
            'dateExpPass': _("Date d'expiration passport"),
            'email': _("G-mail"),
            'numTel': _("Numero du telephone"),
            'dateNaissance': _("Date de naissance"),
            'descPoste': _("Description du poste"),
            'expose': _('Photo du passeport'),
            'photo': _("Image"),
            'TypePermis': _("Type de permis"),
            'etatRetrait': _('Etat de retrait'),     
        }




class User_appForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nom d'utulisateur",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Gmail",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Mot de passe ",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirmation du mot de passe",
                "class": "form-control"
            }
        ))
    photo = forms.CharField(
        widget=forms.FileInput(
            attrs={
                "placeholder": "Image",
                "class": "form-control"
            }
        ))
    class Meta:
        model = User_app
        fields = ('username', 'email', 'photo','password1', 'password2')

class DmandevForm(forms.ModelForm):
    class Meta:
        model = Demande
        fields = ['dateExpiration','dateDeDelivrance']
        widgets = {
            'dateExpiration': forms.DateInput(attrs={'type': 'date','class':'form-control'}),
            'dateDeDelivrance': forms.DateInput(attrs={'type': 'date','class':'form-control'}),
        }
        labels = {
            'dateExpiration': _("Date d'Expiration"),
            'dateDeDelivrance': _('Date de délivrance'),
        }