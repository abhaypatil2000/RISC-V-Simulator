from bitstring import BitArray
from copy import deepcopy
#Control Signals
Branch = 0
MemRead = 0
MemtoReg = 0
# ALUOp = 0
MemWrite = 0
ALUSrc1 = 0
ALUSrc2 = 0
PCSrc = -1
PCReg = 0 #Signal if the PC is updated by the Register value

#Register File inputs and Outputs
RegWrite = 0
ReadData1 = 0
ReadData2 = 0
ReadRegister1 = 0
ReadRegister2 = 0
WriteRegister = 0
WriteDataRegFile = 0

#Immediate Generation
ImmGenOutput = 0

#ALU Control
ALUControl = 0

#ALUinputs
ALU_input1 = 0
ALU_input2 = 0

#PC
PC = 0

#Instruction Memory
ReadAddress = 0
Instruction = '0' * 32

#ALU output
Zero = 0
LessThan = 0
GE = 0
ALUResult = 0

#Data Memory
Address = 0
WriteData = 0
ReadData = 0

#Exit Signal
EXIT = False
#Registers
reg_file = {
		'x0' : 0, 'x1' : 0, 'x2' : 0x7ffffffc, 'x3' : 0,
		'x4' : 0, 'x5' : 0, 'x6' : 0, 'x7' : 0,
		'x8' : 0, 'x9' : 0, 'x10' : 0, 'x11' : 0,
		'x12' : 0, 'x13' : 0, 'x14' : 0, 'x15' : 0,
		'x16' : 0, 'x17' : 0, 'x18' : 0, 'x19' : 0,
		'x20' : 0, 'x21' : 0, 'x22' : 0, 'x23' : 0,
		'x24' : 0, 'x25' : 0, 'x26' : 0, 'x27' : 0,
		'x28' : 0, 'x29' : 0, 'x30' : 0, 'x31' : 0,
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
        if(len(inst) != 2):
            break
        a = int(inst[0], 16)
        b = inst[1][2:]
        if(len(b)==8):
            TempMem[a] = b[6:]
            TempMem[a+1] = b[4:6]
            TempMem[a+2] = b[2:4]
            TempMem[a+3] = b[0:2]
        elif(len(b)==4):
            TempMem[a] = b[2:]
            TempMem[a+1] = b[0:2]
        else:
            TempMem[a] = b
    fp.close()
def exit_routine():
    global TempMem
    global clock
    fp = open("1.mc", "r+")
    for i in TempMem.keys():
        fp.write(hex(i) + " " + '0x'+TempMem[i]+'\n')
    fp.close()
def reset():
    initialize_mem()
    global reg_file
    reg_file = {
		'x0' : 0, 'x1' : 0, 'x2' : 0x7ffffffc, 'x3' : 0,
		'x4' : 0, 'x5' : 0, 'x6' : 0, 'x7' : 0,
		'x8' : 0, 'x9' : 0, 'x10' : 0, 'x11' : 0,
		'x12' : 0, 'x13' : 0, 'x14' : 0, 'x15' : 0,
		'x16' : 0, 'x17' : 0, 'x18' : 0, 'x19' : 0,
		'x20' : 0, 'x21' : 0, 'x22' : 0, 'x23' : 0,
		'x24' : 0, 'x25' : 0, 'x26' : 0, 'x27' : 0,
		'x28' : 0, 'x29' : 0, 'x30' : 0, 'x31' : 0,
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
    return read_byte(address+3)+read_byte(address+2)+read_byte(address+1)+read_byte(address)
def read_hword(address):
    return read_byte(address+1)+read_byte(address)
def write_byte(address, data):
    global TempMem
    TempMem[address] = data
def write_word(address, data):
    write_byte(address,data[6:])
    write_byte(address+1,data[4:6])
    write_byte(address+2,data[2:4])
    write_byte(address+3,data[0:2])
def write_hword(address,data):
    write_byte(address,data[2:])
    write_byte(address+1,data[0:2])
def read_dword(address):
    return read_word(address+4) + read_word(address)
def write_dword(address, data):
    write_word(address, data[8:])
    write_word(address + 8, data[0:8])
def fetch():
        #Control Signals
    global Branch 
    global MemRead 
    global MemtoReg 
    # ALUOp 
    global MemWrite 
    global ALUSrc1 
    global ALUSrc2 
    global PCSrc 
    global PCReg  #Signal if the PC is updated by the Register value

    #Register File inputs and Outputs
    global RegWrite 
    global ReadData1 
    global ReadData2 
    global ReadRegister1 
    global ReadRegister2 
    global WriteRegister 
    global WriteDataRegFile 

    #Immediate Generation
    global ImmGenOutput 

    #ALU Control
    global ALUControl 

    #ALUinputs
    global ALU_input1 
    global ALU_input2 

    #PC
    global PC 

    #Instruction Memory
    global ReadAddress 
    global Instruction

    #ALU output
    global Zero 
    global LessThan 
    global GE 
    global ALUResult 

    #Data Memory
    global Address 
    global WriteData 
    global ReadData 

    #Registers
    global reg_file 

    #clock
    global clock 

    #TempMem
    global TempMem
    #Exit
    global EXIT
    if(PCReg == 1):
        PC = ALUResult
    elif(PCSrc == 0):
        PC = PC + 4
    elif(PCSrc == 1):
        PC = PC + (ImmGenOutput << 1)
    ReadAddress = PC
    Instruction = "{:032b}".format(int(read_word(ReadAddress),16))
def decode():
        #Control Signals
    global Branch 
    global MemRead 
    global MemtoReg 
    # ALUOp 
    global MemWrite 
    global ALUSrc1 
    global ALUSrc2 
    global PCSrc 
    global PCReg  #Signal if the PC is updated by the Register value

    #Register File inputs and Outputs
    global RegWrite 
    global ReadData1 
    global ReadData2 
    global ReadRegister1 
    global ReadRegister2 
    global WriteRegister 
    global WriteDataRegFile 

    #Immediate Generation
    global ImmGenOutput 

    #ALU Control
    global ALUControl 

    #ALUinputs
    global ALU_input1 
    global ALU_input2 

    #PC
    global PC 

    #Instruction Memory
    global ReadAddress 
    global Instruction

    #ALU output
    global Zero 
    global LessThan 
    global GE 
    global ALUResult 

    #Data Memory
    global Address 
    global WriteData 
    global ReadData 

    #Registers
    global reg_file 

    #clock
    global clock 

    #TempMem
    global TempMem
    #Exit
    global EXIT
    if(int(Instruction, 2) == 0):
        EXIT = True
        exit_routine()
    else:
        opcode = Instruction[25:]
        func3 = Instruction[17:20]
        func7 = Instruction[0:7]
        ReadRegister1 = int(Instruction[12:17], 2)
        ReadRegister2 = int(Instruction[7:12], 2)
        WriteRegister = int(Instruction[20:25], 2)
        MemtoReg = 0
        MemRead = 0
        MemWrite = 0
        if(opcode == '0000011' or opcode == '0010011' or opcode == '1100111'):
            ImmGenOutput = BitArray(bin = Instruction[0:12]).int
            ALUSrc2 = 1
            if(opcode == '0000011'):
                MemRead = int(func3, 2) + 1
            if(opcode == '0000011'):
                MemtoReg = 1
            elif(opcode == '1100111'):
                MemtoReg = 2
            ALUSrc1 = 0
        elif(opcode == '0100011'):
            ImmGenOutput = BitArray(bin = Instruction[0:7]+Instruction[20:25]).int
            MemWrite = int(func3, 2) + 1
            ALUSrc2 = 1
            ALUSrc1 = 0
        elif(opcode == '1100011'):
            ImmGenOutput = BitArray(bin = Instruction[0] + Instruction[24] + Instruction[1:7] + Instruction[20:24]).int
            ALUSrc2 = 0
            ALUSrc1 = 0
        elif(opcode == '0010111' or opcode == '0110111'):
            ImmGenOutput = BitArray(bin = Instruction[0:20]).int
            ALUSrc2 = 2
            ALUSrc1 = 1 if opcode == '0010111' else 2
        elif(opcode == '1101111'):
            ImmGenOutput = BitArray(bin = Instruction[0]+Instruction[12:20]+Instruction[11]+Instruction[1:11]).int
            ALUSrc2 = 0
            ALUSrc1 = 0
            MemtoReg = 2
            Branch = 1
        else:
            ALUSrc2 = 0
            ALUSrc1 = 0
        if(opcode == '1100011'):
            Branch = int(func3,2) + 2
        else:
            Branch = 0
        PCReg = 1 if opcode == '1100111' else 0
        RegWrite = 0 if opcode == '0100011' or  opcode == '1100011' else 1
        if(opcode == '0110011'):
            if(func3 == '111'):
                ALUControl = 1
            elif(func3 == '110'):
                ALUControl = 2
            elif(func3 == '001'):
                ALUControl = 3
            elif(func3 == '010'):
                ALUControl = 4
            elif(func3 == '101' and func7 == '0100000'):
                ALUControl = 5
            elif(func3 == '101'):
                ALUControl = 6
            elif(func7 == '0100000' and func3 =='000'):
                ALUControl = 7
            elif(func3 == '100'):
                ALUControl = 8
            elif(func7 == '0000001' and func3 == '000'):
                ALUControl = 9
            elif(func7 == '0000001' and func3 == '100'):
                ALUControl = 10
            elif(func7 == '0000001' and func3 == '110'):
                ALUControl = 11
            else:
                ALUControl = 0
        elif(opcode == '1100111'):
            if(func3 == '111'):
                ALUControl = 1
            elif(func3 =='110'):
                ALUControl = 2
            elif(func3 == '001'):
                ALUControl = 3
            else:
                ALUControl = 0
        else:
            ALUControl = 0
        if(opcode == '1100011' and (func3 == '000' or func3 == '001')):
            ALUControl = 7
        ReadData1 = reg_file['x' + str(ReadRegister1)]
        ReadData2 = reg_file['x'+str(ReadRegister2)]
def execute():
        #Control Signals
    global Branch 
    global MemRead 
    global MemtoReg 
    # ALUOp 
    global MemWrite 
    global ALUSrc1 
    global ALUSrc2 
    global PCSrc 
    global PCReg  #Signal if the PC is updated by the Register value

    #Register File inputs and Outputs
    global RegWrite 
    global ReadData1 
    global ReadData2 
    global ReadRegister1 
    global ReadRegister2 
    global WriteRegister 
    global WriteDataRegFile 

    #Immediate Generation
    global ImmGenOutput 

    #ALU Control
    global ALUControl 

    #ALUinputs
    global ALU_input1 
    global ALU_input2 

    #PC
    global PC 

    #Instruction Memory
    global ReadAddress 
    global Instruction

    #ALU output
    global Zero 
    global LessThan 
    global GE 
    global ALUResult 

    #Data Memory
    global Address 
    global WriteData 
    global ReadData 

    #Registers
    global reg_file 

    #clock
    global clock 

    #TempMem
    global TempMem
    #Exit
    global EXIT
    if(EXIT):
        return
    if(ALUSrc1 == 0):
        ALU_input1 = ReadData1
    elif(ALUSrc1 == 1):
        ALU_input1 = 0
    else:
        ALU_input1 = PC
    if(ALUSrc2 == 0):
        ALU_input2 = ReadData2
    elif(ALUSrc2 == 1):
        ALU_input2 = ImmGenOutput
    elif(ALUSrc2 == 2):
        ALU_input2 = ImmGenOutput << 12
    if(ALUControl == 0):
        ALUResult = ALU_input1 + ALU_input2
    elif(ALUControl == 1):
        ALUResult = ALU_input1 & ALU_input2
    elif(ALUControl == 2):
        ALUResult = ALU_input1 | ALU_input2
    elif(ALUControl == 3):
        ALUResult = ALU_input1 << ALU_input2
    elif(ALUControl == 4):
        ALUResult = 1 if ALU_input1 < ALU_input2 else 0
    elif(ALUControl == 5):
        ALUResult = ALU_input1 >> ALU_input2
    elif(ALUControl == 6):
        ALUResult = ALU_input1 - ALU_input2
    elif(ALUControl == 7):
        ALUResult = ALU_input1 ^ ALU_input2
    elif(ALUControl == 8):
        ALUResult = ALU_input1 ^ ALU_input2
    elif(ALUControl == 9):
        ALUResult = ALU_input1 * ALU_input2
    elif(ALUControl == 10):
        ALUResult = ALU_input1 // ALU_input2
    else:
        ALUResult = ALU_input1 % ALU_input2
    Address = ALUResult
    WriteData = ReadData2
    LessThan = 1 if ALU_input1 < ALU_input2 else 0
    GE = 1 if ALU_input1 >= ALU_input2 else 0
    zero = 1 if ALU_input1 == ALU_input2 else 0
    PCSrc = 0
    opcode = Instruction[25:]
    if(Branch == 1):
        PCSrc = 1
    elif(Branch == 2 and zero == 1):
        PCSrc = 1
    elif(Branch == 3 and zero == 0):
        PCSrc = 1
    elif(Branch == 6 and LessThan == 1):
        PCSrc = 1
    elif(Branch == 7 and GE == 1):
        PCSrc = 1
    elif(opcode == '1101111'):
        PCSrc = 1
def memory_access():
        #Control Signals
    global Branch 
    global MemRead 
    global MemtoReg 
    # ALUOp 
    global MemWrite 
    global ALUSrc1 
    global ALUSrc2 
    global PCSrc 
    global PCReg  #Signal if the PC is updated by the Register value

    #Register File inputs and Outputs
    global RegWrite 
    global ReadData1 
    global ReadData2 
    global ReadRegister1 
    global ReadRegister2 
    global WriteRegister 
    global WriteDataRegFile 

    #Immediate Generation
    global ImmGenOutput 

    #ALU Control
    global ALUControl 

    #ALUinputs
    global ALU_input1 
    global ALU_input2 

    #PC
    global PC 

    #Instruction Memory
    global ReadAddress 
    global Instruction

    #ALU output
    global Zero 
    global LessThan 
    global GE 
    global ALUResult 

    #Data Memory
    global Address 
    global WriteData 
    global ReadData 

    #Registers
    global reg_file 

    #clock
    global clock 

    #TempMem
    global TempMem
    #Exit
    global EXIT
    if(EXIT):
        return
    Address = ALUResult
    WriteData = BitArray(int = ReadData2, length = 32).bin
    if(MemRead != 0):
        if(MemRead == 1):
            ReadData = read_byte(Address)
            ReadData = '0' * (8 - len(ReadData)) + ReadData
        elif(MemRead == 2):
            ReadData = read_hword(Address)
            ReadData = '0' * (8 - len(ReadData)) + ReadData
        elif(MemRead == 3):
            ReadData = read_word(Address)
        else:
            ReadData = read_dword(Address)
    if(MemWrite != 0):
        if(MemWrite == 1):
            WriteData = "{:02x}".format(int(WriteData[-2:], 2))
            write_byte(Address, WriteData)
        elif(MemWrite == 2):
            WriteData = "{:04x}".format(int(WriteData[-4:], 2))
            write_hword(Address, WriteData)
        elif(MemWrite == 3):
            WriteData = "{:08x}".format(int(WriteData, 2))
            write_word(Address, WriteData)
        else:
            WriteData += BitArray(int = reg_file['x' + str((ReadRegister2 + 1) % 32)], length = 32).bin
            WriteData = "{:016x}".format(int(WriteData, 2))
            write_dword(Address, WriteData)
def writeback():
        #Control Signals
    global Branch 
    global MemRead 
    global MemtoReg 
    # ALUOp 
    global MemWrite 
    global ALUSrc1 
    global ALUSrc2 
    global PCSrc 
    global PCReg  #Signal if the PC is updated by the Register value

    #Register File inputs and Outputs
    global RegWrite 
    global ReadData1 
    global ReadData2 
    global ReadRegister1 
    global ReadRegister2 
    global WriteRegister 
    global WriteDataRegFile 

    #Immediate Generation
    global ImmGenOutput 

    #ALU Control
    global ALUControl 

    #ALUinputs
    global ALU_input1 
    global ALU_input2 

    #PC
    global PC 

    #Instruction Memory
    global ReadAddress 
    global Instruction

    #ALU output
    global Zero 
    global LessThan 
    global GE 
    global ALUResult 

    #Data Memory
    global Address 
    global WriteData 
    global ReadData 

    #Registers
    global reg_file 

    #clock
    global clock 

    #TempMem
    global TempMem
    #Exit
    global EXIT
    if(EXIT):
        return
    if(RegWrite == 1):
        if(MemtoReg == 0):
            WriteDataRegFile = ALUResult
        elif(MemtoReg == 1):
            WriteDataRegFile = BitArray(hex = ReadData).int
        else:
            WriteDataRegFile = PC + 4
        if(MemRead != 4):
            reg_file['x' + str(WriteRegister)] = WriteDataRegFile
        else:
            reg_file['x' + str(WriteRegister)] = BitArray(hex = ReadData[8:]).int
            reg_file['x' + str((WriteRegister + 1) % 32)] = BitArray(hex = ReadData[0:8]).int
    reg_file['x0'] = 0
PCList = []
MemList = []
RegList = []
InstCount=0
count = 0
def main3():
    
    global clock
    global MemList
    global RegList
    global PCList
    global InstCount
    global EXIT
    print("main3 called")
    initialize_mem()
    MemList.append(deepcopy(TempMem))
    RegList.append(deepcopy(reg_file))
    EXIT = False
    while(True):
        fetch()
        PCList.append(PC)
        decode()
        execute()
        memory_access()
        writeback()
        MemList.append(deepcopy(TempMem))
        RegList.append(deepcopy(reg_file))
        #print(count)
        InstCount = InstCount + (0 if EXIT else 1)
        if(EXIT):
            break
        
#main3()