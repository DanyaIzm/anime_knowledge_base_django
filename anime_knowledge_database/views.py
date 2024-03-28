from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required


def anime(request):
    return render(request, "index.html")


@login_required
def unit(request, path: str):
    if path.split(".")[-1] == "html":
        path = path.replace(".html", "")
    
    with open(settings.UPLOAD_PATH + "/" + path + ".html", "r", encoding="utf-8") as file:
        file_content = file.read()
    
    return HttpResponse(file_content)
