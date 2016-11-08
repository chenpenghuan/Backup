from sys import argv
from os import listdir,path
def find(file,keyword):
    global results
    global errors
    global selected
    try:
        if file.split('.')[-1] in selected:
            f=open(file)
            cont=f.read()
            f.close()
            if keyword in cont:
                results.append(file)
    except Exception as e:
        errors.append([file,str(e)])
def findstart(nowpath):
    files=listdir(nowpath)
    for file in files:
        filepath=nowpath+'/'+file
        if path.isdir(filepath):
            findstart(filepath)
        else:
            find(filepath,argv[2])
if __name__ == '__main__':
    global results
    global errors
    global selected
    results=[]
    errors=[]
    selected=argv[1].split(',')
    findstart('.')
    if len(results)>0:
        print('匹配文件：')
        for result in results:
            print(result)
    if len(errors)>0:
        print('异常文件：')
        for error in errors:
            print(error[0])
