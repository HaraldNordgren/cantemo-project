#!/usr/bin/env python3

import sys
import time
import logging

from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler
from watchdog.events import FileCreatedEvent

class MyEventHandler(FileSystemEventHandler):

    def dispatch(self, event):
        if isinstance(event, FileCreatedEvent):
            print("hej")

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
#path = sys.argv[1] if len(sys.argv) > 1 else '.'
#event_handler = LoggingEventHandler()
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
