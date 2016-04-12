#!/usr/bin/env python3

import time, os, django

os.environ["DJANGO_SETTINGS_MODULE"] = "mysite.settings"
django.setup()
from image_bank.models import BankImage

from watchdog.observers import Observer
from watchdog.events import *

from constants import watched_folder


class MyEventHandler(FileSystemEventHandler):

    def remove_dot(self, event):
        return "/".join(event.src_path.split("/")[1:])

    def on_created(self, event):
        if isinstance(event, FileCreatedEvent):
            #im_path = self.remove_dot(event)
            im = BankImage(path=event.src_path)
            im.save()
            print("Added %s" % event.src_path)


    def on_deleted(self, event):
        if isinstance(event, FileDeletedEvent):
            #im_path = self.remove_dot(event)
            BankImage.objects.filter(path=event.src_path).delete()
            print("Removed %s" % event.src_path)


#os.chdir(watched_folder)
event_handler = MyEventHandler()
observer = Observer()
observer.schedule(event_handler, watched_folder, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    observer.stop()

observer.join()
