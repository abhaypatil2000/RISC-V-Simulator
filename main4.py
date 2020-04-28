#No data Forwarding

from bitstring import BitArray
from copy import deepcopy
from btb import *

prediction = 0  #TODO prediction changes the fetch and decode
#TODO STALL them when no prediction
#Buffer Registers
#{
#add PC to the registers as decode ,memory access, writebackneed it #TODO (DONE)
REGTEMP = {}
REGTEMP['Branch'] = 0
REGTEMP['MemRead'] = 0
REGTEMP['MemtoReg'] = 0
REGTEMP['MemWrite'] = 0
REGTEMP['ALUSrc1'] = 0
REGTEMP['ALUSrc2'] = 0
REGTEMP['RegWrite'] = 0
REGTEMP['ReadData1'] = 0
REGTEMP['ReadData2'] = 0
REGTEMP['ReadRegister1'] = 0
REGTEMP['ReadRegister2'] = 0
REGTEMP['WriteRegister'] = 0
REGTEMP['WriteDataRegFile'] = 0
REGTEMP['ImmGenOutput'] = 0
REGTEMP['ALUControl'] = 0
REGTEMP['ALU_input1'] = 0
REGTEMP['ALU_input2'] = 0
# REGTEMP['ReadAddress'] = 0
REGTEMP['Zero'] = 0
REGTEMP['LessThan'] = 0
REGTEMP['GE'] = 0
REGTEMP['ALUResult'] = 0
REGTEMP['Address'] = 0
REGTEMP['WriteData'] = 0
REGTEMP['ReadData'] = 0
REGTEMP['PC'] = 0
REGTEMP['BranchTaken'] = 0  #As decided by the branch prediction

RegFD = {}
RegDE = {}
RegEM = {}
RegMW = {}

for i, j in REGTEMP.items():
    RegFD[i] = j
    RegDE[i] = j
    RegEM[i] = j
    RegMW[i] = j

#}

#Flush
FLUSHDONE = 0
#Branching
BRANCHTOBETAKEN = 0
currSTATE='NT'
#Pipelining Registers
PipE = 0
PipM = 0
PipRegs = [PipE, PipM]

#DataForwarding
ForwardA = '00'
ForwardB = '00'

#Control Signals
# Branch = 0  #
# MemRead = 0  #
# MemtoReg = 0  #
# ALUOp = 0
# MemWrite = 0  #
# ALUSrc1 = 0  #
# ALUSrc2 = 0  #

#PC increament
PCSrc = -1  #If the PC is updated from the instruction
PCReg = 0  #Signal if the PC is updated by the Register value

#Register File inputs and Outputs
# RegWrite = 0  #
# ReadData1 = 0  #
# ReadData2 = 0  #
# ReadRegister1 = 0  #
# ReadRegister2 = 0  #
# WriteRegister = 0  #
# WriteDataRegFile = 0  #

#Immediate Generation
# ImmGenOutput = 0  #

#ALU Control
# ALUControl = 0  #

#ALUinputs
# ALU_input1 = 0  #
# ALU_input2 = 0  #

#PC
PC = 0

#Instruction Memory
ReadAddress = 0  #
InstructionF = '0' * 32
InstructionD = '0' * 32
InstructionE = '0' * 32
InstructionM = '0' * 32
InstructionW = '0' * 32

#ALU output
# Zero = 0  #
# LessThan = 0  #
# GE = 0  #
# ALUResult = 0  #

#Data Memory
# Address = 0  #
# WriteData = 0  #
# ReadData = 0  #

#Exit Signal
EXIT = False
#Registers
reg_file = {
    'x0': 0,
    'x1': 0,
    'x2': 0x7ffffffc,
    'x3': 0,
    'x4': 0,
    'x5': 0,
    'x6': 0,
    'x7': 0,
    'x8': 0,
    'x9': 0,
    'x10': 0,
    'x11': 0,
    'x12': 0,
    'x13': 0,
    'x14': 0,
    'x15': 0,
    'x16': 0,
    'x17': 0,
    'x18': 0,
    'x19': 0,
    'x20': 0,
    'x21': 0,
    'x22': 0,
    'x23': 0,
    'x24': 0,
    'x25': 0,
    'x26': 0,
    'x27': 0,
    'x28': 0,
    'x29': 0,
    'x30': 0,
    'x31': 0,
}

#clock
clock = 0

