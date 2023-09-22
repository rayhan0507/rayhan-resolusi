
#login page
import tkinter as tk
import customtkinter
from PIL import ImageTk, Image

customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme("green")
app = customtkinter.CTk()
app.geometry("1200x1000")
app.title("LOG IN")

def fungsi_tombol():
    value1 = kolom1.get()
    value2 = kolom2.get()
    print('status LOG IN terkonfirmasi!')
    print(f'USERNAME: {value1}')
    print(f'PASSWORD: {value2}')

    app.destroy()
    w = customtkinter.CTk()
    w.geometry('900x700')
    w.title('welcome')
    l1 = customtkinter.CTkLabel(master=w, text="HOME PAGE", font=('Century Gostic', 80))
    l1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    l2 = customtkinter.CTkLabel(master=w, text="sedang perbaikan!", font=('Century Gostic', 20))
    l2.place(x=524, y=430)

    w.mainloop()

    

img1 = ImageTk.PhotoImage(Image.open("C:/Users/USER/Documents/pyhton vscode/project/GUI LOGIN PAGE/4230771.jpg"))
l1 = customtkinter.CTkLabel(master=app, image=img1)
l1.pack()

frame = customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=3)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

l2 = customtkinter.CTkLabel(master=frame, text="LOG IN TO YOUR ACCOUNT", font=('Century Gostic', 20))
l2.place(x=27, y=45)

kolom1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="USERNAME", corner_radius=7)
kolom1.place(x=48, y=100)

kolom2 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="PASSWORD", corner_radius=7, show="•")
kolom2.place(x=48, y=150)

l2 = customtkinter.CTkLabel(master=frame, text="Forgot your password?", font=('Century Gostic', 11, 'bold'))
l2.place(x=137, y=180)

tombol = customtkinter.CTkButton(master=frame, width=220, text="LOG IN", font=('Century Gostic', 11), command=fungsi_tombol)
tombol.place(x=48, y=230)

img2 = customtkinter.CTkImage(Image.open("C:/Users/USER/Documents/pyhton vscode/project/GUI LOGIN PAGE/Google__G__Logo.svg.webp").resize((20,20)))
img3 = customtkinter.CTkImage(Image.open("C:/Users/USER/Documents/pyhton vscode/project/GUI LOGIN PAGE/facebook-logo-1-2-1536x1536.png").resize((20,20)))

tombol2 = customtkinter.CTkButton(master=frame, image=img2, width=90, text="Google", compound='left', text_color="black", fg_color='white', hover_color="#AFAFAF")
tombol2.place(x=48, y=270)

tombol3 = customtkinter.CTkButton(master=frame, image=img3, width=90, text='Facebook', compound="left", text_color="white", fg_color='#4e77de', hover_color="#AFAFAF")
tombol3.place(x=168, y=270)
app.mainloop()
