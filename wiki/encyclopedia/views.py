from django import forms
import markdown2
from django.http import HttpResponse
from django.shortcuts import render, redirect
import random

from . import util

class WikiPage(forms.Form):
    pgcontent = forms.CharField(label="",
    widget=forms.TextInput(attrs={
            'placeholder': 'Search Encyclopedia...',
            'class': 'form-control'
            })
    )
 

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": WikiPage()
    })

def entry(request,name):       
    mdfile = util.get_entry(name)
    if mdfile is None:
        return render(request, "encyclopedia/notfound.html")

    content = markdown2.markdown(mdfile)
    return render(request, "encyclopedia/entry.html", {
        "name": name,
        "content": content,
        "form": WikiPage()
    })

def search(request):
    form = WikiPage(request.GET)

    if form.is_valid():
        query = form.cleaned_data["pgcontent"]

    entries = util.list_entries()
    for entry in entries:
        if query.lower() == entry.lower():
            return redirect("entry", name=entry)

    match_entries = []
    for entry in entries:
        if query.lower() in entry.lower():
            match_entries.append(entry)
            
    return render(request, "encyclopedia/search_results.html",{
        "form": WikiPage(),
        "matched": match_entries
    })

def newpage(request):
    entries = util.list_entries()
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("user_provided_content")
        if any(entry.lower() == title.lower() for entry in entries):
            return HttpResponse("Page already exits dummy :(")
        else:
            util.save_entry(title, content)
            return redirect("entry", name=title)

    return render(request, "encyclopedia/newpage.html",{
        "form": WikiPage(),
        "entries": entries,
    })

def randompage(request):
    return redirect("entry", random.choice(util.list_entries()))


def edit(request, name):
    if request.method == "POST":
        util.save_entry(name, request.POST.get("content"))
        return redirect("entry", name)

    content = util.get_entry(name)

    return render(request, "encyclopedia/edit.html", {
        "name": name,
        "content": content,
    })