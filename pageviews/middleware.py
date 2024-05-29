from .models import PageView

class PageViewMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.method == 'GET':
            PageView.objects.create(
                url=request.build_absolute_uri(),
                ip_address=request.META.get('REMOTE_ADDR'),
                referrer=request.META.get('HTTP_REFERER', '')
            )
        return response
