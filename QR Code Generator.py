import tkinter as tk
import sys
import os

# PyInstaller sets icon automatically
def resource_path(relative_path):
    """Get path to resource (for PyInstaller)"""
    try:
        base_path = sys._MEIPASS  # PyInstaller sets this
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# GUI setup
root = tk.Tk()
root.title("QR Code Generator")
icon_path = resource_path("RezaulKarim.ico")
root.iconbitmap(icon_path)
root.geometry("400x500")
root.resizable(False, False)

# Run the app
root.mainloop()
