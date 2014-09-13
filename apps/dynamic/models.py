import os
import yaml
from datetime import date

from django.db import models
from django.conf import settings

class DynamicModel(object):
    models = {}

    def __init__(self, name=None, title=None, fields=None):
        if not name or not title or not fields:
            return None

        attrs = {'__module__': __name__,
                 '__unicode__': lambda x: '%s dynamic' % name,
                 'Meta': type('Meta', (),
                    {'app_label': 'dynamic',
                     'verbose_name': title,
                     'verbose_name_plural': title})}

        for field in fields:
            attrs.update({field['id']:
                self.to_field(field['type'], field['title'])})

        model = type(name, (models.Model,), attrs)

        self.__class__.models['%sDynamicModel' % name] = model

        self.model = model

    def to_field(self, tfield, verbose_name):
        if tfield == 'int':
            field = models.IntegerField(verbose_name=verbose_name)
        if tfield == 'char':
            field = models.CharField(max_length=256, verbose_name=verbose_name)
        if tfield == 'date':
            field = models.DateField(verbose_name=verbose_name,
                                         default=date.today)

        return field

with open(os.path.join(settings.BASE_DIR, 'data.yaml'), 'r') as data:
    for k, v in yaml.load(data).iteritems():
        DynamicModel(k, v['title'], v['fields']).model
