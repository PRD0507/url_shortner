from django.shortcuts import render
from django.http import HttpResponse
import pyshorteners


# Create your views here.
def shorten(request, url):
    print("asdasdads")
    shortener = pyshorteners.Shortener()
    shortened_url = shortener.chilpit.short(url)
    return HttpResponse(f'Shortened URL: <a href="{shortened_url}">{shortened_url}</a>')

# def shorten(request, url):
#     random_hash = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(7))
#     mapping = LinkMapping(original_url=url, hash=random_hash, creation_date=timezone.now())
#     mapping.save()
#     return random_hash



def load_url(url_hash):
    return LinkMapping.objects.get(hash=url_hash)
