from Accounts.models import *

def profile_details(request):
    if request.user.is_authenticated: 
        user = User_Profile.objects.get(user=request.user.id)
        try:
            pic = Profile_pic.objects.get(user=request.user)
            user_pic = pic.picture
        except:
            user_pic = None
        user_pfn = user.profile_name
        user_abt = user.about
        return {'user_pfn': user_pfn, 'user_abt': user_abt, 'user_pic': user_pic}
    else:
        user_pfn = None
        user_abt = None
        user_pic = None
        return {'user_pfn': user_pfn, 'user_abt': user_abt, 'user_pic': user_pic}

    