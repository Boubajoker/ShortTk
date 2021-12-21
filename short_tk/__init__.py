r"""# ShortTk Module

A simple python module that shorten the Tkinter setup.

## Root variable

The root variable is the variable that contain the Tk() object from tkinter.
It can be used in elements placing for example:
```python
import short_tk

short_tk.Window(root_title=data, root_size=data, root_bg=data, root_favicon=data)

label = Label(short_tk.root, text="hello world!")
              ^^^^^^^^^^^^^
label.pack()   

short_tk.MainLoop()
```

## Window object

Window object is for generate simple window based on the Tk() object from tkinter.
Example:
```python
import short_tk

short_tk.Window(root_title=data, root_size=data, root_bg=data, root_favicon=data)
```

## Loop function

Loop function is for create a loop for the window, this function is based on the mainloop
porperty of Tkinter(Tcl/Tk components)
for example:
```python
import short_tk

short_tk.Window(root_title=data, root_size=data, root_bg=data, root_favicon=data)

# tkinter code 

short_tk.Loop()
         ^^^^
```

## Conf function [Beta]

Conf function is for configure the window based on the config property of Tkinter(Tcl/Tk components)
for example:
```python
import short_tk

short_tk.Window(root_title=data, root_size=data, root_bg=data, root_favicon=data)

# Tkinter code

short_tk.Window.Conf(data)
                ^^^^
short_tk.Window.Loop()
```

## Err, Warn, Info function
The Err, Warn and Info function is the functions that are based from the Tk() object from tkinter. For example:

```python
import short_tk
short_tk.Window(root_title=data, root_size=data, root_bg=data, root_favicon=data)

short_tk.Window.Err("MyApp:", "A test Error!")
                ^^^
short_tk.Window.Warn("MyApp:", "A test Warning!")
                ^^^^
short_tk.Window.Info("MyApp:", "A test Info.")
                ^^^^
short_tk.Window.Loop()
```

check short_tk docs too ! https://boubajoker.github.io/ShortTk/

"""

from tkinter import *
from tkinter import messagebox as _msgbox
from typing import Any, AnyStr
import random as _rndm
import sys as _sys

root = Tk()

#! Window object
class Window(object):    
    def __init__(self, root_title: str, root_size: str, root_bg=None, root_relief=None, root_favicon=None, root_update=None, *agrs, **kwagrs) -> AnyStr:
        super(Tk).__init__()
        """
        ## GenerateWindow object

        GenerateWindow object is for generate simple window based on Tk() object from tkinter.
        Example:
        >>> import short_tk
        >>> short_tk.GenerateWindow(root_title=data, root_size=data, root_bg=data, root_favicon=data)
        """

        root.title(root_title)
        root.geometry(root_size)
        root.config(bg=root_bg, relief=root_relief)
        root.iconbitmap(root_favicon)
        self.root = root
        self.root_size = root_size
        self.root_update = root_update
        
        if self.root_update:
            root.update()
        else:
            pass

        if self.root_size == '0x0':
            print("short_tk:[ERROR]: The window cannot be generated: '",self.root_size,"' is an invalid window value.")
            print("short_tk:[TIP]: pruposed height:", _rndm.randint(700, 1080),".And pruposed width:", _rndm.randint(500, 1920))
            quit()


    #! Loop function
    def Loop(loop=False) -> AnyStr:
        """
        ## Loop function

        Loop function is for create a loop for the window, this function is based on the mainloop
        porperty of Tkinter(Tcl/Tk components)
        Example:
        >>> import short_tk
        >>> short_tk.GenerateWindow(root_title=data, root_size=data, root_bg=data, root_favicon=data)
        >>> # tkinter code 
        >>> short_tk.Loop()
        """

        if loop:
            root.mainloop()
        else:
            pass
        
    #! Config function [Beta]
    def Conf(bg=None,*agrs, **kwagrs) -> AnyStr:
        """
        ## Conf function [Beta]
        Conf function is for configure the window
        """
        root.config(bg=bg)

#! Err function
def Err(title, content, *agrs, **kwagrs) -> AnyStr:
    """
    ## Err, Warn, Info function

    The Err, Warn and Info function is the functions that are based from the Tk() object from tkinter. For example:
    
    >>> import short_tk
    >>> short_tk.Window(root_title=data, root_size=data, root_bg=data, root_favicon=data)
    
    >>> short_tk.Window.Err("MyApp:", "A test Error!")
    >>> short_tk.Window.Warn("MyApp:", "A test Warning!")
    >>> short_tk.Window.Info("MyApp:", "A test Info.")
    
    >>> short_tk.Window.Loop()
    """
    _msgbox.showerror(title, content)

#! Warn function
def Warn(title, content, *agrs, **kwagrs) -> AnyStr:
    """
    ## Err, Warn, Info function

    The Err, Warn and Info function is the functions that are based from the Tk() object from tkinter. For example:
    
    >>> import short_tk
    >>> short_tk.Window(root_title=data, root_size=data, root_bg=data, root_favicon=data)
    
    >>> short_tk.Window.Err("MyApp:", "A test Error!")
    >>> short_tk.Window.Warn("MyApp:", "A test Warning!")
    >>> short_tk.Window.Info("MyApp:", "A test Info.")
    
    >>> short_tk.Window.Loop()
    """
    _msgbox.showwarning(title, content)

#! Info function
def Info(title, content, *agrs, **kwagrs) -> AnyStr:
    """
    ## Err, Warn, Info function
    
    The Err, Warn and Info function is the functions that are based from the Tk() object from tkinter. For example:
    
    >>> import short_tk
    >>> short_tk.Window(root_title=data, root_size=data, root_bg=data, root_favicon=data)
    
    >>> short_tk.Window.Err("MyApp:", "A test Error!")
    >>> short_tk.Window.Warn("MyApp:", "A test Warning!")
    >>> short_tk.Window.Info("MyApp:", "A test Info.")
    
    >>> short_tk.Window.Loop()
    """
    _msgbox.showinfo(title, content)

#// Zen object (easter-egg)
class Zen(object):
    def __init__(self) -> Any:
        super(object).__init__()
        print("A simple python module that shorten the Tkinter setup.")

print("Hello from the short_tk community ! Get started at: https://boubajoker.github.io/short_tk/. Happy Coding =)")

# Method 2 (organized stuff)
class VirtualMachine(Window):
    def __init__(self) -> Any:
        super(Window).__init__()
        def my_command() -> Any:
            lbl_2 = Label(root, text="Hello World !", font=('Arial', 20), bg="#fff", fg="#000")
            lbl_2.pack()

        Window(root_title="MyApp (Method 2)", root_size="700x500", root_bg="#fff")

        self.lbl_1 = Label(root, text="Hello World !", font=('Arial', 20), bg="#fff", fg="#000")
        self.lbl_1.pack()

        self.btn_1 = Button(root, text="Press Me !", font=('Arial', 20), bg="#fff", fg="#000", command=my_command)
        self.btn_1.pack()

        self.entry_1 = Entry()
        self.entry_1.pack()

        Err("MyApp:", "A test Error!")
        Warn("MyApp:", "A test Warning!")
        Info("MyApp:", "A test Info.")

        Window.Loop(loop=True)

__version__ = "0.0.1 Alpha A-1"
__all__ = [
    "shorten",
    "Tk/Tcl",
    "tkinter",
    "short_tk"
]
__doc__ = "https://boubajoker.github.io/short_tk/"

if __name__ == '__main__':
    VirtualMachine()