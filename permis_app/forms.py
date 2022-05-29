import imp
from django import forms
from .models import Societe, User_app, Demande
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.utils.translation import ugettext_lazy as _

class SocieteForm(forms.ModelForm):
    class Meta:
        model = Societe
        fields = ['Nom','NumeroRC','NumeroCNSS','region','nbreEmployee','secteurActivite',
            'FormeJuridique','adresse','gmail','contact']
        widgets = {
            'Nom': forms.TextInput(attrs={"placeholder": "Nom",'class':'form-control'}),
            'NumeroRC': forms.FileInput(attrs={'class':'form-control'}),
            'NumeroCNSS': forms.FileInput(attrs={'class':'form-control'}),
            'region' : forms.Select(attrs={"placeholder": "Région",'class':'form-control'}),
            'nbreEmployee': forms.NumberInput(attrs={"placeholder": "Nombre d'employe",'class':'form-control'}),
            'secteurActivite': forms.TextInput(attrs={"placeholder": "Secteur d'activite",'class':'form-control'}),
            'FormeJuridique': forms.TextInput(attrs={"placeholder": "Forme Juridique",'class':'form-control'}),
            'adresse': forms.TextInput(attrs={"placeholder": "Adresse",'class':'form-control'}),
            'gmail': forms.TextInput(attrs={"placeholder": "Gmail",'class':'form-control'}),
            'contact': forms.NumberInput(attrs={"placeholder": "Contact",'class':'form-control'}),        
        }
        labels = {
            'NumeroRC': _(' '),
            'Nom': _(' '),
            'NumeroCNSS': _(' '),
            'region': _(' '),
            'nbreEmployee': _(" "),
            'secteurActivite': _(" "),
            'FormeJuridique': _(' '),
            'adresse': _(' '),
            'gmail': _(' '),
            'contact': _(' '),    
        }

class DmandeForm(forms.ModelForm):
    class Meta:
        model = Demande
        fields = ['denomination','siege','numIMM','nomPrenom','Nationalite','lieu_nais','cnss',
            'numPass','dateExpPass','email','numTel','dateNaissance','descPoste','expose',
            'photo','TypePermis']
        widgets = {
            # 'TypeDemande': forms.Select(attrs={"placeholder": "Type de demande",'class':'form-control'}),
            'denomination': forms.TextInput(attrs={"placeholder": "Denomination",'class':'form-control'}),
            'siege' : forms.TextInput(attrs={"placeholder": "Siége",'class':'form-control'}),
            'numIMM': forms.NumberInput(attrs={"placeholder": "Numéro NNI",'class':'form-control'}),
            'nomPrenom': forms.TextInput(attrs={"placeholder": "Nom et Prenom",'class':'form-control'}),
            'Nationalite': forms.Select(attrs={"placeholder": "Nationalité",'class':'form-control'}),
            'lieu_nais': forms.TextInput(attrs={"placeholder": "Lieu de naissance",'class':'form-control'}),
            'cnss': forms.TextInput(attrs={"placeholder": "Caisse Nationale de Securité Sociale",'class':'form-control'}),
            'numPass': forms.TextInput(attrs={"placeholder": "Numéro du passeport",'class':'form-control'}),
            'dateExpPass': forms.DateInput(attrs={"placeholder": "Date d'expiration passport",'type': 'date','class':'form-control'}),
            'email': forms.TextInput(attrs={"placeholder": "Gmail",'class':'form-control'}),
            'numTel': forms.NumberInput(attrs={"placeholder": "Numero du telephone",'type': 'number','class':'form-control'}), 
            'dateNaissance': forms.DateInput(attrs={"placeholder": "Date de naissance",'type': 'date','class':'form-control'}),
            'descPoste': forms.Textarea(attrs={"placeholder": "Description du poste",'type':'textarea','class':'form-control'}),
            'expose': forms.FileInput(attrs={"placeholder": "Photo du passeport",'class':'form-file-input form-control'}),
            'photo': forms.FileInput(attrs={"placeholder": "Image",'class':'form-file-input form-control'}),
            'TypePermis': forms.Select(attrs={"placeholder": "Type de permis",'class':'form-control'}),   
        }
        labels = {
            'TypeDemande': _(''),
            'denomination': _(''),
            'siege': _(""),
            'numIMM': _(""),
            'nomPrenom': _(''),
            'Nationalite': _(''),
            'lieu_nais': _(''),
            'cnss': _(' '),
            'numPass': _(''),
            'dateExpPass': _(""),
            'email': _(""),
            'numTel': _(""),
            'dateNaissance': _(""),
            'descPoste': _(""),
            'expose': _(''),
            'photo': _(""),
            'TypePermis': _(""),   
        }

class User_appForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nom d'utulisateur",
                "class": "form-control"
            }
        ),
        label = "")
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Gmail",
                "class": "form-control"
            }
        ),
        label = "")
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id':'password',
                "placeholder": "Mot de passe ",
                "class": "form-control"
            }
        ),
        label = ""
        )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirmation du mot de passe",
                "class": "form-control"
            }
        ),
        label = ""
        )
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

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User_app
        fields = (  
            'type_user',
            'photo',
            'username',
            'email',
            'last_name',
            'first_name',
           )