from expense_tracker import settings

def cloud_front_host(request):
    return {
        'CLOUD_FRONT_HOST': settings.CLOUD_FRONT_HOST,
    }
