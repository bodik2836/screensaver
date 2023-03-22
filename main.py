import datetime
import os
import time

block_times = ["10:20", "11:50", "15:20", "16:50", "18:20"]

while True:
    current_time = datetime.datetime.now().strftime("%H:%M")

    if current_time in block_times:
        os.system("gnome-screensaver-command -l")

    time.sleep(60)
