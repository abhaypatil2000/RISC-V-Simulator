from declarations import *
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
    if(PCReg == 1):
        PC = ALUResult
    elif(PCSrc == 0):
        PC = PC + 4
    elif(PCSrc == 1):
        PC = PC + ImmGenOutput << 1
    ReadAddress = PC
    Instruction = "{:032b}".format(int(read_word(ReadAddress),16))
    print("ReadAddress " + str(ReadAddress))
    print("Instruction " + '0x' + read_word(ReadAddress))
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
    zero = 1 if ALUResult == 0 else 0
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
    print('PCSrc '+str(PCSrc))