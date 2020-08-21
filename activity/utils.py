import datetime
import os
import uuid

def upload_to_storage(instance, filename):
    today = str(datetime.datetime.today().date())
    path = os.path.join('logos', str(instance.user.username))
    ext = '.' + filename.split('.')[-1]
    path = os.path.join(path, today + uuid.uuid4().hex + ext)
    return path