def dns(file):
    f = open(file, 'rb')
    str = f.read()

    print(str[12:])

    list = []
    list.append('')
    count = 0
    for i in range(12, len(str)):
        if (hex(str[i])=='0x0'):
            i += 1
            list.append('')
            count += 1
            continue
        list[count] += chr(str[i])

    # удаление пустых
    # print(len(list))
    count=0
    for i in list:
        if(i == ''):
           count+=1
    for i in range(0,count):
        list.remove('')

    # print(len(list))

    print(list)
    alf = [chr(i) for i in range(43, 122)]

    tmp=''
    for j in list[0][1:]:
        if (j in alf):
            print (j, end='')
            tmp+=j
        else:
            print('.', end='')
            tmp+='.'
    print()
    # IP адрес

    if (list[1] == '\x01'):
        print('A',end='')
        tmp=[]
        count=0
        for i in range(12+len(tmp)+5, len(str)):
            if(hex(str[i])=='0x0' and hex(str[i+1])=='0x0'):
                i+=3
                if(len(tmp)>0 and count>1):
                    q=tmp[1:].index(0)
                    print('\nttl',int.from_bytes(tmp[1:q+1], byteorder='big', signed=False),end=' ')
                    print('ip',tmp[q+2],end=' ')
                    print(' : ',end=' ')
                    for i in range(q+3,q+3+4):
                        print(tmp[i],end='.')
                tmp=[]
                count += 1
                continue
            tmp.append(int(hex(str[i]),16))
        if (len(tmp) > 0 and count > 1):
            q = tmp[1:].index(0)
            print('\nttl', int.from_bytes(tmp[1:q + 1], byteorder='big', signed=False), end=' ')
            print('ip', tmp[q + 2], end=' ')
            print(' : ', end=' ')
            for i in range(q + 3, q + 3 + 4):
                print(tmp[i], end='.')
    # сервер DNS
    if(list[1] == '\x02'):
        print('NS',end='')
        tmp = []
        count = 0
        for i in range(12 + len(tmp) + 5, len(str)):
            if (hex(str[i]) == '0x0' and hex(str[i - 1]) == '0x0'):
                i += 2
                if (len(tmp) > 0 and count > 1):
                    q = tmp.index(0)
                    print('\nttl', int.from_bytes(tmp[:q], byteorder='big', signed=False), end=' ')

                    print(' : ', end=' ')
                    for i in range(q + 1, len(tmp)):
                        if (chr(tmp[i]) in alf):
                            print(chr(tmp[i]), end='')
                        else:
                            print('.', end='')
                tmp = []
                count += 1
                continue
            tmp.append(int(hex(str[i]), 16))
        if (len(tmp) > 0 and count > 1):
            q = tmp.index(0)
            print('\nttl', int.from_bytes(tmp[:q], byteorder='big', signed=False), end=' ')
            print(' : ', end=' ')
            for i in range(q + 1, len(tmp)):

                if (chr(tmp[i]) in alf):
                    print(chr(tmp[i]), end='')
                else:
                    print('.', end='')


    # запись об обмене почтой
    if (list[1] == '\x0f'):
        print('MX')
        tmp = []
        count = 0
        for i in range(12 + len(tmp) + 5, len(str)):
            if (hex(str[i]) == '0x0' and hex(str[i - 1]) == '0x0'):
                i += 2
                if (len(tmp) > 0 and count > 1):
                    q = tmp.index(0)
                    print('\nttl', int.from_bytes(tmp[:q], byteorder='big', signed=False), end=' ')
                    print('pr', tmp[q + 3], end=' ')
                    print(' : ', end=' ')
                    for i in range(q + 3,len(tmp)):
                        print(chr(tmp[i]),end='')
                tmp = []
                count += 1
                continue
            tmp.append(int(hex(str[i]),16))
        if (len(tmp) > 0 and count > 1):
            q = tmp.index(0)
            print('\nttl', int.from_bytes(tmp[:q], byteorder='big', signed=False), end=' ')
            print('pr', tmp[q + 3], end=' ')
            print(' : ', end=' ')
            for i in range(q + 3,len(tmp)):

                if (chr(tmp[i]) in alf):
                    print(chr(tmp[i]),end='')
                else:
                    print('.', end='')
    f.close()

def dhcp(file,op):
    f = open(file, 'rb')
    str = f.read()
    list=[]
    for i in str[236:]:
        list.append(hex(i))
    print(list)

    print('опция',op,list[op])
    f.close()