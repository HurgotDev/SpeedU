import os
from uuid import uuid4

from django.db import models
from django.utils import timezone


def path_and_rename(path, name=''):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        now = timezone.now()
        #get filename
        if name != '':
            filename = '{}_{}.{}'.format(name,now, ext)
        else:
            #set filename as random string
            filename = '{}_{}.{}'.format(uuid4().hex, now, ext)
        return os.path.join(path, filename)
    return wrapper


