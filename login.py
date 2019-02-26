import time, subprocess
from pynput.keyboard import Key, Controller

keyboard = Controller()

subprocess.call(['C:\Riot Games\League of Legends\LeagueClient.exe'])
time.sleep(15)
keyboard.type('suasenha123')
keyboard.press(Key.enter)
keyboard.release(Key.enter)
