from declarations import *
from bitstring import BitArray
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
        print('opcode '+opcode)
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
        print('PCReg '+str(PCReg))
        print('Immediate Gen Ouput ' + str(ImmGenOutput))
        print('Write Reg '+str(WriteRegister))