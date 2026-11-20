import csv
import os
import time
from datetime import datetime

class KeystrokeLogger:
    def __init__(self, output_dir="../data/keystroke_logs",buffer_size=10):
        self.output_dir = output_dir
        self.keys = []  # (key, time_pressed, time_released)
        self.count = 0
        self.buffer_size = buffer_size
        os.makedirs(self.output_dir, exist_ok=True)

    def _get_current_filename(self):
        "generate a filename based on the current date and hour"
        now = datetime.now()
        timestamp_string = now.strftime("%Y-%m-%d_%H-00")
        filename = f"keystroke_log_{timestamp_string}.csv"
        return os.path.join(self.output_dir, filename)

    def log_event(self, user_id, key_code:str, press_time_ms:int, release_time_ms:int, dwell_time_ms:int=-1):
        "Saves a single event into the "
    def close(self):
        "closing the logger and saving any remaining keys to file"
        self.flush()
                                        