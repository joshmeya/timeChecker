def mainProgram():
    print("This is not your first time running the program.")

def firstTime():
    import time
    print("It looks like this is your first time running the program")

def firstChecker():
    from pathlib import Path
    import os

    firstFile = Path("lib/N8mops9")
    if firstFile.is_file():
        mainProgram()
    else:
        os.makedirs("lib")
        file = open("lib/N8mops9","a+")
        file.close()
        firstTime()

firstChecker()
