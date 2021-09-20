from django.http import HttpResponse
from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request):
    # if request.medthod == "POST":
    #     name =
    # return render(request, "encyclopedia/entry.html", {
    #     "name": util.get_entry(request)
    # })

    return HttpResponse("Hello World")
