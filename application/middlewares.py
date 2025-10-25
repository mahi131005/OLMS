from django.shortcuts import redirect

#********** Authenticated Middleware **********#
# This middleware is used to check if the user is authenticated or not.

def auth(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated==False:
            return redirect('login')
        return view_function(request, *args, **kwargs)
    return wrapper_function

#********** Unauthenticated Middleware **********#
# This middleware is used to check if the user is unauthenticated or not.

def unauth(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated==True:
            return redirect('index')
        return view_function(request, *args, **kwargs)
    return wrapper_function