#TempMem
TempMem = {}


def initialize_mem():
    global TempMem
    TempMem.clear()
    fp = open("1.mc", "r+")
    for line in fp:
        inst = line.split()
        if (len(inst) != 2):
            break
        a = int(inst[0], 16)
        b = inst[1][2:]
        if (len(b) == 8):
            TempMem[a] = b[6:]
            TempMem[a + 1] = b[4:6]
            TempMem[a + 2] = b[2:4]
            TempMem[a + 3] = b[0:2]
        elif (len(b) == 4):
            TempMem[a] = b[2:]
            TempMem[a + 1] = b[0:2]
        else:
            TempMem[a] = b
    fp.close()


def exit_routine():
    global TempMem
    global clock
    fp = open("1.mc", "r+")
    for i in TempMem.keys():
        fp.write(hex(i) + " " + '0x' + TempMem[i] + '\n')
    fp.close()


def reset():
    initialize_mem()
    global reg_file
    reg_file = {
        'x0': 0,
        'x1': 0,
        'x2': 0x7ffffffc,
        'x3': 0,
        'x4': 0,
        'x5': 0,
        'x6': 0,
        'x7': 0,
        'x8': 0,
        'x9': 0,
        'x10': 0,
        'x11': 0,
        'x12': 0,
        'x13': 0,
        'x14': 0,
        'x15': 0,
        'x16': 0,
        'x17': 0,
        'x18': 0,
        'x19': 0,
        'x20': 0,
        'x21': 0,
        'x22': 0,
        'x23': 0,
        'x24': 0,
        'x25': 0,
        'x26': 0,
        'x27': 0,
        'x28': 0,
        'x29': 0,
        'x30': 0,
        'x31': 0,
    }
    global clock
    clock = 0


def read_byte(address):
    global TempMem
    if address in TempMem.keys():
        return TempMem[address]
    else:
        return '00'


def read_word(address):
    return read_byte(address + 3) + read_byte(address + 2) + read_byte(address + 1) + read_byte(address)


def read_hword(address):
    return read_byte(address + 1) + read_byte(address)


def write_byte(address, data):
    global TempMem
    TempMem[address] = data


def write_word(address, data):
    write_byte(address, data[6:])
    write_byte(address + 1, data[4:6])
    write_byte(address + 2, data[2:4])
    write_byte(address + 3, data[0:2])


def write_hword(address, data):
    write_byte(address, data[2:])
    write_byte(address + 1, data[0:2])


def read_dword(address):
    return read_word(address + 4) + read_word(address)


def write_dword(address, data):
    write_word(address, data[8:])
    write_word(address + 8, data[0:8])


def fetch():
    global RegDE  #as the PC is dependent on the last execute made
    global BRANCHTOBETAKEN
    global currSTATE
    #Control Signals
    # global Branch
    # global MemRead
    # global MemtoReg
    # ALUOp
    # global MemWrite
    # global ALUSrc1
    # global ALUSrc2
    global PCSrc
    global PCReg  #Signal if the PC is updated by the Register value

    #Register File inputs and Outputs
    # global RegWrite
    # global ReadData1
    # global ReadData2
    # global ReadRegister1
    # global ReadRegister2
    # global WriteRegister
    # global WriteDataRegFile

    #Immediate Generation
    # global ImmGenOutput

    #ALU Control
    # global ALUControl

    #ALUinputs
    # global ALU_input1
    # global ALU_input2

    #PC
    global PC

    #Instruction Memory
    global ReadAddress
    global InstructionF

    #ALU output
    # global Zero
    # global LessThan
    # global GE
    # global ALUResult

    #Data Memory
    # global Address
    # global WriteData
    # global ReadData

    #Registers
    global reg_file

    #clock
    global clock

    #TempMem
    global TempMem
    #Exit
    global EXIT
    
    if PC in btb:
         currSTATE=returnCurrentState(PC)
         if currSTATE!='NT':
             BRANCHTOBETAKEN=1
             UPDATEDPC=returnTakenAddress(PC)
         else:
             BRANCHTOBETAKEN=0
    
    
    if (BRANCHTOBETAKEN == 1):
        PC = UPDATEDPC
        BRANCHTOBETAKEN = 0
    elif (PCReg == 1):
        PC = RegDE['ALUResult']
        PCReg = 0
        PCSrc = 0

    elif (PCSrc == 0):
        PC = PC + 4

    elif (PCSrc == 1):
        PC = PC + (RegDE['ImmGenOutput'] << 1)

    if (RegDE['Branch'] != RegDE['BranchTaken']):
        flush()

    ReadAddress = PC  #TODO problem for the first two read instructions (DONE)
    PCSrc = 0  #This would make the next instruction to be the PC + 4
    PCReg = 0  #This would make the next instruction to be the PC + 4
    InstructionF = "{:032b}".format(int(read_word(ReadAddress), 16))

    #TODO add input from the prediction merge with Gurpreet
    #take the input in teh RegDE['ImmGenOutput']


