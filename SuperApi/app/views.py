"""
Definition of views.
"""
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpRequest
from rest_framework import viewsets
from .serializers import SupernaturalContactSerializer, SupernaturalPostSerializer,SupernaturalSermonSerializer,SupernaturalVideoSerializer
from .models import Contact, Post, Sermon, Video


class SupernaturalContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = SupernaturalContactSerializer

class SupernaturalPostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = SupernaturalPostSerializer

class SupernaturalSermonViewSet(viewsets.ModelViewSet):
    queryset = Sermon.objects.all()
    serializer_class =SupernaturalSermonSerializer

class SupernaturalVideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = SupernaturalVideoSerializer



from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
