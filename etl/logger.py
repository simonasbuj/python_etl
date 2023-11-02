from datetime import datetime
from pathlib import Path

class Logger():

    def __init__(
            self, 
            app_name, 
            log_file=(Path(__file__).parents[1] / 'logs' / 'logs.txt').absolute(),
            input_files_folder=Path(__file__).parents[1] / 'input_files'
            ):
        self.app_name = app_name
        self.log_file = Path(log_file)
        self.input_files_folder = Path(input_files_folder)


    def log(self, message):
        timestamp = datetime.now()

        if type(message) == dict:
            message_object = message
        else:
            message_object = {"message": message}

        message_object["timestamp"] = str(timestamp)
        message_object["log_file"] = self.log_file
        message_object["input_files"] = self.input_files_folder

        with self.log_file.open('a') as f: 
            f.write(str(message_object))
            f.write("\n")
