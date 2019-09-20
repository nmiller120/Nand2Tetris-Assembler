# HACK Assembler

from Parser import *
from Code import *
import sys

def main():
    filename = sys.argv[1]
    
    # init
    i = filename.find(".")
    filename_truncated = filename[0:i]
    filename_HACK = filename_truncated + ".hack"   
    
    symbol_table = {
        "SCREEN": 16384,
        "KBD": 24576,
        "SP": 0,
        "LCL": 1,
        "ARG": 2,
        "THIS": 3,
        "THAT": 4
            }

    for x in range(16):
        registerName = "R" + str(x)
        symbol_table[registerName] = x

    # first pass
    assemblyFile = open(filename, "r")
    
    x = 0
    for line in assemblyFile:
        inst = Parser(line)
        if inst.inst_type == "label":
            symbol_table[inst.label] = x
            
        if inst.inst_type == "A" or inst.inst_type == "C":
            #print(x, line)
            x+=1
    
    # second pass
    assemblyFile = open(filename, "r")
    hackFile = open(filename_HACK, "w")
    encoder = Code()
    n = 16
    for line in assemblyFile:
        encoded_Inst = 0
        inst = Parser(line)
        if inst.inst_type == "C":
            d = inst.dest
            c = inst.comp
            j = inst.jump
            encoded_Inst = encoder.create_Cinst(d,c,j)
                
        if inst.inst_type == "A":
            if inst.label != "":
                address = symbol_table.get(inst.label)
                if address == None:
                    inst.addr = n
                    symbol_table[inst.label] = n
                    n += 1
                else:
                    inst.addr = address
                
            encoded_Inst = encoder.create_Ainst(inst.addr)

        if inst.inst_type == "A" or inst.inst_type == "C":
            leading0s = bin(encoded_Inst + (1<<16))
            leading0s = leading0s[3:]
            hackFile.write(leading0s)
            hackFile.write("\n")

    
    hackFile.close()
    assemblyFile.close()
    
if __name__ == '__main__':
    main()
