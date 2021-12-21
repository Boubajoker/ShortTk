# ShortTk

A python module that shorts the Tkinter root setup.

## How to install ShortTk ?

To install ShortTk go to <a href="https://boubajoker.github.io/ShortTk">ShortTk Online web page</a> and downlaod the "last realese of ShortTk requied Tools".
Then, extract the requied tools in your project and execute 'DownlaodRealeses.py' and then type 'setup --setup' in the terminal input if you have'nt installed the module 'request'. And Then restart the shell and type 'short_tk --update', it will downlaod the last stable realese of short_tk. Then extract the 'short_tk.zip' file and the setup is finished ! 

## How To Use ShortTk ?

Make sure tkinter and <a href="#Requied Tools">Requied Tools</a> are installed.

To setup a simple window based on tkinter, it's very simple.

1. Create a new python file

2. import the module 'short_tk' with copy and past it or downlaod it to your project.

3. Setup a window with the following porperty in the module:
```python
import short_tk

short_tk.Window(root_title="MyApp", root_size="700x500", root_bg="#fff")

short_tk.Window.Loop(loop=True)
```

more info at <a href="FeaturesContribution.md">FeaturesContribution.md</a>.

## Requied Tools

- Python 3.8.10
- pip 21.3.1
- git 2.33.1
- Tkinter tcl/Tk components

## To make sure all the requied tools is installed:

### for tkinter:

1. type the following command in your system terminal:

```PowerShell
pip install -i tkinter
```

If it says: "Requirements allready exsist" Tkinter is already installed.
Else it will downlaod it to the Pypi platform.

### for python

1. type the following command in your system terminal:

```PowerShell
python -V
```

2. You should have a result like this:

```PowerShell
Python 3.8.10
```

### for pip

1. type the following command in your system terminal:

```PowerShell
pip -V
```

2. you must have a result like this:

```
pip 21.3.1 from C:\Users\{Username}\AppData\Roaming\Python\Python38\site-packages\pip (python 3.8)
```

### for git

1. type the following command in your system terminal:

```PowerShell
git --version
```

2. you must have a result like this:

```PowerShell
git version 2.33.1.windows.1
```