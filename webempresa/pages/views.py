from django.shortcuts import render
from .models import Page
from django.shortcuts import get_object_or_404
# Create your views here.

def page(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    return render(request, "pages/sample.html", {'page': page})