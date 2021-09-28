from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from random import randint

from . import util

entries = []

class SearchForm(forms.Form):
    inquiry = forms.CharField(label="inquiry")

class EntryForm(forms.Form):
    title = forms.CharField(label="Page Title")
    content = forms.CharField(label="Page Content")


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
    entries = util.list_entries()
    inquiry = request.GET.get("q","")
    if inquiry in entries:
        return redirect (entry, inquiry)
    results = []
    for entry in entries:
        if inquiry.lower() in entry.lower():
            results.append(entry)

    return render(request, "encyclopedia/search.html", {
        "entries": results
    })

def create(request):
    return render (request, "encyclopedia/create.html", {
    "form": EntryForm()
    })


def add(request):
    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            entries = util.list_entries()
            if title in entries:
                return HttpResponse("Error: Entry already exists")
            else:
                new_entry = util.save_entry(title, content)
                return redirect (entry, title)
    else:
        return render(request, "encyclopedia/create.html", {
        "form": EntryForm()
        })

def edit(request, title):
    return render(request, "encyclopedia/edit.html", {
        "title": title.capitalize,
        "content": util.get_entry(title)
    })

def revise(request):
    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            revise_entry = util.save_entry(title, content)
            return redirect (entry, title)
    else:
        return render(request, "encyclopedia/edit.html", {
            "title": title.capitalize
        })

def random(request):
    entries = util.list_entries()
    x = randint(1, len(entries))
    title = entries[x]
    return redirect (entry, title)
