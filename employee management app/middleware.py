# djangoexamapp/middleware.py
from django.http import HttpResponseForbidden

# List of blocked IPs
BLOCKED_IPS = ['192.168.1.10', '10.0.0.5']  

class BlockIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        if ip in BLOCKED_IPS:
            return HttpResponseForbidden("Your IP address is blocked.")
        response = self.get_response(request)
        return response
