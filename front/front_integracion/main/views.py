from django.shortcuts import render
from django.http import JsonResponse
import requests 

# Create your views here.

def home(request):
    return render(request, "index.html")

def register_view(request):
    if request.method == "post":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if not all([username, email, password, confirm_password]):
            return JsonResponse({'error': 'All fields are required.'}, status=400)

        if password != confirm_password:
            return JsonResponse({'error': 'Passwords do not match.'}, status=400)


        backend_url = 'http://ip/register/'
        payload = {
            'username': username,
            'email': email,
            'password': password,
            'confirm_password': confirm_password,
        }
        try:
            response = requests.post(backend_url, json=payload)
            if response.status_code == 200:
                return JsonResponse({'message': 'User registered successfully.'})
            else:
                return JsonResponse({'error': response.json().get('error', 'Unknown error')}, status=response.status_code)
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': 'Failed to connect to the backend.'}, status=500)

    return render(request, 'index.html')
