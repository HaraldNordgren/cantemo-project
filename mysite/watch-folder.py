#!/usr/bin/env python3

import time, os, django

os.environ["DJANGO_SETTINGS_MODULE"] = "mysite.settings"
django.setup()
from image_bank.models import BankImage

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import FileCreatedEvent

from constants import watched_folder


class MyEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        if isinstance(event, FileCreatedEvent):
            im_path = "/".join(event.src_path.split("/")[1:])
            im = BankImage(path=im_path)
            im.save()
            print("Added %s" % im_path)

os.chdir(watched_folder)
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
