from django.contrib import admin
from .models import DynamicModel

models = DynamicModel().models
for model in models.values():
    admin.site.register(model)

