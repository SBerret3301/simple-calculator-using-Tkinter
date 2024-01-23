from tkinter import *

# Create the main window
root = Tk()
root.title("Calculator")
root.iconbitmap("C:\\Users\\salah\\Downloads\\calculator.ico")

# Create an Entry widget for displaying input and output
en = Entry(root, width=46, borderwidth=5)
en.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Initialize global variables
cal = None
f_num = 0

# Function to handle button clicks
def Button_click(number):
    current_num = en.get()
    en.delete(0, END)
    en.insert(0, str(current_num) + str(number))

# Functions to handle arithmetic operations
def Button_add():
    global cal, f_num
    cal = "add"
    f_num = int(en.get())
    en.delete(0, END)

def Button_mins():
    global cal, f_num
    cal = "mins"
    f_num = int(en.get())
    en.delete(0, END)

def Button_mult():
    global cal, f_num
    cal = "mult"
    f_num = int(en.get())
    en.delete(0, END)

def Button_devide():
    global cal, f_num
    cal = "div"
    f_num = int(en.get())
    en.delete(0, END)

# Function to clear the Entry widget
def clear():
    en.delete(0, END)

# Function to perform calculation and display the result
def button_Equal():
    if cal == "add":
        second_num = en.get()
        en.delete(0, END)
        en.insert(0, f_num + int(second_num))
    elif cal == "mins":
        second_num = en.get()
        en.delete(0, END)
        en.insert(0, f_num - int(second_num))
    elif cal == "mult":
        second_num = en.get()
        en.delete(0, END)
        en.insert(0, f_num * int(second_num))
    try:
        if cal == "div":
            second_num = en.get()
            en.delete(0, END)
            if second_num != 0:
                en.insert(0, f_num / int(second_num))
    except ZeroDivisionError:
        en.insert(0, "ERROR")

# Create Button widgets for digits and operations
my_button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: Button_click(1))
my_button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: Button_click(2))
my_button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: Button_click(3))
my_button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: Button_click(4))
my_button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: Button_click(5))
my_button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: Button_click(6))
my_button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: Button_click(7))
my_button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: Button_click(8))
my_button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: Button_click(9))
my_button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: Button_click(0))

button_add = Button(root, text="+", padx=39, pady=20, command=Button_add)
button_mins = Button(root, text="-", padx=40, pady=20, command=Button_mins)
button_equal = Button(root, text="=", padx=39, pady=57, command=button_Equal)
button_clear = Button(root, text="Clear", padx=82, pady=25, command=clear)
button_multiply = Button(root, text="x", padx=40, pady=20, command=Button_mult)
button_devide = Button(root, text="/", padx=41, pady=20, command=Button_devide)

# Place Button widgets on the grid
my_button_1.grid(row=3, column=0)
my_button_2.grid(row=3, column=1)
my_button_3.grid(row=3, column=2)

my_button_4.grid(row=2, column=0)
my_button_5.grid(row=2, column=1)
my_button_6.grid(row=2, column=2)

my_button_7.grid(row=1, column=0)
my_button_8.grid(row=1, column=1)
my_button_9.grid(row=1, column=2)

my_button_0.grid(row=4, column=1)
button_add.grid(row=4, column=0)
button_mins.grid(row=4, column=2)
button_equal.grid(row=5, column=2, rowspan=2)
button_clear.grid(row=6, column=0, columnspan=2)
button_multiply.grid(row=5, column=0)
button_devide.grid(row=5, column=1)

# Start the Tkinter event loop
root.mainloop()
