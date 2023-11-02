from datetime import datetime
from pathlib import Path
import os

class Logger():

    def __init__(self, app_name, log_file=Path(__file__).parents[1] / 'logs' / 'logs.txt'):
        self.app_name = app_name
        self.log_file = log_file


    def log(self, message):
        timestamp = datetime.now()
        print(f"hi {os.path.dirname(self.log_file)}")
        message_object = {
            "message": message,
            "timestamp": {timestamp},
            "log_file": self.log_file
        }

        print(message_object)
