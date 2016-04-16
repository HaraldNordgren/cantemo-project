#!/usr/bin/env python3

import time, os, mimetypes, subprocess
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

    def convert_video(self, rel_path):

        (filename, ex) = os.path.splitext(rel_path)

        converted_path = filename + "_libx264.mp4"
        cmd = 'ffmpeg -i "%s" "%s" -y' % (rel_path, converted_path)
        subprocess.call(cmd, shell=True)

        return converted_path

    def on_created(self, event):
        if isinstance(event, FileCreatedEvent):
            rel_path = self.remove_dot(event)
            start_path = os.path.splitext(rel_path)[0]

            if BankImage.objects.filter(path__startswith=start_path.rstrip("_libx264")):
                    return

            file_type = mimetypes.guess_type(rel_path)[0]

            if file_type == 'application/mxf':
                file_type = 'video/mxf'

            if file_type.split("/")[0] == 'video':
                converted_path = self.convert_video(rel_path)
                im = BankImage(path=rel_path, file_type=file_type, converted_path=converted_path)
            else:
                im = BankImage(path=rel_path, file_type=file_type)
            
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
