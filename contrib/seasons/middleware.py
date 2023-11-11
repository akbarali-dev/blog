from blog.models import Visitor


class VisitorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip_address = self.get_client_ip(request)
        Visitor.objects.create(ip_address=ip_address, referring_url=request.path)
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
