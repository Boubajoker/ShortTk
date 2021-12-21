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

short_tk.Err("MyApp:", "A test Error!")
                ^^^
short_tk.Warn("MyApp:", "A test Warning!")
                ^^^^
short_tk.Info("MyApp:", "A test Info.")
                ^^^^
short_tk.Loop()
```

check short_tk docs too ! https://boubajoker.github.io/ShortTk/
