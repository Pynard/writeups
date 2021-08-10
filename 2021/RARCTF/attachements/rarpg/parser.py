
import binascii

def parse(data,out):
    if len(data) != 198:
        return data

    if out:
        print('--> ',end='')
    else:
        print('<-- ',end='')

    data = data.replace(b'W',b' ')
    print(data)

    return data
