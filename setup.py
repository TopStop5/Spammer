from cx_Freeze import setup, Executable

base = None    

executables = [Executable("main.py", base=base)]

packages = ["idna", "pyautogui"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Python Spammer",
    options = options,
    version = "1.1",
    description = 'A Spammer coded in python',
    executables = executables
)