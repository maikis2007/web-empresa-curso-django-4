from django.utils.text import slugify
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Page

# Create your views here.

def page(request, page_id, page_title=''):
    page = get_object_or_404(Page, id=page_id)

    if page_title and not page_title == slugify(page.title):  # page_title no esta vacío pero no es su slugify
        raise Http404

    return render(request, 'pages/sample.html', {
        'page': page
    })
