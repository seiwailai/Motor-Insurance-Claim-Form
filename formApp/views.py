from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClaimsForm
from django.contrib import messages
from .models import Claims

# Create your views here.
def home(request):
    form = ClaimsForm()
    if request.method == 'POST':
        form = ClaimsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form successfully submitted')
            return redirect('claim-home')
    return render(request, 'formApp/home.html', context={'form':form})


def history(request):
    claims = Claims.objects.all()
    return render(request,'formApp/history.html', context={'claims':claims})


def editClaim(request, pk):
    claim = get_object_or_404(Claims, pk=pk)

    if claim.claim_progress == 'Accepted':
        messages.info(request, 'The claim form is accepted and further amendment is not allowed.')
        return render(request, 'formApp/edit.html', context={'claimForm': None})
    else:
        claimForm = ClaimsForm(request.POST or None,instance=claim)
        if claimForm.is_valid():
            claim = claimForm.save(commit=False)
            claim.save()
            messages.success(request, 'The claim form is successfully updated.')
        return render(request, 'formApp/edit.html', context={'claimForm':claimForm})
        