import os
import yaml

from django.shortcuts import render
from django.conf import settings


def index(request):
    models = ''
    with open(os.path.join(settings.BASE_DIR, 'data.yaml'), 'r') as data:
        models = yaml.load(data)
    return render(request, 'index.html',
                  {'object': models})
