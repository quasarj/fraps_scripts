import time
import datetime
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    """Simple handler that sets up a queue of new files"""
    queue = []

    def on_created(self, event):
        self.queue.append(event)


def print_status(guild, boss, wipe_counter):
    print
    print
    print guild
    print "Currently fightning {boss}, on attempt {attempt}. Good luck!".format(
        boss=boss, attempt=wipe_counter + 1)
    print "Press Control+C to exit this script"
    print

def rename(path, source, dest):
    print "Renaming '{}' to '{}'".format(source, dest)
    os.rename(os.path.join(path, source), os.path.join(path, dest))

if __name__ == "__main__":
    # initial setup
    wipe_counter = 0
    today = datetime.date.today()
    guild = raw_input("Enter guild name: ")
    boss = raw_input("Enter starting boss: ")
    print_status(guild, boss, wipe_counter)

    # start up watchdog to monitor the directory
    handler = MyHandler()
    observer = Observer()
    observer.schedule(handler, path='.', recursive=False)
    observer.start()

    try:
        while True:
            if len(handler.queue) > 0:
                event = handler.queue.pop(0)
                if not event.is_directory and 'FRAPSVID' not in event.src_path:
                    path, filename = os.path.split(event.src_path)
                    print "Detected new file ({0})".format(filename)
                    
                    win = raw_input("Did you win? (No): ")
                    if win.lower() == 'yes':
                        wipe_text = "Kill"

                        new_filename = "{guild} {date} {boss} {wipe}.avi".format(
                            guild=guild, boss=boss, date=today, wipe=wipe_text)

                        new_boss = raw_input("Enter new boss name: ")
                        boss = new_boss
                        wipe_counter = 0
                    else:
                        wipe_counter += 1
                        wipe_text = "Wipe {0}".format(wipe_counter)

                        new_filename = "{guild} {date} {boss} {wipe}.avi".format(
                            guild=guild, boss=boss, date=today, wipe=wipe_text)

                    rename(path, filename, new_filename)

                    print_status(guild, boss, wipe_counter)
            else:
                time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