def decode():
    global RegFD
    global BRANCHTOBETAKEN
    #Control Signals
    # global Branch
    # global MemRead
    # global MemtoReg
    #ALUOp
    # global MemWrite
    # global ALUSrc1
    # global ALUSrc2
    global PCSrc
    global PCReg  #Signal if the PC is updated by the Register value

    #Register File inputs and Outputs
    # global RegWrite
    # global ReadData1
    # global ReadData2
    # global ReadRegister1
    # global ReadRegister2
    # global WriteRegister
    # global WriteDataRegFile

    #Immediate Generation
    # global ImmGenOutput

    #ALU Control
    # global ALUControl

    #ALUinputs
    # global ALU_input1
    # global ALU_input2

    #PC
    global PC

    #Instruction Memory
    global ReadAddress
    global InstructionD

    #ALU output
    # global Zero
    # global LessThan
    # global GE
    # global ALUResult

    #Data Memory
    # global Address
    # global WriteData
    # global ReadData

    #Registers
    global reg_file

    #clock
    global clock

    #TempMem
    global TempMem
    #Exit
    global EXIT
    #Data Forwarding
    global ForwardA
    global ForwardB
    #Pipelining
    global PipE

    if (BRANCHTOBETAKEN == 1):
        RegFD['BranchTaken'] = 1
    if (EXIT):
        return
    if (int(InstructionD) == 0):
        return
    #  exit_routine()
    # if(int(InstructionD, 2) == 0):
    # EXIT = True
    else:
        RegFD['PC'] = PC
        opcode = InstructionD[25:]
        func3 = InstructionD[17:20]
        func7 = InstructionD[0:7]
        RegFD['ReadRegister1'] = int(InstructionD[12:17], 2)
        RegFD['ReadRegister2'] = int(InstructionD[7:12], 2)
        RegFD['WriteRegister'] = int(InstructionD[20:25], 2)
        RegFD['MemtoReg'] = 0
        RegFD['MemRead'] = 0
        RegFD['MemWrite'] = 0
        if (opcode == '0000011' or opcode == '0010011' or opcode == '1100111'):
            RegFD['ImmGenOutput'] = BitArray(bin=InstructionD[0:12]).int
            RegFD['ALUSrc2'] = 1
            if (opcode == '0000011'):
                RegFD['MemRead'] = int(func3, 2) + 1
            if (opcode == '0000011'):
                RegFD['MemtoReg'] = 1
            elif (opcode == '1100111'):
                RegFD['MemtoReg'] = 2
            RegFD['ALUSrc1'] = 0
        elif (opcode == '0100011'):
            RegFD['ImmGenOutput'] = BitArray(bin=InstructionD[0:7] + InstructionD[20:25]).int
            RegFD['MemWrite'] = int(func3, 2) + 1
            RegFD['ALUSrc2'] = 1
            RegFD['ALUSrc1'] = 0
        elif (opcode == '1100011'):    #branch
            RegFD['ImmGenOutput'] = BitArray(bin=InstructionD[0] + InstructionD[24] + InstructionD[1:7] + InstructionD[20:24]).int
            RegFD['ALUSrc2'] = 0
            RegFD['ALUSrc1'] = 0
            
            if PC not in btb:
                #prePC=PC
                offset = RegFD['ImmGenOutput'] << 1
                #PC = PC + offset
                if offset<0:
                    add_instruction(PC,PC+offset,'T')
                    RegFD['BranchTaken']=1
                else:
                    add_instruction(PC,PC+offset,'NT')
                    RegFD['BranchTaken']=0
                    
        elif (opcode == '0010111' or opcode == '0110111'):
            RegFD['ImmGenOutput'] = BitArray(bin=InstructionD[0:20]).int
            RegFD['ALUSrc2'] = 2
            RegFD['ALUSrc1'] = 1 if opcode == '0010111' else 2
        elif (opcode == '1101111'):     #jal
            RegFD['ImmGenOutput'] = BitArray(bin=InstructionD[0] + InstructionD[12:20] + InstructionD[11] + InstructionD[1:11]).int
            RegFD['ALUSrc2'] = 0
            RegFD['ALUSrc1'] = 0
            RegFD['MemtoReg'] = 2
            RegFD['Branch'] = 1
            
            if PC not in btb:
                add_instruction(PC,PC+(RegFD['ImmGenOutput'] << 1),'T')
                
        else:
            RegFD['ALUSrc2'] = 0
            RegFD['ALUSrc1'] = 0
        if (opcode == '1100011'):
            RegFD['Branch'] = int(func3, 2) + 2
        else:
            RegFD['Branch'] = 0
        PCReg = 1 if opcode == '1100111' else 0
        RegFD['RegWrite'] = 0 if opcode == '0100011' or opcode == '1100011' else 1
        if (opcode == '0110011'):
            if (func3 == '111'):
                RegFD['ALUControl'] = 1
            elif (func3 == '110'):
                RegFD['ALUControl'] = 2
            elif (func3 == '001'):
                RegFD['ALUControl'] = 3
            elif (func3 == '010'):
                RegFD['ALUControl'] = 4
            elif (func3 == '101' and func7 == '0100000'):
                RegFD['ALUControl'] = 5
            elif (func3 == '101'):
                RegFD['ALUControl'] = 6
            elif (func7 == '0100000' and func3 == '000'):
                RegFD['ALUControl'] = 7
            elif (func3 == '100'):
                RegFD['ALUControl'] = 8
            elif (func7 == '0000001' and func3 == '000'):
                RegFD['ALUControl'] = 9
            elif (func7 == '0000001' and func3 == '100'):
                RegFD['ALUControl'] = 10
            elif (func7 == '0000001' and func3 == '110'):
                RegFD['ALUControl'] = 11
            else:
                RegFD['ALUControl'] = 0
        elif (opcode == '1100111'):
            if (func3 == '111'):
                RegFD['ALUControl'] = 1
            elif (func3 == '110'):
                RegFD['ALUControl'] = 2
            elif (func3 == '001'):
                RegFD['ALUControl'] = 3
            else:
                RegFD['ALUControl'] = 0
        else:
            RegFD['ALUControl'] = 0
        if (opcode == '1100011' and (func3 == '000' or func3 == '001')):
            RegFD['ALUControl'] = 7

        checkExHazard()
        CheckMemHazard()

        RegFD['ReadData1'] = reg_file['x' + str(RegFD['ReadRegister1'])]
        RegFD['ReadData2'] = reg_file['x' + str(RegFD['ReadRegister2'])]

        if ForwardA == '10':
            RegFD['ReadData1'] = PipE
        elif ForwardA == '01':
            RegFD['ReadData1'] = PipM

        if ForwardB == '10':
            RegFD['ReadData2'] = PipE
        elif ForwardB == '01':
            RegFD['ReadData2'] = PipM


