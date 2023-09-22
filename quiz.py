
import tkinter as tk
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme('green')

class QuizPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x400')
        # Menghitung lebar dan tinggi layar monitor
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        # Mengatur lebar dan tinggi jendela
        window_width = 400
        window_height = 400
        
        # Menghitung posisi x dan y untuk membuat jendela muncul di tengah
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        self.geometry(f'{window_width}x{window_height}+{x}+{y}')  # Mengatur geometri jendela
        self.title("quiz")
        
        self.frame = customtkinter.CTkFrame(master=self, width=360, height=320, corner_radius=10)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        self.no_soal = customtkinter.CTkLabel(master=self, text='Soal No 1', font=('Century Gostic', 15, 'bold'))
        self.no_soal.place(x=21, y=10)
        
        self.label = customtkinter.CTkLabel(master=self.frame, text='1 + 1 = ?', font=('Century Gostic', 30))
        self.label.place(x=120, y=10)
        
        self.button3 = customtkinter.CTkButton(master=self.frame, text='3', width=300, height=40, command=self.tombol3)
        self.button3.place(x=30, y=90)
        self.button2 = customtkinter.CTkButton(master=self.frame, text='2', width=300, height=40, command=self.tombol2)
        self.button2.place(x=30, y=140)
        self.button1 = customtkinter.CTkButton(master=self.frame, text='1', width=300, height=40, command=self.tombol1)
        self.button1.place(x=30, y=190)
        self.button4 = customtkinter.CTkButton(master=self.frame, text='4', width=300, height=40, command=self.tombol4)
        self.button4.place(x=30, y=240)
    
    def tombol3(self):
        self.label.configure(text='JAWABAN SALAH!', font=('Century Gostic', 30, 'bold'))
        self.label.place(x=45, y=10)
        print('Jawaban Anda Salah')

    def tombol1(self):
        self.label.configure(text='JAWABAN SALAH!', font=('Century Gostic', 30, 'bold'))
        self.label.place(x=45, y=10)
        print('Jawaban Anda Salah')

    def tombol4(self):
        self.label.configure(text='JAWABAN SALAH!', font=('Century Gostic', 30, 'bold'))
        self.label.place(x=45, y=10)
        print('Jawaban Anda Salah')

    def tombol2(self):  # menuju halaman 2
        print('Jawaban Anda Benar')
        print('lanjutkan')
        self.destroy()
        page2 = QuizPage2()
        page2.mainloop()

