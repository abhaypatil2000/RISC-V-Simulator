import re
from common_backend import *

label_instructions = ['jal', 'beq', 'bge', 'blt', 'bne']
label_dict = {}

class MyException(Exception):
    pass

def findLabels(line, num):
    label = re.compile("(\A\w+)\:")
    label_matches = label.search(line)
    if label_matches!= None:
        if label_dict.get(label_matches[0].replace(':', '')) == None:
            label_dict[label_matches[0].replace(':', '')] = 4*num
        else:
            raise MyException("Label '" + label_matches[0].replace(':', '') + "' defined twice")


def parse(line, num):
    instruction = re.compile("^(\w)+(\s(\w)+)+")
    instruction_matches = instruction.search(line)
    comment = re.compile("\#\w*")
    comment_matches = comment.search(line)

    if comment_matches != None:
        lines = line.split("#")
        line = lines[0]

    elif instruction_matches != None:
        lines = instruction_matches[0].replace(',', ' ').split(' ')
        if lines[0] in label_instructions:
            try:
                int(lines[-1])
            except:
                try:
                    lines[-1] = int((label_dict[lines[-1]] - 4*num))
                except:
                    raise MyException("Label not recognized on line " + str(num))
            line = ' '.join(str(elem) for elem in lines)

    return line

def preprocessing(line):
    label = re.compile("(\A\w+)\:")
    label_matches = label.search(line)
    if label_matches!= None:
        line=line.replace(label_matches[0],"")
    return line
    
    

def parseDoc(lines):
    
    for i in range(len(lines)):
        findLabels(lines[i], i)
        
    for i in range(len(lines)):
        lines[i] = parse(lines[i], i)
       
    for i in range(len(lines)):
        lines[i]=preprocessing(lines[i])
     

    #print(lines)
    return lines
