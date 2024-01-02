from django.shortcuts import render
from markdown2 import Markdown
import random


from . import util

def mdToHtml(title):
    content = util.get_entry(title)
    markdowner = Markdown()
    if content == None:
        return None
    return markdowner.convert(content)


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def wikiPage(request, title):
    content = mdToHtml(title)
    if content == None:
        return render(request, "encyclopedia/error.html", {
            "title": title
        })
    return render(request, "encyclopedia/wiki.html", {
        "title": title.capitalize(),
        "content": content
    })



# The form sends its data to this function
# The form's value is returned in the request argument under "q" because that is the name of our form's action
# CSRF tokens are needed for forms (Needed for secure requests)
def search(request):
    if request.method == "POST":
        title = request.POST["q"]
        content = mdToHtml(title)
        if content != None: # If the a wiki page exists already, then render the page
            return render(request, "encyclopedia/wiki.html", {
                "title": title,
                "content": content
            })
        # If wiki page doesn't exist then we want to return any wiki pages that
        allEntries = util.list_entries()
        res = []
        
        for entry in allEntries:
            if title.lower() in entry.lower():
                res.append(entry)
        return render(request, "encyclopedia/results.html", {
            "entries": res
        })
        
        
def randomPage(request):
    allEntries = util.list_entries()
    title = random.choice(allEntries)
    return wikiPage(request, title)