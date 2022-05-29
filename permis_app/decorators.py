from django.shortcuts import redirect
# from django.http import HttpResponse




def notLoggedUsers(view_func):
    def wrapper_func(request , *args,**kwargs):
        if request.user.is_authenticated:
            return redirect('test')
        else:
            return view_func(request , *args,**kwargs)
    return wrapper_func

def allowedUsers(allowedGroups=[]):
    def decorator(view_func):
        def wrapper_func(request , *args,**kwargs): 
            group = None
            if request.user.groups.exists():
               group =  request.user.groups.all()[0].name
            if group in allowedGroups:
               return view_func(request , *args,**kwargs)
            else:
                return redirect('user_profile')
            
        return wrapper_func
    return decorator


def forDirectionStrategiquesPolitiquesEmploi(view_func): 
        def wrapper_func(request , *args,**kwargs): 
            group = None
            if request.user.groups.exists():
               group =  request.user.groups.all()[0].name
            if group == 'Groupe_A':
               return view_func(request , *args,**kwargs)
            if group == 'Groupe_B':
                return redirect('DirectionGeneralTravail')
            if group == 'Groupe_C':
                return redirect('DirectionGeneralEmploi')
            if group == 'Groupe_D':
                return redirect('Societe')
            
        return wrapper_func


def forDirectionGeneralTravail(view_func): 
        def wrapper_func(request , *args,**kwargs): 
            group = None
            if request.user.groups.exists():
               group =  request.user.groups.all()[0].name
            if group == 'Groupe_B':
               return view_func(request , *args,**kwargs)
            if group == 'Groupe_A':
                return redirect('DirectionStrategiquesPolitiquesEmploi')
            if group == 'Groupe_C':
                return redirect('DirectionGeneralEmploi')
            if group == 'Groupe_D':
                return redirect('Societe')
            
        return wrapper_func 


def forDirectionGeneralEmploi(view_func): 
        def wrapper_func(request , *args,**kwargs): 
            group = None
            if request.user.groups.exists():
               group =  request.user.groups.all()[0].name
            if group == 'Groupe_C':
               return view_func(request , *args,**kwargs)
            if group == 'Groupe_B':
                return redirect('DirectionGeneralTravail')
            if group == 'Groupe_A':
                return redirect('DirectionStrategiquesPolitiquesEmploi')
            if group == 'Groupe_D':
                return redirect('Societe')
            
        return wrapper_func 


def forSociete(view_func): 
        def wrapper_func(request , *args,**kwargs): 
            group = None
            if request.user.groups.exists():
               group =  request.user.groups.all()[0].name
            if group == 'Groupe_D':
               return view_func(request , *args,**kwargs)
            if group == 'Groupe_B':
                return redirect('DirectionGeneralTravail')
            if group == 'Groupe_C':
                return redirect('DirectionGeneralEmploi')
            if group == 'Groupe_A':
                return redirect('DirectionStrategiquesPolitiquesEmploi')
            
        return wrapper_func
