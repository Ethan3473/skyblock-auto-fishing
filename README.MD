# Minecraft Skyblock Auto Fisher

Auto Fisher is a small utility to automate fishing in Minecraft Hypixel Skyblock (tested with an old 1.8.9 Skyclient client, may need tweaks for new versions). It resizes and focuses the game window, then uses pixel color detection and simulated mouse/keyboard events to automatically fish.

---

## Features

- Prepare and position the Minecraft window automatically
- Start an automated fishing loop that reacts to the fishing bobber color
- Stop the loop by holding the `x` key

---

## Requirements

- Windows (the script uses absolute screen coordinates and window management utilities)
- Python 3.8+
- The following packages (install via pip):
  - pyautogui
  - pygetwindow
  - keyboard

Install dependencies:

```bash
pip install pyautogui pygetwindow keyboard
```

---

## Usage

1. Run the app:

```bash
python main.py
```

2. In the UI click **Prepare Minecraft** so the script can find/position your Minecraft window.
3. Click **Start** to begin auto-fishing. Hold **x** for 2 seconds to stop.

> Note: The script may require slight configuration of pixel coordinates depending on display scaling or different game clients (tested with 1080p monitor resolution).

---

## Project structure

- `main.py` — Minimal entrypoint; starts the UI
- `interface.py` — `AutoFisherUI` class and tkinter UI
- `functionality.py` — Core automation functions (prepare window, fishing loop)
- `README.MD` — This file

---

## Disclaimer

Use at your own risk. Automating game interactions may violate server rules or terms of service. This project is for educational purposes.
