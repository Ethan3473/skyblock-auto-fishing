"""Core functionality for Auto Fisher.
Contains functions to prepare the Minecraft window and run the fishing loop.
"""

import pyautogui
from time import sleep
import pygetwindow
import random
import keyboard


def prepare_minecraft():
    """Find the Minecraft window, resize and move it.

    Returns:
        window object if found, otherwise None
    """
    try:
        game = pygetwindow.getWindowsWithTitle('SkyClient (Forge 1.8.9)')[0]
        game.size = (870, 590)
        game.moveTo(900, 340)
        return game
    except Exception:
        pass

    try:
        game = pygetwindow.getWindowsWithTitle('Minecraft 1.8.9')[0]
        game.size = (870, 590)
        game.moveTo(900, 340)
        return game
    except Exception:
        print("Minecraft not found")
        return None


def random_wait():
    """Sleep for a short random interval to simulate human behavior."""
    sleep(random.uniform(0.2, 0.5))


def start(game, stop_key='x'):
    """Start the auto-fishing loop.

    This will block until the stop key is pressed, so call it from a thread
    if you want the UI to remain responsive.
    """
    if game is None:
        print("Minecraft not found")
        return

    try:
        pyautogui.moveTo(game.topleft[0] + game.size[0] / 2, game.topleft[1] + game.size[1] / 2)
        game.activate()
    except Exception:
        print("Could not focus game window")
        return

    fishes = 0
    sleep(2)
    pyautogui.rightClick()

    while not keyboard.is_pressed(stop_key):
        matching_color = pyautogui.pixelMatchesColor(930, 397, (255, 85, 85))
        if matching_color:
            random_wait()
            pyautogui.rightClick()
            random_wait()
            pyautogui.rightClick()
            fishes += 1

            # small movement every 10 catches to look a bit more natural
            if fishes % 10 == 0 and fishes != 0:
                fishes_sleep = random.uniform(0.2, 0.6)
                pyautogui.keyDown('a')
                sleep(fishes_sleep)
                pyautogui.keyUp('a')
                pyautogui.keyDown('d')
                sleep(fishes_sleep)
                pyautogui.keyUp('d')

    return
