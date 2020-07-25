import re
import sys
kk = ['print','if','else','help','about','function','return','while','break','Console','use','put','input','Consolelog','output','test','try','elif','open','write','read','new','class','for','do','loop']
k = []
kx = []
List = []
Dictionary = []
Error = ['>>> -Error, unknown error caused program to end.','>>> -Error, an error in a variable caused the program to end','>>> -Error, logic error','>> -Error, wrong keyword, unrecognized keyword','>>> -Error,program is missing:configuration,link,key cll,variable list,test file,test log,source code,please check whether thr configuration path is correct','>>> -Error, file read error','>>> -Error, wrong data type, possibly caused by: int+string','>>> -Error, missing parameter','[Important Error, program crash]','>>> -Hrlp error ,Unkown command ']
error2 = 0
none = ''
xhelp = [1,2,3,4,5,6,7,8,9]
ckey = ['put','listvalue','listerror','error','chelp','set','keylist','ckeylist','And More……']
previousVariable =[]
import time
#========================================================================================
print('XK [0.4.1 bate / 0.4.12] For Windows , The Developer : xk . use "help();" or "about;" to check the Using ,use the "list()" in "k"/"kx" have 2 list for you to use .')
print("    ========================================")
print("    |    XK interpreter          Ver 0.5.29|")
print("    |    Made By Xinkong                   |")
print("    |    USE Python                        |")
print("    |    PXK_SDK XK XKvm                   |")
print("    ========================================")

time.sleep(0.3)
def a1():
    a = str(input('xk>'))
    previousVariable.append(a)
    if a[-1] == ';':
        if '=' in a or '+' in a or '-' in a or '*' in a or '/' in a or '%' in a :
            for i in range(len(a)):
                b = a[i:i+1]
                try:
                    if b == '=':
                       
                        
                            
                        a2 = a.partition('=')
                        k1 = str(a2[0].rstrip())
                        k2 = a2[2].lstrip()
                        
                        k.append(k1)
                        k22 = str(k2[:len(k2)-1])
                        kx.append(k22)
                
                    if b == '+':          
                        a2 = a.partition('+')
                        k1 = int(a2[0].rstrip())
                        k2 = a2[2].lstrip()
                    
                            
                        k.append(k1)
                        k22 = int(k2[:len(k2)-1])
                        kx.append(k22)
                        k3 = k1 + k22
                        print(k3)
                    if b == '-':
                        a2 = a.partition('-')
                        k1 = int(a2[0].rstrip())
                        k2 = a2[2].lstrip()
                        k.append(k1)
                        k22 = int(k2[:len(k2)-1])
                        kx.append(k22)
                        k3 = k1 - k22
                        print(k3)
                    if b == '/':
                        a2 = a.partition('/')
                        k1 = int(a2[0].rstrip())
                        k2 = a2[2].lstrip()
                        k.append(k1)
                        k22 = int(k2[:len(k2)-1])
                        kx.append(k22)
                        k3 = k1 / k22
                        print(k3)
                    if b == '*':
                        a2 = a.partition('*')
                        k1 = int(a2[0].rstrip())
                        k2 = a2[2].lstrip()
                        k.append(k1)
                        k22 = int(k2[:len(k2)-1])
                        kx.append(k22)
                        k3 = k1 * k22
                        print(k3)
                    if b == '%':
                        a2 = a.partition('%')
                        k1 = int(a2[0].rstrip())
                        k2 = a2[2].lstrip()
                        k.append(k1)
                        k22 = int(k2[:len(k2)-1])
                        kx.append(k22)
                        k3 = k1 % k22
                        print(k3)
                    if b == '<':
                        a2 = a.partition('<')
                        k1 = int(a2[0].rstrip())
                        k2 = a2[2].lstrip()
                        k.append(k1)
                        k22 = int(k2[:len(k2)-1])
                        kx.append(k22)
                        print(k1)
                        print(k22)
                        if k1 < k22:
                            print('True')
                        else:
                            print('False')
                except Exception:
                    print('  -XK-Console>>Error The Wrong > Unkonw Wrong <Appared in haer\n  -XK-Console>> Please check in "help()"\n  -XK-Console>> Maybe it is the value wrong:String and Int')
        elif a[0:7] == 'print:"' and a[-2:-1] == '"' and a[-1] == ';':
            print(a[7:-2])
        elif a[0:7] == "print:'" and a[-2:-1] == "'" and a[-1] == ';':
            print(a[7:-2])

        elif a[0:7] == 'exit(0)':
            exit(0)
        elif a[0:7] == 'exit(1)':
            exit(1)
        elif a[0:3] == 'for':
            a2 = a.partition('=')
            k2 = int(a2[2].lstrip())
            k3 = a.partition('print: ')
            k4 = str(a2[2].listrip())
            for i in range(k2):
                print(k4)
        elif a[0:6] == 'print:':
            try:
                qwq = a[6:-1]
                awa = k.index(qwq)
                qwq1 = kx[awa]
                print(qwq1)
            except Exception:
                print('  -XK-Console>> Error The Wrong > list > The "' +qwq + '"is not in list,please check the list()')
        elif a[0:4] == 'list':
            print(k)
            print(kx)
            print(Error)
            print(kk)
            print(List)
            print(Dictionary)
            print(error2)
            print(xhelp)
            print(ckey)
            print('none' + none)
            print('The previous Variable :' + previousVariable[-2])
        else:
            print('  -XK-Console>> Error The Wrong > Unkonw Wrong <Appared in haer,and check your Grammar\n  -XK-Console>> Please check in "help"') 
        a1()       
    else:
        print('  -XK-Console>> Error The Wrong > " '+ a + '" < Appared in hear')
        a1()
a1()
