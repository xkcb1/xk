a = input('>>>>')
if a[0:3] == 'for':
    a2 = a.partition('=')
    k2 = int(a2[2].lstrip())
    k3 = a.partition('print: ')
    k4 = str(a2[2].listrip())
    for i in range(k2):
        print(k4)
