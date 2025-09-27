f=open ('demo.txt','x')

def readingFile(f):
    try:
        print (f.read())
    except FileNotFoundError:
        print('File not exists')
    else:
        print (f.read())
    finally:
     f.close()

readingFile(f)
