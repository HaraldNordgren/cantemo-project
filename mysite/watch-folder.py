#!/usr/bin/env python3

import time, os, django

os.environ["DJANGO_SETTINGS_MODULE"] = "mysite.settings"
django.setup()
from image_bank.models import BankImage

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import FileCreatedEvent


class MyEventHandler(FileSystemEventHandler):

    #def dispatch(self, event):
    def on_created(self, event):
        if isinstance(event, FileCreatedEvent):
            im = BankImage(path=event.src_path)
            im.save()
            print("Added %s" % event.src_path)

event_handler = MyEventHandler()
observer = Observer()
observer.schedule(event_handler, "./stored-images", recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    observer.stop()

observer.join()
