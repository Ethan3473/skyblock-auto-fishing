"""User interface for Auto Fisher.

Contains the AutoFisherUI class that wraps the tkinter GUI and wires
buttons to functions in `functionality.py`.
"""

import threading
import tkinter as tk
from tkinter import Tk, Label, Button

import functionality


class AutoFisherUI:
    def __init__(self, root: Tk = None):
        self.root = root or tk.Tk()
        self.root.title('Auto Fisher')
        self.root.geometry('400x400')
        self.root.resizable(False, False)

        self.game = None

        title_text = Label(self.root, text='Auto Fisher', font=('Arial', 20))
        title_text.pack(side='top')

        prepare_minecraft_button = Button(self.root, text='Prepare Minecraft', command=self.prepare_minecraft)
        prepare_minecraft_button.pack(side='top', pady=(25, 0))

        start_button = Button(self.root, text='Start', command=self.start)
        start_button.pack(side='top', pady=(25, 0))

        stop_button = Label(self.root, text='Hold x for 2 seconds to stop', font=('Arial', 10))
        stop_button.pack(side='top', pady=(25, 0))

        self.status_label = Label(self.root, text='', font=('Arial', 10))
        self.status_label.pack(side='top', pady=(10, 0))

    def prepare_minecraft(self):
        """Prepare the Minecraft window and store it on the instance."""
        self.game = functionality.prepare_minecraft()
        if self.game:
            self.status_label.config(text='Minecraft prepared.')
        else:
            self.status_label.config(text='Minecraft not found.')

    def start(self):
        """Start the fishing loop in a background thread so the UI stays responsive."""
        if not self.game:
            self.status_label.config(text='Game not prepared. Press Prepare Minecraft first.')
            return

        self.status_label.config(text='Starting fishing... (hold x to stop)')
        t = threading.Thread(target=functionality.start, args=(self.game,), daemon=True)
        t.start()

    def run(self):
        self.root.mainloop()
