# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 18:31:17 2020

@author: SARVESH
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 23:48:03 2020
@author: SARVESH
"""

isa={
     'beq' :{'opcode':'1100011', 'fun3':'000'},
     'bne' :{'opcode':'1100011', 'fun3':'001'},
     'blt' :{'opcode':'1100011', 'fun3':'100'},
     'bge' :{'opcode':'1100011', 'fun3':'101'}
     }

class MyException(Exception):
    pass

def SB_format(instruction):
    instruction=instruction.replace(" ",",")
    instruction_arr=instruction.split(",")
    
    while "" in instruction_arr:
        instruction_arr.remove("")
        
    ############################################################################
    if(len(instruction_arr)!=4):
        raise MyException("Expected three arguements!")
    try:
        int(instruction_arr[3])
    except:
        raise MyException("Offset Value must be an Integer!")
    if int(instruction_arr[3]) > 4094 or int(instruction_arr[3]) < -4096:
        raise MyException("Immediate value out of bounds!")
   ###############################################################################
     
    machine_code=[]
    if (int(instruction_arr[3]))>=0:
        immediate=bin(int(instruction_arr[3])).replace("0b","").rjust(12,'0')
    else:
        immediate=bin(2**12+int(instruction_arr[3])).replace("0b","").rjust(12,'0')
    
    immediate_rev=immediate[::-1]
    
    instruction_arr[1]=instruction_arr[1].replace('x','')
    instruction_arr[2]=instruction_arr[2].replace('x','')
    
    #########################
    if(int(instruction_arr[1])>31 or int(instruction_arr[2])>31):
        raise MyException("Register number must be between 0 and 31, both inclusive.")
    #########################

    machine_code.append(immediate_rev[11])
    machine_code.append(immediate_rev[10:4:-1])
    machine_code.append(bin(int(instruction_arr[2])).replace("0b", "").rjust(5, '0'))
    machine_code.append(bin(int(instruction_arr[1])).replace("0b", "").rjust(5, '0'))
    machine_code.append(isa[instruction_arr[0]]['fun3'])
    machine_code.append(immediate_rev[4:0:-1])
    machine_code.append(immediate_rev[10])
    machine_code.append(isa[instruction_arr[0]]['opcode'])
    #print(machine_code)
    while "" in machine_code:
        machine_code.remove("")
        
    machine_bin=machine_code[0]+machine_code[1]+machine_code[2]+machine_code[3]+machine_code[4]+machine_code[5]+machine_code[6]+machine_code[7]
    machine_hex="{:08x}".format((int(machine_bin,2)))
    return "0x" + machine_hex
    
#print(SB_format("bge x0 x0 -4"))