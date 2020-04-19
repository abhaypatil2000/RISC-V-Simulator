from common_backend import *

#use memory and data_ptr
#.byte, .half, .word, .dword, .asciiz


#
class UnknownAD(Exception):  #unknown assembler directive
    pass


class BigData(Exception):
    pass


class SntxErr(Exception):
    pass


dict = {}
ptr = 0x10000000


def asembler_directives():
    global ptr
    ptr = 0x10000000
    global dict
    dict.clear
    asmdirinp = open("input.txt", "r")
    inplist = asmdirinp.readlines()
    for lien in inplist:  #lien is line
        if (lien[-1] == '\n'):
            lien = lien[:-1]
        if ('.' in lien):
            while (':' in lien):
                lien = lien[1:]
            lien = lien.replace(" ", ",")
            lien_list = lien.split(',')
            while ("" in lien_list):
                lien_list.remove("")
            if (lien_list[0] != '.data' and lien_list[0] != '.text'):
                if (lien_list[0] == '.byte'):
                    lien_list.remove(lien_list[0])
                    data_list = lien_list
                    for data in data_list:
                        for ch in data:
                            if (ch not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
                                raise SntxErr("Not a decimal number")
                        if (int(data) < 0):
                            data = int(data)
                            data = data + pow(2, 8)
                            if (data < pow(2, 7)):  #128
                                raise BigData("data too big to fit")
                            data = str(data)
                        elif (int(data) >= pow(2, 7)):  #128
                            raise BigData("data too big to fit")
                        dict[ptr] = int(data)
                        ptr = ptr + 1
                elif (lien_list[0] == '.asciiz'):
                    lien_list.remove(lien_list[0])
                    data_list = lien_list
                    for data in data_list:
                        for ch in data[1:-1]:
                            dict[ptr] = ord(ch)
                            ptr = ptr + 1
                elif (lien_list[0] == '.half'):
                    lien_list.remove(lien_list[0])
                    data_list = lien_list
                    for data in data_list:
                        if (int(data) < 0):
                            data = int(data)
                            data = data + pow(2, 16)
                            if (data < pow(2, 15)):
                                raise BigData("data too big to fit")
                            data = str(data)
                        elif (int(data) >= pow(2, 15)):
                            raise BigData("data too big to fit")
                        dict[ptr] = int(data) % 0x100
                        ptr = ptr + 1
                        dict[ptr] = int(int(data) / 0x100) % 0x100
                        #dict[ptr] = int(int(data) % 0xffff) /
                        ptr = ptr + 1
                elif (lien_list[0] == '.word'):
                    lien_list.remove(lien_list[0])
                    data_list = lien_list
                    for data in data_list:
                        if (int(data) < 0):
                            data = int(data)
                            data = data + pow(2, 32)
                            if (data < pow(2, 31)):
                                raise BigData("data too big to fit")
                            data = str(data)
                        elif (int(data) >= pow(2, 31)):
                            raise BigData("data too big to fit")
                        dict[ptr] = int(data) % 0x100
                        ptr = ptr + 1
                        dict[ptr] = int(int(data) / 0x100) % 0x100
                        ptr = ptr + 1
                        dict[ptr] = int(int(data) / 0x10000) % 0x100
                        ptr = ptr + 1
                        dict[ptr] = int(int(data) / 0x1000000) % 0x100
                        ptr = ptr + 1
                elif (lien_list[0] == '.dword'):
                    lien_list.remove(lien_list[0])
                    data_list = lien_list
                    for data in data_list:
                        if (int(data) < 0):
                            data = int(data)
                            data = data + pow(2, 64)
                            if (data < pow(2, 63)):
                                raise BigData("data too big to fit")
                            data = str(data)
                        elif (int(data) >= pow(2, 63)):
                            raise BigData("data too big to fit")
                        dict[ptr] = int(data) % 0x100
                        ptr = ptr + 1
                        dict[ptr] = int(int(data) / 0x100) % 0x100
                        ptr = ptr + 1
                        dict[ptr] = int(int(data) / 0x10000) % 0x100
                        ptr = ptr + 1
                        dict[ptr] = int(int(data) / 0x1000000) % 0x100
                        ptr = ptr + 1
                        dict[ptr] = int(int(data) / 0x100000000) % 0x100
                        ptr = ptr + 1
                        dict[ptr] = int(int(data) / 0x10000000000) % 0x100
                        ptr = ptr + 1
                        dict[ptr] = int(int(data) / 0x1000000000000) % 0x100
                        ptr = ptr + 1
                        dict[ptr] = int(int(data) / 0x100000000000000) % 0x100
                        ptr = ptr + 1
                else:
                    raise UnknownAD("unknown assembler directive")
                    #unrecognised assembler directive
    return dict
    asmdirinp.close()


#asembler_directives()
