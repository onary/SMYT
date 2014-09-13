import os
import yaml

from django.shortcuts import render
from django.conf import settings
from django.db.models import get_model

from annoying.decorators import ajax_request
from django.views.decorators.http import require_POST

from .forms import create_form

def index(request):
    models = []
    with open(os.path.join(settings.BASE_DIR, 'data.yaml'), 'r') as data:
        models = yaml.load(data).keys()
    model = get_model('dynamic', 'users')
    return render(request, 'index.html',
                  {'models': models})


def entity(request, model_name=None):
    model = get_model('dynamic', model_name)
    fields = [f.name for f in model._meta.fields]
    verbose = {}
    for f in fields:
        verbose.update({f: model._meta.get_field_by_name(f)[0].verbose_name})

    result = [verbose] + list(model.objects.all().values(*fields))

    # obj = model.objects.all()[0]

    form = create_form(model, fields)

    return render(request, 'index.html',
                  {'objects': result, 'entity': model_name, 'form': form})


@ajax_request
@require_POST
def switch_data(request):
    model_name = request.POST.get('entity', None)
    id = request.POST.get('id', None)
    field = request.POST.get('field', None)
    value = request.POST.get('value', None)
    if not model_name or not id or not field or not value:
        return {'res': 'fail'}

    model = get_model('dynamic', model_name)
    item = model.objects.get(pk=id)
    print item[field]
    return {'res': 'success', 'data': 'data'}
