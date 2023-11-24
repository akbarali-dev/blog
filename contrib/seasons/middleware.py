import os

from blog.models import Visitor
import requests


class VisitorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip_address = self.get_client_ip(request)
        if not Visitor.objects.filter(ip_address=ip_address).exists():
            response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()

            print("Res:  ", response)
            message = "#new_user\n"
            message += "IP address: " + ip_address
            message += "\nCity: " + response.get("city")
            message += "\nRegion: " + response.get("region")
            message += "\nCountry: " + response.get("country_name")

            token = os.environ.get("BOT_TOKEN")

            requests.get("https://api.telegram.org/bot" + token + "/sendMessage?chat_id"
                                                                  "=1474104201&text=" + message + "")

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
