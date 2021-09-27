from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

from . import util

# class NewEntryForm(forms.form):
#     entry = forms.CharField(label="Add Entry")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):

    return render(request, "encyclopedia/entry.html", {
        "title": title.capitalize,
        "content": util.get_entry(title)
    })

def search(request):

    return render(request, "encyclopedia/search.html", {
        "entries": util.list_entries()
    })

# def add(request):
#     if request.method == "POST":
#         form = NewEntryForm(request.POST)
#         if form.is_valid():
#             entry = form.cleaned_data["entry"]
#             request.session["entries"] += [entry]
#             return HttpResponseRedirect(reverse("entries:title"))
#         else:
#             return render(request, "encyclopedia/index.html", {
#                 "form": form
#             })
#     else:
#         return render(request, "encyclopedia/index.html", {
#             "form": NewTaskForm()
#         })
