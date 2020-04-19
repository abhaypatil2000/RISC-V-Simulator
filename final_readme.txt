TEAM NAME: APOCALYPTIC REDEMPTION

MEMBERS:

	1. Abhaysinh Sunil Patil       :	2018CSB1063
	2. Gurpreet Singh              :	2018CSB1092
	3. Kanniganti Nagasrikar       :	2018CSB1098
	4. Sarvesh Shirirsh Vhaval     :	2018CSB1121
	5. Navneet Kumar               :	2018CSB1237
	

A RISC V simulator which supports the following instruction:

	R format - add, and, or, sll, slt, sra, srl, sub, xor, mul, div, rem
	I format - addi, andi, ori, lb, ld, lh, lw, jalr
	S format - sb, sw, sd, sh
	SB format - beq, bne, bge, blt
	U format - auipc, lui
	UJ format - jal

HOW TO RUN:
Preferrably INSTALL SPYDER latest version for easy execution

Libraries required before running the python code
bitstring
PyQt5 version 5.9.2
PyQt5.sip any version

1. Put the code to be tested in input.txt file.
2. Run the Program try4(1).py. You might need to run the program twice.
3. A new window "RISC-V Simulator" will open.
4. Click file and then open (Ctlr + O) input.txt. Now the .mc file has been generated.
5. If you want to edit the code, do that in editor and click file and generate mc file(Ctrl + G). (The new window will close).
6. The edited code has been saved in input.txt and respective .mc files have been generated  (the new window will close). Open the window again by running the program try4(1).py. Click files and then open file and select input.txt to load the input file.
7. Click the simulator tab.
8. You can Run it or Step through it.


BUGS TO BE FIXED:
1. When clicking the previous button in simulator, the highlighter goes to the next line once even when it is actually going back.
2. Editor is not for editing your code. It is to view the code written.




GUIDLINES ON OPERATION (PRECAUTIONS):


1. The call for assembler directives must be in lowercase. Uppercase will give an error.
eg. .Byte or .BYTE will give an error.

2. A signed value should be given. For unsigned values error will be thrown.
eg. for .byte (8bits) value from -128 to 127 (both incusive) will be supported. Same for .half, .word and .dword

3. .asciiz will take strings starting and terminating with " or '. Multiple strings can be given by separating them with <space> or <comma>
eg. .asciiz "hello" 'helo' and .asciiz 'hello',"helo" both will work

4. Assembler directives support only decimal numbers.

5. After a label is inserted put a '\n' character DON'T WRITE ANYTHING AFTER THAT IN THE SAME LINE

6. Editor is not for editing your code. It is to view the code written.

7. There should be no space between a label and the following ':'.
eg. label: is correct method and label : is wrong

8. After declaring a label add another line add x0 x0 x0

9. If the code doesnt run try running the program again



INDIVIDUAL CONTRIBUTION
Abhay : UJ_Format, U_Format, Assembler Directives, Main.py, README
Gurpreet : S_Format, Main.py, errors in SB_Format
Nagasrikar : I_Format, Parser.py, main.py
Sarvesh : Graphic User Interface, SB_Format, 1.mc, Main.py
Navneet : R_Format, phase2, main3.py