import short_tk
from tkinter import *
from typing import *

# See Ln.210, Col.1 in short_tk module (short_tk/__init__.py) module for the method 'organized stuff'

# Method 1 (basic stuff)
def my_command() -> Any:
    lbl_2 = Label(short_tk.root, text="Hello World !", font=('Arial', 20), bg="#fff", fg="#000")
    lbl_2.pack()

short_tk.Window(root_title="MyApp (Method 1)", root_size="700x500", root_bg="#fff", root_relief="groov")

lbl_1 = Label(short_tk.root, text="Hello World !", font=('Arial', 20), bg="#fff", fg="#000")
lbl_1.pack()

btn_1 = Button(short_tk.root, text="Press Me !", font=('Arial', 20), bg="#fff", fg="#000", command=my_command)
btn_1.pack()

entry_1 = Entry()
entry_1.pack()

short_tk.Err("MyApp:", "A test Error!")
short_tk.Warn("MyApp:", "A test Warning!")
short_tk.Info("MyApp:", "A test Info.")

short_tk.Window.Loop(loop=True)