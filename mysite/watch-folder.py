#!/usr/bin/env python3

import time, os
import django
os.environ["DJANGO_SETTINGS_MODULE"] = "mysite.settings"
django.setup()

from image_bank.models import BankImage
from image_bank.constants import *

from watchdog.observers import Observer
from watchdog.events import *


class MyEventHandler(FileSystemEventHandler):

    def remove_dot(self, event):
        return event.src_path.lstrip("./")

    def on_created(self, event):
        if isinstance(event, FileCreatedEvent):
            rel_path = self.remove_dot(event)
            im = BankImage(path=rel_path)
            im.save()
            print("Added %s" % rel_path)

    def on_deleted(self, event):
        if isinstance(event, FileDeletedEvent):
            rel_path = self.remove_dot(event)
            if BankImage.objects.filter(path=rel_path).delete()[0]:
                print("Removed %s" % rel_path)


full_watched_folder = "image_bank/" + watched_folder
os.chdir(full_watched_folder)

event_handler = MyEventHandler()
observer = Observer()
observer.schedule(event_handler, ".", recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    observer.stop()

observer.join()
