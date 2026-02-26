from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import RegisterForm

def register_view(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Account Created!')
            return redirect('users:register')

    context = {'form': form}
    return render(request, 'users/register.html', context)