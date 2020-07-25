Keyword = ['print','if','else','help','about','function','return','while','break','Console','use','put','input','Consolelog','output','test','try','elif','open','write','read','new','class','for','do','loop']
n = []
v = []
List = []
Dictionary = []
Error = ['>>> -Error, unknown error caused program to end.','>>> -Error, an error in a variable caused the program to end','>>> -Error, logic error','>> -Error, wrong keyword, unrecognized keyword','>>> -Error,program is missing:configuration,link,key cll,variable list,test file,test log,source code,please check whether thr configuration path is correct','>>> -Error, file read error','>>> -Error, wrong data type, possibly caused by: int+string','>>> -Error, missing parameter','[Important Error, program crash]','>>> -Hrlp error ,Unkown command ']
error2 = 0
none = ''
xhelp = [1,2,3,4,5,6,7,8,9]
ckey = ['put','listvalue','listerror','error','chelp','set','keylist','ckeylist','And More……']
#===============================================================================

#===============================================================================
print('XK [0.4.1 bate / 0.4.12] For Windows , The Developer : xk . use "help();" or "about;" to check the Using ,use the "list()" in "k"/"kx" have 2 list for you to use .')
print("    ========================================")
print("    |    XK interpreter          Ver 0.5.29|")
print("    |    Made By Xinkong                   |")
print("    |    USE Python                        |")
print("    |    PXK_SDK XK XKvm                   |")
print("    ========================================")

def put(text='',value=none):
    try:
        value1 = n.index(value)
        print(v[value1])
    except Exception:
        print(Error[2])
        error2 += 1
def numerror():
    print('Number of errors :' + str(error2))
def listvalue(list1=none,list2=none):
    if list1 == 'n':
        print(list(n))
    elif list2 =='v':
        print(list(v))
    else:
        print(Error[1])
def listerror():
    print(Error)
def error(number):
    try:
        print('Test Error' + Error[number])
    except Exception:
        print(Error[2])
        error2 += 1
def chelp(number):
    number = number -1
    try:
        if number == 1:
            print(xhelp[1])
        elif number == 2:
            print(xhelp[2])
        elif number == 3:
            print(xhelp[3])
        elif number == 4:
            print(xhelp[4])
        elif number == 5:
            print(xhelp[5])
        elif number == 6:
            print(xhelp[6])
        elif number == 7:
            print(xhelp[7])
        elif number == 8:
            print(xhelp[8])
        elif number == 9:
            print(xhelp[9])
        else:
            print(Error[1])
    except Exception:
        print(Error[-1])
        error2 += 1
        
def keylist():
    print(Keyword)
def ckeylist():
    print(ckey)
   
def set(name,value=''):
    n.append(name)
    v.append(value)
def cfor(number,text,a='',b='',c=''):
    try:
        for i in range(number):
            print(text)
    except Exception:
        print(Error[-1])
        error2 += 1
def cif(a,b,c):
    if str(a) in n:
      
        x = n.index(a)
        a = v[x]
        print(a)
    try:
        b = str(b)
     
        if b == '>':
            a = int(a)
            c = int(c)
            if a > c:
                print('True')
            else:
                print('False')
        elif b == '<':
            a = int(a)
            c = int(c)
            if a < c:
                print('True')
            else:
                print('False')
        elif b == '=':
            a = int(a)
            c = int(c)
            if a == c:
                print('True')
            else:
                print('False')
        elif b == 'in':
            a = str(a)
            c = str(c)
            if a in c:
                print('True')
            else:
                print('False')
        elif b == 'notin':
            a = str(a)
            c = str(c)
            if a not in  c:
                print('True')
            else:
                print('False')
        else:
            print('Error')
    except Exception:
        print(Error[-1])
        error2 += 1

             
            