def checkExHazard():
    global ForwardA
    global ForwardB
    global RegDE
    global RegFD

    if ((RegDE['RegWrite'] == 1) and (RegDE['WriteRegister'] != 0) and (RegDE['WriteRegister'] == RegFD['ReadRegister1'])):
        ForwardA = '10'

    if ((RegDE['RegWrite'] == 1) and (RegDE['WriteRegister'] != 0) and (RegFD['WriteRegister'] == RegFD['ReadRegister2'])):
        ForwardB = '10'


def CheckMemHazard():
    global ForwardA
    global ForwardB
    global RegFD
    global RegEM
    global RegDE

    if (RegEM['RegWrite'] == 1 and RegEM['WriteRegister'] != 0 and not ((RegDE['RegWrite'] == 1) and (RegDE['WriteRegister'] != 0) and (RegDE['WriteRegister'] == RegFD['ReadRegister1'])) and RegEM['WriteRegister'] == RegFD['ReadRegister1']):
        ForwardA = '01'

    if (RegEM['RegWrite'] == 1 and RegEM['WriteRegister'] != 0 and not ((RegDE['RegWrite'] == 1) and (RegDE['WriteRegister'] != 0) and (RegDE['WriteRegister'] == RegFD['ReadRegister2'])) and RegEM['WriteRegister'] == RegFD['ReadRegister2']):
        ForwardB = '01'


