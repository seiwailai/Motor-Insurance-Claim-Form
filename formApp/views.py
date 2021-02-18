from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClaimsForm, LoginForm, CreateUserForm
from .models import Claims
from django.core.exceptions import PermissionDenied


# Create your views here.

@login_required
def home(request):
    form = ClaimsForm()
    if request.method == 'POST':
        form = ClaimsForm(request.POST, request.FILES)
        if form.is_valid():
            claim = form.save()
            claim.user = request.user
            claim.save()
            messages.success(request, 'Form successfully submitted')
            return redirect('claim-home')
    return render(request, 'formApp/home.html', context={'form':form})


def signup(request):
    if request.user.is_authenticated:
        return redirect('claim-home')
    form = CreateUserForm(request.POST or None)
    if form.is_valid():
        form.save()
        user = form.cleaned_data.get('username')
        messages.success(request, f'Account was created for {user}')
        return redirect('claim-login')          
    return render(request, 'formApp/signup.html', {'title': 'Sign Up', 'form': form})


def login(request):
    if request.user.is_authenticated:
        return redirect('claim-home')
    form = LoginForm(data=request.POST or None)
    if form.is_valid():
        user = form.user_cache
        if user is not None:
            auth_login(request, user)
            return redirect('claim-home')
    return render(request, 'formApp/login.html', context={'form':form})

@login_required
def history(request):
    claims = Claims.objects.filter(user__pk=request.user.pk)
    return render(request,'formApp/history.html', context={'claims':claims})

@login_required
def editClaim(request, user_pk, claim_pk):
    if request.user.pk != user_pk:
        raise PermissionDenied("You have no permission to edit other user's claim form")

    claim = get_object_or_404(Claims, pk=claim_pk, user__pk=user_pk)

    if claim.claim_progress == 'Accepted':
        messages.info(request, 'The claim form is accepted and further amendment is not allowed.')
        claimForm = None
    else:
        claimForm = ClaimsForm(request.POST or None,instance=claim)
        if claimForm.is_valid():
            claim = claimForm.save(commit=False)
            claim.save()
            messages.success(request, 'The claim form is successfully updated.')
    return render(request, 'formApp/edit.html', context={'claimForm':claimForm})
        