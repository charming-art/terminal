import time
import os
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import shutil

WATCH_PATH = './docs'
SOURCE_PATH = WATCH_PATH
TARGET_PATH = "../website/docs"


class CopyEventHandler(LoggingEventHandler):

    def on_any_event(self, event):
        if os.path.exists(TARGET_PATH):
            shutil.rmtree(TARGET_PATH)

        shutil.copytree(SOURCE_PATH, TARGET_PATH)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    event_handler = CopyEventHandler()
    observer = Observer()
    observer.schedule(event_handler, WATCH_PATH, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()
