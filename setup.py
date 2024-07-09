# import sys
# import os
# from cx_Freeze import setup, Executable

# # ADD FILES
# files = ['icon.ico','themes/']

# # TARGET
# target = Executable(
#     script="main.py",
#     base="Win32GUI",
#     icon="icon.ico"
# )

# # SETUP CX FREEZE
# setup(
#     name = "PyDracula",
#     version = "1.0",
#     description = "Modern GUI for Python applications",
#     author = "Wanderson M. Pimenta",
#     options = {'build_exe' : {'include_files' : files}},
#     executables = [target]
    
#

from cx_Freeze import setup, Executable

setup(
    name = "chatclient",
    version = "0.1",
    description = "chatclient prototype",
    options = {
        "build_exe": {
            "packages": ["PySide6"],
            "excludes": ["PyQt6"]
        }
    },
    executables = [Executable("main.py")]
)

# python setup.py build