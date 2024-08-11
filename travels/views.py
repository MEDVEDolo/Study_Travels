from django.shortcuts import render, redirect
from .models import Travel
from .forms import TravelForm
from Core.models import User

# Create your views here.
def main(request):
    return render(request, 'travels/main.html')

def travel_list(request):
    travels = Travel.objects.all()
    return render(request, 'travels/travel_list.html', {'travels': travels})

def travel_detail(request, travel_id):
    travel = Travel.objects.get(id=travel_id)
    return render(request, 'travels/travel_detail.html', {'travel': travel})

def travel_create(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    if request.method == 'POST':
        form = TravelForm(request.POST, request.FILES)
        if form.is_valid():
            user_id=request.user.id
            author = User.objects.get(id=user_id)
            form_update = form.save(commit=False)
            form_update.author = author
            print(author)
            form_update.save()
            return redirect('travel_list')
    else:
        form = TravelForm()
    return render(request, 'travels/travel_create.html', {'form': form})