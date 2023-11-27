import os
from multiprocessing.sharedctypes import synchronized

from blog.models import Visitor
import requests
from urllib.parse import quote


def already_ip_address(ip_address):
    print("hello")
    if not Visitor.objects.filter(ip_address=ip_address).exists():
        response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
        message = "#new_user\n"
        message += "IP address: " + ip_address
        message += "\nCity: " + str(response.get("city"))
        message += "\nRegion: " + str(response.get("region"))
        message += "\nCountry: " + str(response.get("country_name"))

        token = os.environ.get("BOT_TOKEN")
        encoded_message = quote(message)
        requests.get("https://api.telegram.org/bot" + token + "/sendMessage?chat_id"
                                                              "=1474104201&text=" + encoded_message + "")


class VisitorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip_address = self.get_client_ip(request)
        already_ip_address(ip_address=ip_address)
        if request.path.startswith('/admin/'):
            Visitor.objects.create(ip_address=ip_address, referring_url=request.path, category='A')
        elif request.path.startswith('/static/'):
            Visitor.objects.create(ip_address=ip_address, referring_url=request.path, category='S')
        elif request.path.startswith('/media/'):
            Visitor.objects.create(ip_address=ip_address, referring_url=request.path, category='M')

        else:
            Visitor.objects.create(ip_address=ip_address, referring_url=request.path, category='W')
        response = self.get_response(request)

        return response

    # @staticmethod
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    # def __call__(self, request):
    #     ip_address = request.META.get('REMOTE_ADDR')
    #     referring_url = request.META.get('HTTP_REFERER')
    #     print("data: ", request.path)
    #     # if request.method == "POST" and "HTTP_REFERER" in request.META:
    #     Visitor.objects.create(ip_address=ip_address, referring_url=request.path)
    #     response = self.get_response(request)
    #     return response
