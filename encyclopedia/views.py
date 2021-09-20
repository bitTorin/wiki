from django.http import HttpResponse
from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    # if request.medthod == "POST":
    #     name =
    return render(request, "encyclopedia/entry.html", {
        "title": util.get_entry(title)
    })
