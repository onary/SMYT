from django.forms.models import model_to_dict
from copy import copy

def UPOST(post, obj, field=None, value=None):
    '''
        Updates request's POST dictionary with
        values from object, for update purposes
    '''
    post = copy(post)
    if field and value:
        post[field] = value
    for k,v in model_to_dict(obj).iteritems():
        if k not in post: post[k] = v
    return post
