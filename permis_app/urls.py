from django.urls import path
# from django.conf.urls import url
from django.contrib.auth.views import LoginView
from django.conf.urls import url
from . import views,viewss,viewse
from django.contrib.auth import views as authViews

urlpatterns = [
    path('',views.test,name='DirectionStrategiquesPolitiquesEmploi'),
    path('login',views.logi_n,name='login'),
    path('register',views.register,name='register'),
    path('incoherent/<str:id_user>/<str:id_n>/<str:id_d>',views.incoherent,name='incoherent'),
    path('exploiter/<int:id_soc>/<int:id_dem>',views.exploiter,name='exploiter'),
    path('valide/<int:id_u>/<int:id_sc>',views.valide,name='valide'),
    path('incomplet/<int:id_u>',views.incomplet,name='incomplet'),
    path('detaill/<str:id_user>/<str:id_n>/<str:id_d>',views.detaill,name='detaill'),
    path('logout',views.logou_t,name='logout'),
    path('activate/<uidb64>/<token>',views.activate, name='activate'),
    path('nactivate/<uidb64>/<token>',views.nactivate, name='nactivate'),
    url(r'^profile/$',views.view_profile,name='profile'),
    url(r'^profile/edit/$',views.edit_profile,name='edit_profile'),
    url(r'^change-password/$',views.change_password,name='change_password'),
    
    # user_soc
    path('Societe',viewss.index,name='Societe'),
    path('voir',viewss.voir,name='voir'),
    path('registerr',viewss.registerr,name='registerr'),
    path('renouvel',viewss.renouvel,name='renouvel'),
    path('detaill/<int:id_n>/<int:id_d>',viewss.detail,name='detail'),
    path('reponse/<int:id_n>/<int:id_d>',viewss.reponse,name='reponse'),
    
    # user_b
    path('DirectionGeneralTravail',viewse.index,name='DirectionGeneralTravail'),
    path('detaills/<str:id_user>/<str:id_n>/<int:id_d>',viewse.detail,name='detaills'),

    # user_c
    path('DirectionGeneralEmploi',viewse.indexc,name='DirectionGeneralEmploi'),
    path('detaillc/<str:id_user>/<str:id_n>/<int:id_d>',viewse.detailc,name='details'),
    path('valider/<int:id_d>',viewse.imprimer,name='imprimer'),
    path('impretion/<int:id_d>',viewse.valid,name='valid'),
    path('status',viewse.status,name='status'),
    path('travailleur',viewse.travailleur,name='travailleur'),
    path('hystorique',viewse.hystorique,name='hystorique'),
    
    
     path('reset_password/' ,authViews.PasswordResetView.as_view(template_name= "type_a/pages/password_reset.html") , name="reset_password"),
     path('reset_password_sent/' ,authViews.PasswordResetDoneView.as_view(template_name= "type_a/pages/password_reset_sent.html") , name="password_reset_done"),
     path('reset/<uidb64>/<token>/' ,authViews.PasswordResetConfirmView.as_view(template_name= "type_a/pages/password_reset_form.html") , name="password_reset_confirm"),
     path('reset_password_complete/' ,authViews.PasswordResetCompleteView.as_view(template_name= "type_a/pages/password_reset_done.html") , name="password_reset_complete"),
    

    
    

]