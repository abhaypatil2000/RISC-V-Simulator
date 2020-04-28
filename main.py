from UJU_format import *
from I_Format import *
from R_Format import *
from SB_format import *
from S_Format import *
from common_backend import *
from Parser import *
from assembler_directives import *



line_no =0
class MyException(Exception):
    pass

dict = {
    'lui':{'type': 'UJU'},
    'auipc':{'type':'UJU'},
    'jal':{'type': 'UJU'},
    'sb': {'type': 'S'},
    'sh': {'type': 'S'},
    'sw': {'type': 'S'},
    'sd': {'type': 'S'},
    'addi': {'type': 'I'},
    'andi': {'type': 'I'},
    'ori': {'type': 'I'},
    'lb': {'type': 'I'},
    'ld': {'type': 'I'},
    'lh': {'type': 'I'},
    'lw': {'type': 'I'},
    'jalr': {'type': 'I'},
    'add':{'type':'R'},
    'and':{'type':'R'},
    'or':{'type':'R'},
    'sll':{'type':'R'},
    'slt':{'type':'R'},
    'sra':{'type':'R'},
    'srl':{'type':'R'},
    'sub':{'type':'R'},
    'xor':{'type':'R'},
    'mul':{'type':'R'},
    'div':{'type':'R'},
    'rem':{'type':'R'},
    'beq':{'type':'SB'},
    'bne':{'type':'SB'},
    'blt':{'type':'SB'},
    'bge':{'type':'SB'}
    }

def main1(file_name):
    global InstCount
    print("main1 called")
    file_read = open(file_name,"r")
    file_write = open("1.mc","w")
    file_write1 = open("output.mc","w")
    lines =file_read.readlines()
    lines=[val for val in lines if val!='\n']
    lines2 = []
    for line in lines:
        line2=line.replace('\n','')
        lines2.append(line2)
    lines = lines2.copy()
    lines = parseDoc(lines)
    #print(lines)
    lines3=[]
    global line_no
    for x in lines:
        oper= x.split()[0]
        #print (x)
        #print(oper)
        if('.' not in x and ':' not in x):
            if oper not in dict:
                 raise MyException('Error, unrecognized instruction')
            format_type=dict[oper]['type']
            #print(format_type)
            lines3.append('0x'+hex(line_no).replace("0x",'').rjust(8,'0'))
            line_no=line_no+4
            lines3.append(' ')
            if format_type=='S':
                y=S_Format(x)
                lines3.append(y)
            elif format_type=='R':
                y=R_Format(x)
                lines3.append(y)
            elif format_type=='I':
                y=I_Format(x)
                lines3.append(y)
            elif format_type=='SB':
                y=SB_format(x)
                lines3.append(y)
            elif format_type=='UJU':
                y=UJU_Format(x)
                lines3.append(y)
            else:
                raise MyException('Error, unrecognized instruction')
            lines3.append('\n')
    file_write.writelines(lines3)
    asmdirdict=asembler_directives()
    memptr='0x10000000'
    lines4=[]
    for p, q in asmdirdict.items():
    	lines4.append(hex(p)+' '+hex(q)+'\n')
    file_write.writelines(lines4)
    file_write1.writelines(lines3)
    file_read.close()
    file_write.close()
    file_write1.close()
    
    
    
#main1("input.txt")
#main3()
#print(InstCount)