class QuizPage2(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('quiz')
        # Menghitung lebar dan tinggi layar monitor
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        # Mengatur lebar dan tinggi jendela
        window_width = 400
        window_height = 400
        
        # Menghitung posisi x dan y untuk membuat jendela muncul di tengah
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        self.geometry(f'{window_width}x{window_height}+{x}+{y}')  # Mengatur geometri jendela

        customtkinter.set_appearance_mode('light')
        customtkinter.set_default_color_theme('blue')

        self.frame2 = customtkinter.CTkFrame(master=self, width=360, height=320, corner_radius=10)
        self.frame2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.no_soal2 = customtkinter.CTkLabel(master=self, text='Soal No 2', font=('Century Gostic', 15, 'bold'))
        self.no_soal2.place(x=21, y=10)

        self.label2 = customtkinter.CTkLabel(master=self.frame2, text='16 - 8 = ?', font=('Century Gostic', 30,))
        self.label2.place(x=120, y=10)

        self.button11 = customtkinter.CTkButton(master=self.frame2, text='11', width=300, height=40, command=self.tombol11)
        self.button11.place(x=30, y=90)
        self.button7 = customtkinter. CTkButton(master=self.frame2, text='7', width=300, height=40, command=self.tombol7)
        self.button7.place(x=30, y=140)
        self.button24 = customtkinter. CTkButton(master=self.frame2, text='24', width=300, height=40, command=self.tombol24)
        self.button24.place(x=30, y=190)
        self.button8 = customtkinter. CTkButton(master=self.frame2, text='8', width=300, height=40, command=self.tombol8)
        self.button8.place(x=30, y=240)

    def tombol11(self):
        self.label2.configure(text='JAWABAN SALAH!', font=('Century Gostic', 30, 'bold'))
        self.label2.place(x=45, y=10)
        print('Jawaban Anda Salah')

    def tombol7(self):
        self.label2.configure(text='JAWABAN SALAH!', font=('Century Gostic', 30, 'bold'))
        self.label2.place(x=45, y=10)
        print('Jawaban Anda Salah')

    def tombol24(self):
        self.label2.configure(text='JAWABAN SALAH!', font=('Century Gostic', 30, 'bold'))
        self.label2.place(x=45, y=10)
        print('Jawaban Anda Salah')

    def tombol8(self):    #menuju halaman 3
        self.destroy()
        page3 = Quizpage3()
        page3.mainloop()
        
        print('Jawaban Anda Benar')
        print('lanjutkan')

class Quizpage3(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('quiz')
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        window_width = 400
        window_height = 400
        
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        self.geometry(f'{window_width}x{window_height}+{x}+{y}')  
        
        customtkinter.set_appearance_mode('light')
        customtkinter.set_default_color_theme('green')

        self.frame3 = customtkinter.CTkFrame(master=self, width=360, height=320, corner_radius=10)
        self.frame3.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
       
        self.no_soal_3 = customtkinter.CTkLabel(master=self, text='Soal No 3', font=('Century Gostic', 15, 'bold'))
        self.no_soal_3.place(x=21, y=10)

        self.label_3 = customtkinter.CTkLabel(master=self.frame3, text='8 x 4 = ?', font=('Century Gostic', 30))
        self.label_3.place(x=120, y=10)

        self.button_12 = customtkinter.CTkButton(master=self.frame3, width=300, height=40, text='12', corner_radius=10, command=self.tombol12)
        self.button_12.place(x=30, y=90)

        self.button_24 = customtkinter.CTkButton(master=self.frame3,  width=300, height=40, text='24', corner_radius=10, command=self.tombol24)
        self.button_24.place(x=30, y=140)

        self.button_32 = customtkinter.CTkButton(master=self.frame3, width= 300, height=40, text='32', corner_radius=10, command=self.tombol32)
        self.button_32.place(x=30, y=190)

        self.button_36 = customtkinter.CTkButton(master=self.frame3, width=300, height=40, text='36', corner_radius=10, command=self.tombol36)
        self.button_36.place(x=30, y=240)

    def tombol12(self):
        self.label_3.configure(text='JAWABAN SALAH!', font=('Century Gostic', 30, 'bold'))
        self.label_3.place(x=45, y=10)
        print('Jawaban Anda Salah')
        print('Coba Lagi')

    def tombol24(self):
        self.label_3.configure(text='JAWABAN SALAH!', font=('Century Gostic', 30, 'bold'))
        self.label_3.place(x=45, y=10)
        print('Jawaban Anda Salah')
        print('Coba Lagi')

    def tombol36(self):
        self.label_3.configure(text='JAWABAN SALAH!', font=('Century Gostic', 30, 'bold'))
        self.Label_3.place(x=45, y=10)
        print('Jawaban Anda Salah')
        print('Coba Lagi')

    def tombol32(self):
        self.destroy()
        print('Jawaban Anda Benar')
        print('lanjutkan')
        page4 = Quizpage4()
        page4.mainloop

class Quizpage4(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('quiz')
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        window_width = 400
        window_height = 400
        
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        self.geometry(f'{window_width}x{window_height}+{x}+{y}') 

        customtkinter.set_appearance_mode('light')
        customtkinter.set_default_color_theme('blue')

        self.frame4 = customtkinter.CTkFrame(master=self, width=360, height=320, corner_radius=10)
        self.frame4.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.no_soal_4 = customtkinter.CTkLabel(master=self, text='Soal No 4', font=('Century Gostic', 15, 'bold'))
        self.no_soal_4.place(x=21, y=10)

        self.label_4 = customtkinter.CTkLabel(master=self.frame4, text='96/6 = ?', font=('Century Gostic', 30))
        self.label_4.place(x=120, y=10)

        self.button14 = customtkinter.CTkButton(master=self.frame4, text='14', width=300, height=40, corner_radius=10, command=self.tombol14)
        self.button14.place(x=30, y=90)
        self.button16 = customtkinter.CTkButton(master=self.frame4, text='16', width=300, height=40, corner_radius=10, command=self.tombol16)
        self.button16.place(x=30, y=140)
        self.button19 = customtkinter.CTkButton(master=self.frame4, text='19', width=300, height=40, corner_radius=10, command=self.tombol19)
        self.button19.place(x=30, y=190)
        self.button11 = customtkinter.CTkButton(master=self.frame4, text='11', width=300, height=40, corner_radius=10, command=self.tombol11)
        self.button11.place(x=30, y=240)

    def tombol14(self):
        self.label_4.configure(text='JAWABAN SALAH!', font=('Century Gostic', 30, 'bold'))
        self.label_4.place(x=45, y=10)
        print('Jawaban Anda Salah')
        print('Coba Lagi')

    def tombol19(self):
        self.label_4.configure(text='JAWABAN SALAH!', font=('Century Gostic', 30, 'bold'))
        self.label_4.place(x=45, y=10)
        print('Jawaban Anda Salah')
        print('Coba Lagi')
    
    def tombol11(self):
        self.label_4.configure(text='JAWABAN SALAH!', font=('Century Gostic', 30, 'bold'))
        self.label_4.place(x=45, y=10)
        print('Jawaban Anda Salah')
        print('Coba Lagi')

    def tombol16(self):
        self.destroy()
        print('Jawaban Anda Benar')
        print('lanjutkan')
        page5 = Quizpage5()
        page5.mainloop()
        
class Quizpage5(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('quiz')
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        window_width = 400
        window_height = 400
        
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        self.geometry(f'{window_width}x{window_height}+{x}+{y}')  
        
        customtkinter.set_appearance_mode('light')
        customtkinter.set_default_color_theme('green')

        self.frame5 = customtkinter.CTkFrame(master=self, width=360, height=320, corner_radius=10)
        self.frame5.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.no_soal_5 = customtkinter.CTkLabel(master=self, text='Soal No 5', font=('Century Gostic', 15, 'bold'))
        self.no_soal_5.place(x=21, y=10)

        self.label_5 = customtkinter.CTkLabel(master=self.frame5, text='3+4x3-11 = ?', font=('Century Gostic', 30, 'bold'))
        self.label_5.place(x=90, y=10)

        self.button4 = customtkinter.CTkButton(master=self.frame5, text='4', width=300, height=40, corner_radius=10, text_color='black', fg_color='white', hover_color='#AFAFAF', command=self.tombol4)
        self.button4.place(x=30, y=90)
        self.button8 = customtkinter.CTkButton(master=self.frame5, text='8', width=300, height=40, corner_radius=10, text_color='white', fg_color='#1859db', hover_color='#AFAFAF', command=self.tombol8)
        self.button8.place(x=30, y=140)
        self.button2 = customtkinter.CTkButton(master=self.frame5, text='2', width=300, height=40, corner_radius=10, text_color='#80db18', fg_color='#088c34' , hover_color='#AFAFAF', command=self.tombol2)
        self.button2.place(x=30, y=190)
        self.button14 = customtkinter.CTkButton(master=self.frame5, text='14', width=300, height=40, corner_radius=10, text_color='white', fg_color='#2e2e2d', hover_color='#AFAFAF', command=self.tombol14)
        self.button14.place(x=30, y=240)

    def tombol8(self):
      self.label_5.configure(text='JAWABAN SALAH!', font=('Century Gostic', 30, 'bold'))
      self.label_5.place(x=45, y=10)
      print('Jawaban Anda Salah')
      print('Coba Lagi')

    def tombol2(self):
      self.label_5.configure(text='JAWABAN SALAH!', font=('Century Gostic', 30, 'bold'))
      self.label_5.place(x=45, y=10)
      print('Jawaban Anda Salah')
      print('Coba Lagi')

    def tombol14(self):
      self.label_5.configure(text='JAWABAN SALAH!', font=('Century Gostic', 30, 'bold'))
      self.label_5.place(x=45, y=10)
      print('Jawaban Anda Salah')
      print('Coba Lagi')

    def tombol4(self):
        self.destroy
        print('Jawaban Anda Benar')
        print('selamat Anda menyelesaikan quiz')
        page_tamat = Tamat()
        page_tamat.mainloop()

class Tamat(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('SELAMAT')
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
    
        window_width = 900
        window_height = 700
        
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        self.geometry(f'{window_width}x{window_height}+{x}+{y}')  

        customtkinter.set_appearance_mode('system')
        customtkinter.set_default_color_theme('blue')
        
        self.l1 = customtkinter.CTkLabel(master=self, text='ANDA LULUS', font=('Century Gostic', 30, 'bold'))
        self.l1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        

        





if __name__ == "__main__":
    app = QuizPage()
    app.mainloop()
