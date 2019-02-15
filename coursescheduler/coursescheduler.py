from interface import CourseScheduler
import os

def setapikey():
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, 'apikey.txt')) as f:
        key = f.read().strip()
        if key is not None and key != '':
            os.environ["UW_API_KEY"] = key

def main():
    setapikey()

    app = CourseScheduler()
    app.title('CourseScheduler')
    app.mainloop()

if __name__ == '__main__':
    main()
