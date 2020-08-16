from declarations import *
from bitstring import BitArray
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