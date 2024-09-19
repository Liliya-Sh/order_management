from restaurant_ordering.utils import menu


def get_context(request):
    return {'mainmenu': menu}
