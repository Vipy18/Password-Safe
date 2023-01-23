import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need more details.
build_exe_options = {"packages": ["os", "PyQt6", "pandas"], "excludes": ["tkinter"],'include_files':[('icon.ico', 'image/image.png')]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Password-Safe",
        version = "0.1",
        description = "A Safe which stores your Password for YOU!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("main.py", base=base,icon='icon.ico')])