import os

def setup():
    #May need installation
    try:
        from urllib.request import urlopen
    except ImportError:
        print("You do not have urllib! Installing it now!")
        os.system("python -m pip install urllib5")
    
    try:
        import requests
    except ImportError:
        print("You do not have requests! Installing it now!")
        os.system("python -m pip install requests")

    try:
        import flask
    except ImportError:
        print("You do not have requests! Installing it now!")
        os.system("python -m pip install flask")