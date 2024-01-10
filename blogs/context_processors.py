from .models import Category
from marketing.models import SocialLink, About

def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)

def get_social_links(request):
    social_links = SocialLink.objects.all()
    return dict(social_links=social_links)

def get_about(request):
    try:
        about = About.objects.get(pk=1)
        return dict(about=about)
    except:
        return dict(about=None)