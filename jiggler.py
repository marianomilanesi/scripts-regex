import pyautogui
import time
import random

while True:
    # Mover el cursor del mouse un poco hacia la izquierda o hacia la derecha
    pyautogui.moveRel(random.randint(-10, 10), random.randint(-10, 10), duration=0.25)
    time.sleep(1)  # Esperar 30 segundos antes de mover el mouse nuevamente