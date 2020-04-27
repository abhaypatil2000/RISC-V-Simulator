import re
# class IncorrectArgumentError(Error):
#     pass
def R_Format(input):
    mnemonics = {'add':['0110011','000','0000000'],'and':['0110011','111','0000000'],'or':['0110011','110','0000000'], 'sll':['0110011','001','0000000'],'slt':['0110011','010','0000000'],'sra':['0110011','101','0100000'],'srl':['0110011','101','0000000'],'sub':['0110011','000','0100000'],'xor':['0110011','100','0000000'],'mul':['0110011','000','0000001'],'div':['0110011','100','0000001'],'rem':['0110011','110','0000001']}
    input = (input.split('#'))[0]
    x = re.compile(r'^\s*(?P<mnemonic>\w+)\s+(x(?P<rd>\d+)\s*((,|\s)\s*x(?P<rs1>\d+)\s*((,|\s)\s*x(?P<rs2>[0-31])\s*)?)?)?$')
    y = x.search(input)
    if y == None:
        print('Error in statement: ',input)
        return
    elif y.group('rd') == None:
        print('Expected 3 arguments found none')
        return
    elif int(y.group('rd')) > 31 or (y.group('rd')[0] == '0' and y.group('rd') != '0'):
        print('Register x' + y.group('rd') + ' is not recognized')
        return
    elif y.group('rs1') == None:
        print('Expected 3 arguments but got 1')
        return
    elif int(y.group('rs1')) > 31 or (y.group('rs1')[0] == '0' and y.group('rs1') != '0'):
        print('Register x' + y.group('rs1') + ' is not recognized')
        return
    elif y.group('rs2') == None:
        print('Expected 3 arguments but got 2')
        return
    elif int(y.group('rs1')) > 31 or (y.group('rs2')[0] == '0' and y.group('rs2') != '0'):
        print('Register x' + y.group('rs2') + ' is not recognized')
        return
    else:
        if y.group('mnemonic') not in mnemonics.keys():
            print(y.group('mnemonic') + ' is not supported')
            return
        else:
            z = mnemonics[y.group('mnemonic')]
            opcode = z[0]
            func3 = z[1]
            func7 = z[2]
            rd = "{:05b}".format(int(y.group('rd')))
            rs1 = "{:05b}".format(int(y.group('rs1')))
            rs2 = "{:05b}".format(int(y.group('rs2')))
            machine_hex='0x'+"{:08x}".format(int(func7 + rs2 + rs1 + func3 + rd + opcode,2))
            return machine_hex
