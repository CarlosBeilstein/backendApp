from rest_framework import generics
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from .models import FavStocks
from .serializers import ListSerializer
import json
from django.http import JsonResponse

username = 'carl'
user, created = User.objects.get_or_create(username=username)
token, created = Token.objects.get_or_create(user=user)

# go to index page of server
def index(request):
    data = FavStocks.objects.all()
    return render(request, 'index.html', {'data': data})

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import FavStocks
import json

def create(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Check if a FavStocks entry with the same company name already exists
            existing_entry = FavStocks.objects.filter(companyName=data.get('companyName')).first()

            if existing_entry:
                # Update the existing entry if needed
                existing_entry.price = data.get('price')
                existing_entry.added = data.get('added')
                existing_entry.change = data.get('change')
                #existing_entry.changePer = data.get('changePer')
                existing_entry.movement = data.get('movement')
                existing_entry.save()
            else:
                # Create a new FavStocks entry
                new_entry = FavStocks.objects.create(
                    name=data.get('name'),
                    companyName=data.get('companyName'),
                    price=data.get('price'),
                    added=data.get('added'),
                    change=data.get('change'),
                    #changePer=data.get('changePer'),
                    movement=data.get('movement')
                )

            response_data = {'status': 'success', 'message': 'Data received and processed'}
            return JsonResponse(response_data, status=200)

        except json.JSONDecodeError as e:
            response_data = {'status': 'error', 'message': 'Failed to decode JSON data'}
            return JsonResponse(response_data, status=400)
    else:
        response_data = {'status': 'error', 'message': 'Only POST requests are allowed'}
        return JsonResponse(response_data, status=405)

#delete fav stock from list
@csrf_exempt #to skip csrf validation
def update(request, entryCompanyName):
    entry = FavStocks.objects.filter(companyName=entryCompanyName).first()
    entry.delete()
    return redirect('index')


    

def delete_all(request):
    print(f"Token key for user: {user.username}: {token.key}")
    FavStocks.objects.all().delete()
    return redirect('index')

class FavStockListCreateView(generics.ListCreateAPIView):
    queryset = FavStocks.objects.all()
    serializer_class = ListSerializer