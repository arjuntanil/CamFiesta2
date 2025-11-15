# middleware.py
from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            profile = getattr(request.user, 'profile', None)
            if profile and (not profile.phone_number or not profile.address):
                # Redirect to profile page if phone number or address is missing
                if request.path != reverse('profile'):
                    return redirect('profile')
        return self.get_response(request)
