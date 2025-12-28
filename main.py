"""Entry point for Auto Fisher.

This file contains a minimal `main()` that starts the UI class defined in
`interface.py`.
"""

from interface import AutoFisherUI


def main():
    ui = AutoFisherUI()
    ui.run()


if __name__ == "__main__":
    main()