def execute():
    global RegDE
    #Control Signals
    # global Branch
    # global MemRead
    # global MemtoReg
    # ALUOp
    # global MemWrite
    # global ALUSrc1
    # global ALUSrc2
    global PCSrc
    global PCReg  #Signal if the PC is updated by the Register value

    #Register File inputs and Outputs
    # global RegWrite
    # global ReadData1
    # global ReadData2
    # global ReadRegister1
    # global ReadRegister2
    # global WriteRegister
    # global WriteDataRegFile

    #Immediate Generation
    # global ImmGenOutput

    #ALU Control
    # global ALUControl

    #ALUinputs
    # global ALU_input1
    # global ALU_input2

    #PC
    global PC

    #Instruction Memory
    global ReadAddress
    global InstructionE

    #ALU output
    # global Zero
    # global LessThan
    # global GE
    # global ALUResult

    #Data Memory
    # global Address
    # global WriteData
    # global ReadData

    #Registers
    global reg_file

    #clock
    global clock

    #TempMem
    global TempMem

    #Instruction count
    global InstCount

    #Pipelining Regs
    global PipE
    #Exit
    global EXIT
    if (EXIT):
        return
    if (int(InstructionE) == 0):
        return
    if (RegDE['ALUSrc1'] == 0):
        RegDE['ALU_input1'] = RegDE['ReadData1']
    elif (RegDE['ALUSrc1'] == 1):
        RegDE['ALU_input1'] = 0
    else:
        RegDE['ALU_input1'] = RegDE['PC']
    if (RegDE['ALUSrc2'] == 0):
        RegDE['ALU_input2'] = RegDE['ReadData2']
    elif (RegDE['ALUSrc2'] == 1):
        RegDE['ALU_input2'] = RegDE['ImmGenOutput']
    elif (RegDE['ALUSrc2'] == 2):
        RegDE['ALU_input2'] = RegDE['ImmGenOutput'] << 12
    if (RegDE['ALUControl'] == 0):
        RegDE['ALUResult'] = RegDE['ALU_input1'] + RegDE['ALU_input2']
    elif (RegDE['ALUControl'] == 1):
        RegDE['ALUResult'] = RegDE['ALU_input1'] & RegDE['ALU_input2']
    elif (RegDE['ALUControl'] == 2):
        RegDE['ALUResult'] = RegDE['ALU_input1'] | RegDE['ALU_input2']
    elif (RegDE['ALUControl'] == 3):
        RegDE['ALUResult'] = RegDE['ALU_input1'] << RegDE['ALU_input2']
    elif (RegDE['ALUControl'] == 4):
        RegDE['ALUResult'] = 1 if RegDE['ALU_input1'] < RegDE['ALU_input2'] else 0
    elif (RegDE['ALUControl'] == 5):
        RegDE['ALUResult'] = RegDE['ALU_input1'] >> RegDE['ALU_input2']
    elif (RegDE['ALUControl'] == 6):
        RegDE['ALUResult'] = RegDE['ALU_input1'] - RegDE['ALU_input2']
    elif (RegDE['ALUControl'] == 7):
        RegDE['ALUResult'] = RegDE['ALU_input1'] ^ RegDE['ALU_input2']
    elif (RegDE['ALUControl'] == 8):
        RegDE['ALUResult'] = RegDE['ALU_input1'] ^ RegDE['ALU_input2']
    elif (RegDE['ALUControl'] == 9):
        RegDE['ALUResult'] = RegDE['ALU_input1'] * RegDE['ALU_input2']
    elif (RegDE['ALUControl'] == 10):
        RegDE['ALUResult'] = RegDE['ALU_input1'] // RegDE['ALU_input2']
    else:
        RegDE['ALUResult'] = RegDE['ALU_input1'] % RegDE['ALU_input2']
    RegDE['Address'] = RegDE['ALUResult']
    RegDE['WriteData'] = RegDE['ReadData2']
    RegDE['LessThan'] = 1 if RegDE['ALU_input1'] < RegDE['ALU_input2'] else 0
    RegDE['GE'] = 1 if RegDE['ALU_input1'] >= RegDE['ALU_input2'] else 0
    RegDE['zero'] = 1 if RegDE['ALU_input1'] == RegDE['ALU_input2'] else 0
    PCSrc = 0
    opcode = InstructionE[25:]
    if (RegDE['Branch'] == 1):
        PCSrc = 1
    elif (RegDE['Branch'] == 2 and RegDE['zero'] == 1):
        PCSrc = 1
    elif (RegDE['Branch'] == 3 and RegDE['zero'] == 0):
        PCSrc = 1
    elif (RegDE['Branch'] == 6 and RegDE['LessThan'] == 1):
        PCSrc = 1
    elif (RegDE['Branch'] == 7 and RegDE['GE'] == 1):
        PCSrc = 1
    elif (opcode == '1101111'):
        PCSrc = 1
    InstCount = InstCount + 1

    if PCSrc==1 and currSTATE=='NT':
        update_state(PC,'T')
    elif PCSrc==0 and currSTATE=='T':
        update_state(PC,'NT')
    
    PipE = RegDE['ALUResult']


