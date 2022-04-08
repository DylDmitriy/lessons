from django.contrib.auth import authenticate, login

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
        else:
            print("Не правильное Имя или Пароль")
            ...
    else:
        print("Не правильное Имя или Пароль")
        ...

@login_required
def my_view(request):
    ...
print("Вы в системе!")
