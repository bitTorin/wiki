from django.http import HttpResponse
from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):

    return render(request, "encyclopedia/entry.html", {
        "title": title.capitalize,
        "content": util.get_entry(title)
    })

def search(request, inquiry):
    return render(request, "encyclopedia/search.html", {
     # TODO
    })
