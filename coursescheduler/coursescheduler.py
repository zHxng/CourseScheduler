from interface import setgui
import os

def setapikey():
    with open('apikey.txt') as f:
    key = f.read()
    if key is not None and key != '':
        os.environ["UW_API_KEY"] = key

def main():
    setapikey()
    setgui()

if __name__ == '__main__':
    main()
