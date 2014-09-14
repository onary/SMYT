import json

from django.test import TestCase
from django.test.client import Client
from django.db.models import get_model
from django.core.urlresolvers import reverse

from .utils import get_models_names


class ModelsTest(TestCase):
    def setUp(self):
        self.instances = [get_model("dynamic", model).objects.create() for \
                            model in get_models_names()]

    def test_instances_created(self):
        for instance in self.instances:
            self.assertEqual(instance.pk, 1)


class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.models = get_models_names()

    def test_index(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "text/html; charset=utf-8")

    def test_entity(self):
        for model in self.models:
            response = self.client.get(reverse("entity",
                                 kwargs={"model_name": model}))
            self.assertEqual(response.status_code, 200)

    def test_switch_data(self):
        for model in self.models:
            response = self.client.post(reverse("switch_data"),
                              {"_entity": model},
                              HTTP_X_REQUESTED_WITH="XMLHttpRequest")

            data = json.loads(response.content)

            self.assertEqual(data["res"], "fail")
            self.assertEqual(response.status_code, 200)
