from django.shortcuts import render

# Create your views here.
from .models import Chocolate, Company, Nutrients

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_chocolates = Chocolate.objects.all().count()

    # The 'all()' is implied by default.
    num_companies = Company.objects.count()

    context = {
        'num_chocolates': num_chocolates,
        'num_companies': num_companies,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
