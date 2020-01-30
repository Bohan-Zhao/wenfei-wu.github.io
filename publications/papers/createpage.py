

def GetFileList():
    from os import listdir
    from os.path import isfile, join
    mypath = './'
    #print listdir(mypath)
    return  [f for f in listdir(mypath)]
    #return  [f for f in listdir(mypath) if isfile(join(mypath, f))]

def CreatePage(files):
    links = ''
    for f in files:
        if f.strip() == 'index.html' or f.strip() == 'createpage.py':
            continue
        links += '    <a href="%s" target="_blank">%s</a><br>\n' % (f, f)

    t1 = '''
<html>
  <header>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>Download Page</title>
  </header>
  <body>
'''
    t2 = '''  </body>
</html>
    '''
    content = t1+links+t2
    f = open('index.html', 'w')
    f.write(content)
    f.close()

if __name__=='__main__':
    files = GetFileList()
    CreatePage(files)