from models import Background

def background(request):
    try:
        background = Background.objects.order_by('?')[0]
    except IndexError:
        background = None
    return {'background': background}