def memory_access():
    global RegEM
    #Control Signals
    # global Branch
    # global MemRead
    # global MemtoReg
    # ALUOp
    # global MemWrite
    # global ALUSrc1
    # global ALUSrc2
    global PCSrc
    global PCReg  #Signal if the PC is updated by the Register value

    #Register File inputs and Outputs
    # global RegWrite
    # global ReadData1
    # global ReadData2
    # global ReadRegister1
    # global ReadRegister2
    # global WriteRegister
    # global WriteDataRegFile

    #Immediate Generation
    # global ImmGenOutput

    #ALU Control
    # global ALUControl

    #ALUinputs
    # global ALU_input1
    # global ALU_input2

    #PC
    global PC

    #Instruction Memory
    global ReadAddress
    global InstructionM

    #ALU output
    # global Zero
    # global LessThan
    # global GE
    # global ALUResult

    #Data Memory
    # global Address
    # global WriteData
    # global ReadData

    #Registers
    global reg_file

    #clock
    global clock

    #TempMem
    global TempMem

    #Pipelining Regs
    global PipM
    #Exit
    global EXIT
    if (EXIT):
        return
    if (int(InstructionM) == 0):
        return
    RegEM['Address'] = RegEM['ALUResult']
    RegEM['WriteData'] = BitArray(int=RegEM['ReadData2'], length=32).bin
    if (RegEM['MemRead'] != 0):
        if (RegEM['MemRead'] == 1):
            RegEM['ReadData'] = read_byte(RegEM['Address'])
            RegEM['ReadData'] = '0' * (8 - len(RegEM['ReadData'])) + RegEM['ReadData']
        elif (RegEM['MemRead'] == 2):
            RegEM['ReadData'] = read_hword(RegEM['Address'])
            RegEM['ReadData'] = '0' * (8 - len(RegEM['ReadData'])) + RegEM['ReadData']
        elif (RegEM['MemRead'] == 3):
            RegEM['ReadData'] = read_word(RegEM['Address'])
        else:
            RegEM['ReadData'] = read_dword(RegEM['Address'])
    if (RegEM['MemWrite'] != 0):
        if (RegEM['MemWrite'] == 1):
            RegEM['WriteData'] = "{:02x}".format(int(RegEM['WriteData'][-2:], 2))
            write_byte(RegEM['Address'], RegEM['WriteData'])
        elif (RegEM['MemWrite'] == 2):
            RegEM['WriteData'] = "{:04x}".format(int(RegEM['WriteData'][-4:], 2))
            write_hword(RegEM['Address'], RegEM['WriteData'])
        elif (RegEM['MemWrite'] == 3):
            RegEM['WriteData'] = "{:08x}".format(int(RegEM['WriteData'], 2))
            write_word(RegEM['Address'], RegEM['WriteData'])
        else:
            RegEM['WriteData'] += BitArray(int=reg_file['x' + str((RegEM['ReadRegister2'] + 1) % 32)], length=32).bin
            RegEM['WriteData'] = "{:016x}".format(int(RegEM['WriteData'], 2))
            write_dword(RegEM['Address'], RegEM['WriteData'])

    PipM = RegEM['ReadData']


