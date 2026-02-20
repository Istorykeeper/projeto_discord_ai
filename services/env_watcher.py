from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from dotenv import load_dotenv

class EnvHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".env"):
            print(".env alterado! Recarregando...")
            load_dotenv(override=True)

def start_env_watcher():
    observer = Observer()
    observer.schedule(EnvHandler(), path='.', recursive=False)
    observer.start()
