from django.shortcuts import render
from .forms import InterestCalculationForm

def calculate_interest(request):
    if request.method == 'POST':
        form = InterestCalculationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            principal = data['principal_amount']
            rate = data['interest_rate']
            time = data['time_period']
            # Calculate simple interest
            interest = (principal * rate * time) / 100
            return render(request, 'simple_interest_calc/result.html', {'interest': interest})
    else:
        form = InterestCalculationForm()
    return render(request, 'simple_interest_calc/form.html', {'form': form})
