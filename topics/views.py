from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to the SF Nexus website's page for visualizing the science fiction corpus through LDA topic modeling in Gensim with pyldavis. Stay tuned for an interactive visualization, downloadable extracted features datasets, and guided tutorials and instructions.")
