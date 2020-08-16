from declarations import *
from bitstring import BitArray
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
            WriteData = ALUResult
        elif(MemtoReg == 1):
            WriteData = BitArray(hex = ReadData).int
        else:
            WriteData = PC + 4
        if(MemRead != 4):
            reg_file['x' + str(WriteRegister)] = WriteData
        else:
            reg_file['x' + str(WriteRegister)] = BitArray(hex = ReadData[8:]).int
            reg_file['x' + str((WriteRegister + 1) % 32)] = BitArray(hex = ReadData[0:8]).int
    reg_file['x0'] = 0
    print(reg_file)