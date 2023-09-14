import tkinter as tk
from tkinter import ttk
import webbrowser

win = tk.Tk()
win.configure(bg="white")
win.title("login")
win.geometry("300x300")

input_frame = ttk.Frame()
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

#nama depan
input_label = ttk.Label(input_frame, text="nama depan:")
input_label.pack(padx=10, pady=10, fill="x", expand=True)

#kolom depan
NAMA_DEPAN = tk.StringVar()
input_kolom_depan = ttk.Entry(input_frame, textvariable=NAMA_DEPAN)
input_kolom_depan.pack(fill="x", expand=True)

# nama belakang
input_label_belakang = ttk.Label(input_frame, text="nama belakang")
input_label_belakang.pack(padx=10, pady=10, fill="x", expand=True)

# kolom belakang
NAMA_BELAKANG = tk.StringVar()
input_kolom_belakang = ttk.Entry(input_frame, textvariable=NAMA_BELAKANG)
input_kolom_belakang.pack(fill="x", expand=True)

# tombol
def tombol_click():
    value = NAMA_DEPAN.get()
    value_1 = NAMA_BELAKANG.get()
    print(f"nama depan: {value}")
    print(f"nama belakang: {value_1}")
    print("log in sukses!!!")

    url = "https://www.instagram.com/ryxageneral/"
    webbrowser.open(url)
    

tombol = ttk.Button(input_frame, text="log in", command=tombol_click, style="TButton")
tombol.pack(padx=90, pady=10, fill="x", expand=True)

win.mainloop()