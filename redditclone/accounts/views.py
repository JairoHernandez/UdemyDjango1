from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def signup(request):

    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            # Will create a user in our DB viewable in admin admin page.
            # 'username' corresponds to <input type="text" name="username" />
            # You specify key password because you are breaking order since key email was next in line.
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username already exists.'})
            except User.DoesNotExist:
                User.objects.create_user(request.POST['username'], password=request.POST['password1']) 
                login(request, user) # Instantly signs user in. Helps prevent logging into admin page as a user without admin creds.
                return render(request, 'accounts/signup.html')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords didn\'t match.'})
    else:
        return render(request, 'accounts/signup.html')
