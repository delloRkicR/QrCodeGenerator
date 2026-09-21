import ctypes
import os
import sys

import customtkinter as ctk
import qrcode
from PIL import Image
from tkinter import filedialog

ctk.set_appearance_mode("dark")

base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
logo_png = os.path.join(base, "logo.png")
logo_ico = os.path.join(base, "logo.ico")

W, H = 426, 582
KEY = "#010101"
BG = "#1c1c1c"
GRAY = "#2a2a2a"
GRAY_HOVER = "#363636"
WHITE = "#f2f2f2"
MUTED = "#8a8a8a"
#Code made by @delloRkicR

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("QR Code Generator")
        self.img = None

        self.overrideredirect(True)
        self.configure(fg_color=KEY)
        self.attributes("-transparentcolor", KEY)

        s = self._get_window_scaling()
        x = int((self.winfo_screenwidth() - W * s) / 2)
        y = int((self.winfo_screenheight() - H * s) / 2)
        self.geometry(f"{W}x{H}+{x}+{y}")

        card = ctk.CTkFrame(self, corner_radius=32, fg_color=BG)
        card.pack(fill="both", expand=True)
        self.header(card)
        self.inputs(card)

        self.preview = ctk.CTkLabel(
            card, text="Qr", text_color=MUTED,
            width=240, height=240, corner_radius=16, fg_color=GRAY,
            font=ctk.CTkFont(weight="bold", size=30)
        )
        self.preview.pack(pady=24)

        self.after(100, self.taskbar)
        self.after(300, lambda: self.iconbitmap(logo_ico))

    def header(self, card):
        ctk.CTkButton(
            card, text="X", width=32, height=32, corner_radius=16,
            fg_color="transparent", hover_color=GRAY, text_color=MUTED,
            command=self.destroy,
        ).place(relx=1.0, x=-22, y=18, anchor="ne")

        logo = ctk.CTkImage(Image.open(logo_png), size=(64, 64))
        icon = ctk.CTkLabel(card, image=logo, text="")
        icon.pack(pady=(40, 8))
        title = ctk.CTkLabel(
            card, text="QR Code Generator", text_color=WHITE,
            font=ctk.CTkFont(size=18, weight="bold"),
        )
        title.pack()

        for w in (card, icon, title):
            w.bind("<Button-1>", self.press)
            w.bind("<B1-Motion>", self.drag)

    def inputs(self, card):
        self.entry = ctk.CTkEntry(
            card, placeholder_text="https://www.example.com/", height=44, corner_radius=12,
            border_width=0, fg_color=GRAY, text_color=WHITE,
        )
        self.entry.pack(fill="x", padx=36, pady=(24, 12))
        self.entry.bind("<Return>", lambda e: self.generate())

        row = ctk.CTkFrame(card, fg_color="transparent")
        row.pack(fill="x", padx=36)
        row.grid_columnconfigure((0, 1), weight=1, uniform="a")

        ctk.CTkButton(
            row, text="Oluştur", height=44, corner_radius=12,
            fg_color=WHITE, hover_color="#cfcfcf", text_color=BG,
            command=self.generate,
        ).grid(row=0, column=0, padx=(0, 6), sticky="ew")

        self.btn_save = ctk.CTkButton(
            row, text="Kaydet", height=44, corner_radius=12,
            fg_color=GRAY, hover_color=GRAY_HOVER, text_color=WHITE,
            state="disabled", command=self.save,
        )
        self.btn_save.grid(row=0, column=1, padx=(6, 0), sticky="ew")

    def generate(self):
        text = self.entry.get().strip()
        if not text:
            return
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=2,
        )
        qr.add_data(text)
        qr.make(fit=True)
        self.img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

        big = self.img.resize((480, 480), Image.NEAREST)
        self.photo = ctk.CTkImage(light_image=big, size=(240, 240))
        self.preview.configure(image=self.photo, text="", fg_color="white")
        self.btn_save.configure(state="normal")

    def save(self):
        path = filedialog.asksaveasfilename(
            parent=self, defaultextension=".png", initialfile="qr.png",
            filetypes=[("PNG", "*.png")],
        )
        if path:
            self.img.save(path)

    def press(self, e):
        self.dx = e.x_root - self.winfo_x()
        self.dy = e.y_root - self.winfo_y()

    def drag(self, e):
        self.geometry(f"+{e.x_root - self.dx}+{e.y_root - self.dy}")

    def taskbar(self):
        user32 = ctypes.windll.user32
        hwnd = user32.GetParent(self.winfo_id())
        style = user32.GetWindowLongW(hwnd, -20)
        user32.SetWindowLongW(hwnd, -20, (style & ~0x80) | 0x40000)
        self.withdraw()
        self.after(10, self.deiconify)


if __name__ == "__main__":
    App().mainloop()