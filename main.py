import datetime
import os
import time

# список часових точок для блокування екрану
block_times = ["10:20", "11:50", "15:20", "16:50", "18:20"]

while True:
    # Отримуємо поточний час
    current_time = datetime.datetime.now().strftime("%H:%M")

    # Перевіряємо, чи поточний час є однією з часових точок для блокування екрану
    if current_time in block_times:
        # запускаємо команду блокування екрану
        os.system("gnome-screensaver-command -l")

    # Чекаємо 1 хвилину перед перевіркою наступної часової точки
    time.sleep(60)