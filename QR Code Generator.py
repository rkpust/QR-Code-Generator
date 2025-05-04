import tkinter as tk
import qrcode
import sys
import os
import io

from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk

# PyInstaller sets icon automatically
def resource_path(relative_path):
    """Get path to resource (for PyInstaller)"""
    try:
        base_path = sys._MEIPASS  # PyInstaller sets this
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Global QR image holder
qr_image = None

def generate_qr():
    global qr_image
    data = entry.get()
    if not data.strip():
        messagebox.showwarning("Input Error", "Please enter some text or URL.")
        return

    # Generate QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=2)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Convert to PhotoImage
    img_bytes = io.BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes.seek(0)
    qr_image = Image.open(img_bytes).resize((200, 200))
    tk_image = ImageTk.PhotoImage(qr_image)

    qr_label.config(image=tk_image)
    qr_label.image = tk_image  # Prevent GC
    save_btn.config(state='normal')

# Save qr code function
def save_qr():
    if qr_image:
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png")],
                                                 title="Save QR Code")
        if file_path:
            qr_image.save(file_path)
            messagebox.showinfo("Saved", f"QR code saved to:\n{file_path}")

# GUI setup
root = tk.Tk()
root.title("QR Code Generator")
icon_path = resource_path("RezaulKarim.ico")
root.iconbitmap(icon_path)
root.geometry("400x500")
root.resizable(False, False)

# Style
style = ttk.Style()
style.configure("TButton", font=("Segoe UI", 10))
style.configure("TLabel", font=("Segoe UI", 10))
style.configure("Header.TLabel", font=("Segoe UI", 14, "bold"))

# Widgets
ttk.Label(root, text="QR Code Generator", style="Header.TLabel").pack(pady=10)
ttk.Label(root, text="Enter text or URL below:").pack(pady=5)

entry = ttk.Entry(root, width=40)
entry.pack(pady=5)

ttk.Button(root, text="Generate QR Code", command=generate_qr).pack(pady=10)

qr_label = tk.Label(root)  # 🆕 Changed to tk.Label for image support
qr_label.pack(pady=10)

# 🆕 Frame to hold buttons side-by-side
btn_frame = ttk.Frame(root)
btn_frame.pack(pady=5)

save_btn = ttk.Button(btn_frame, text="💾 Save QR Code", command=save_qr, state='disabled')
save_btn.pack(side='left', padx=10)

# Run the app
root.mainloop()
