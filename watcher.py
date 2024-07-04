import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess


class RunScriptOnChangeHandler(FileSystemEventHandler):
    def __init__(self, script):
        self.script = script

    def on_modified(self, event):
        if event.src_path.endswith(self.script):
            print(f'{self.script} has been modified, running script...')
            subprocess.run(['python', self.script])


if __name__ == "__main__":
    script_to_watch = 'social_scraper.py'
    event_handler = RunScriptOnChangeHandler(script_to_watch)
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
