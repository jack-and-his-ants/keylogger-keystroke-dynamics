import pynput
import time

from pynput.keyboard import Key, Listener

keys = [] # (key,time_pressed,time_released)
count = 0

stringify_keys(key_list)

def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print(f"{key} pressed,{time.time()}")
def on_release(key):
    print(f"{key} released,{time.time()}")
    

with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()