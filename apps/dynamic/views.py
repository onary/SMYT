import os
import yaml

from django.shortcuts import render
from django.conf import settings
from django.db.models import get_model

from annoying.decorators import ajax_request
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict

from .forms import create_form
from .utils import UPOST

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

    form = create_form(model, fields)

    return render(request, 'entity.html',
                  {'objects': result, 'entity': model_name, 'form': form})


@ajax_request
@require_POST
def switch_data(request):
    model_name = request.POST.get('_entity', None)
    id = request.POST.get('_id', None)

    Model = get_model('dynamic', model_name)
    fields = [f.name for f in Model._meta.fields]
    Form = create_form(Model, fields)
    if id:
        field = request.POST.get('field', None)
        value = request.POST.get('val', None)
        instance = get_object_or_404(Model, id=id)
        form = Form(UPOST(request.POST, instance, field, value),
                    instance=instance)

        if form.is_valid():
            form.save()
            return {'res': 'success'}
    else:
        form = Form(request.POST)
        if form.is_valid():
            instance = form.save()
            data = '{'
            for k, v in model_to_dict(instance, fields=fields).iteritems():
                data += '"%s":"%s",' % (k, v)
            data = data[:-1] + '}'
            return {'res': 'success', 'instance': data}
        else:
            return {'res': 'fail', 'err': str(form.errors)}
    return {'res': 'fail'}
