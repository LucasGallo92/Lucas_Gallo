from django.shortcuts import render

# Create your views here.
from .models import BronzeSaint, SilverSaint, GoldSaint

def index(request):
    bronze_saints = BronzeSaint.objects.all()
    silver_saints = SilverSaint.objects.all()
    gold_saints = GoldSaint.objects.all()
    return render(request, 'saints/index.html', {'bronze_saints': bronze_saints, 'silver_saints': silver_saints, 'gold_saints': gold_saints})