def writeback():
    global RegMW
    #Control Signals
    # global Branch
    # global MemRead
    # global MemtoReg
    # ALUOp
    # global MemWrite
    # global ALUSrc1
    # global ALUSrc2
    global PCSrc
    global PCReg  #Signal if the PC is updated by the Register value

    #Register File inputs and Outputs
    # global RegWrite
    # global ReadData1
    # global ReadData2
    # global ReadRegister1
    # global ReadRegister2
    # global WriteRegister
    # global WriteDataRegFile

    #Immediate Generation
    # global ImmGenOutput

    #ALU Control
    # global ALUControl

    #ALUinputs
    # global ALU_input1
    # global ALU_input2

    #PC
    global PC

    #Instruction Memory
    global ReadAddress
    global InstructionW

    #ALU output
    # global Zero
    # global LessThan
    # global GE
    # global ALUResult

    #Data Memory
    # global Address
    # global WriteData
    # global ReadData

    #Registers
    global reg_file

    #clock
    global clock

    #TempMem
    global TempMem
    #Exit
    global EXIT
    if (EXIT):
        return
    if (int(InstructionW) == 0):
        return
    if (RegMW['RegWrite'] == 1):
        if (RegMW['MemtoReg'] == 0):
            RegMW['WriteDataRegFile'] = RegMW['ALUResult']
        elif (RegMW['MemtoReg'] == 1):
            RegMW['WriteDataRegFile'] = BitArray(hex=RegMW['ReadData']).int
        else:
            RegMW['WriteDataRegFile'] = RegMW['PC'] + 4
        if (RegMW['MemRead'] != 4):
            reg_file['x' + str(RegMW['WriteRegister'])] = RegMW['WriteDataRegFile']
        else:
            reg_file['x' + str(RegMW['WriteRegister'])] = BitArray(hex=RegMW['ReadData'][8:]).int
            reg_file['x' + str((RegMW['WriteRegister'] + 1) % 32)] = BitArray(hex=RegMW['ReadData'][0:8]).int
    reg_file['x0'] = 0


def check():
    global InstructionF
    global InstructionD
    global InstructionE
    global InstructionM
    global InstructionW
    global EXIT

    if (int(InstructionF) == int(InstructionD) == int(InstructionE) == int(InstructionM) == int(InstructionW) == 0):
        EXIT = True


PCList = []
MemList = []
RegList = []
InstCount = 0  #Counted in Execute step
count = 0


def flush():
    global PC
    global REGTEMP
    global PCList
    global InstructionF
    global InstructionD
    global InstructionE
    global InstructionM
    global InstructionW
    global RegFD
    global RegDE
    global RegEM
    global RegMW
    global FLUSHDONE
    FLUSHDONE = 1
    InstructionF = '0' * 32
    InstructionD = '0' * 32
    for i, j in REGTEMP.items():
        RegFD[i] = j
    PCList.pop()
    PC = RegDE['PC']

    #TODO update PC (DONE)


def main4():

    global clock
    global MemList
    global RegList
    global PCList
    global InstCount
    global RegFD
    global RegDE
    global RegEM
    global RegMW
    global InstructionF
    global InstructionD
    global InstructionE
    global InstructionM
    global InstructionW
    global EXIT
    global FLUSHDONE
    print("main4 called")
    initialize_mem()
    MemList.append(deepcopy(TempMem))
    RegList.append(deepcopy(reg_file))
    EXIT = False
    clock = 0
    while (True):
        #TODO Flush (DONE)
        InstructionW = InstructionM
        RegMW = RegEM
        InstructionM = InstructionE
        RegEM = RegDE
        InstructionE = InstructionD
        RegDE = RegFD
        InstructionD = InstructionF
        writeback()
        memory_access()
        execute()
        decode()
        fetch()  #flush done in this
        # if (RegDE['Branch'] == RegDE['BranchTaken']):
        if (FLUSHDONE == 0):
            PCList.append(PC)
        FLUSHDONE = 0
        MemList.append(deepcopy(TempMem))
        RegList.append(deepcopy(reg_file))

        # print(count)

        check()  #check for exit condition when all instructions are 0

        clock = clock + (0 if EXIT else 1)
        if (EXIT):
            exit_routine()
            break


#TODO
# 1. no increament in PC when fetching the first 2 or 3 instructions (DONE)
# 2. PCSrs and PCReg are being modified from the prediction table
# 3. For data forwarding from E use ALUResult
# 4. Remove PC from the PCList twice on flush (DONE)
# 5. Halt when dependency occurs if prediction == 0
# 6. Use branchTaken and branch for some results
# 7. Stalling is left
