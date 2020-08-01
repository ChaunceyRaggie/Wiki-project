from django.shortcuts import render
import markdown as md
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def title(request,title):
        content = util.get_entry(title)
        if content:
            return render(request,"encyclopedia/content.html",{
                "content": md.markdown(content),
                "title": title
        })
        else: 
            return render(request,"encyclopedia/error.html")





