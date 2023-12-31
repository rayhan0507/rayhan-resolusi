import tkinter as tk
expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("error")
        expression = ""
def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
    gui = tk.Tk()
    gui.configure(bg="light green")
    gui.title("simple calculator")
    gui.geometry("460x300")
    equation = tk.StringVar()
    expression_field = tk.Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=170, ipady=10)
    
    button1 = tk.Button(gui, text='1', fg='black', bg='white', command=lambda: press(1), height=3, width=15)
    button1.grid(row=2, column=0)

    button2 = tk.Button(gui, text='2', fg='black', bg='white', command=lambda: press(2), height=3, width=15)
    button2.grid(row=2, column=1)

    button3 = tk.Button(gui, text='3', fg='black', bg='white', command=lambda: press(3), height=3, width=15)
    button3.grid(row=2, column=2)

    button4 = tk.Button(gui, text='4', fg='black', bg='white', command=lambda: press(4), height=3, width=15)
    button4.grid(row=3, column=0)

    button5 = tk.Button(gui, text='5', fg="black", bg="white", command=lambda: press(5), height=3, width=15)
    button5.grid(row=3, column=1)

    button6 = tk.Button(gui, text='6', fg='black', bg='white', command=lambda: press(6), height=3, width=15)
    button6.grid(row=3, column=2)

    button7 = tk.Button(gui, text='7', fg='black', bg='white', command=lambda: press(7), height=3, width=15)
    button7.grid(row=4, column=0)

    button8 = tk.Button(gui, text='8', fg='black', bg='white', command=lambda: press(8), height=3, width=15)
    button8.grid(row=4, column=1)

    button9 = tk.Button(gui, text='9', fg='black', bg='white', command=lambda: press(9), height=3, width=15)
    button9.grid(row=4, column=2)

    button0 = tk.Button(gui, text='0', fg='black', bg='white', command=lambda: press(0), height=3, width=15)
    button0.grid(row=5, column=0)

    plus = tk.Button(gui, text='+', fg='black', bg='white', command=lambda: press('+'), height=3, width=15)
    plus.grid(row=2, column=3)

    minus = tk.Button(gui, text='-', fg='black', bg='white', command=lambda: press('-'), height=3, width=15)
    minus.grid(row=3, column=3)

    multiply = tk.Button(gui, text='*', fg='black', bg='white', command=lambda: press('*'), height=3, width=15)
    multiply.grid(row=4, column=3)

    divide = tk.Button(gui, text='/', fg='black', bg='white', command=lambda: press('/'), height=3, width=15)
    divide.grid(row=5, column=3)

    clear = tk.Button(gui, text='Clear', fg='black', bg='white', command=clear, height=3, width=15)
    clear.grid(row=5, column=1)

    equal = tk.Button(gui, text='=', fg='black', bg='white', command=equalpress, height=3, width=15)
    equal.grid(row=5, column=2)

    decimal = tk.Button(gui, text='.', fg='black', bg='white', command=lambda: press('.'), height=3, width=15)
    decimal.grid(row=6, column=0)
     
    gui.mainloop()




































