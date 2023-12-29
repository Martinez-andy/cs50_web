from django.shortcuts import render
from markdown2 import Markdown

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