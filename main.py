# Project Dscription:
# This is an implementation of a program that translates Hack assembly language
# code into machine code that can be run on the Hack CPU, this was completed as
# part of the 2nd semester of the nand2tetris course.

from Parser import * # module parses hack assembly code
from Code import * # module used to encode the assembly instruction in binary
import sys # library used take system arguments when calling program from the
# command line

def main():
    filename = sys.argv[1] # filename of .asm file to be translated

    # create a new string to be used to name the output file
    i = filename.find(".")
    filename_truncated = filename[0:i]
    filename_HACK = filename_truncated + ".hack"

    # symbol_table is a dictionary used to keep record of symbols used in hack
    # code. The symbol_table initializes with the 8 predefined symbols shown
    # below, as well as the 16 registers initialized in the for loop.
    symbol_table = {
        "SCREEN": 16384,
        "KBD": 24576,
        "SP": 0,
        "LCL": 1,
        "ARG": 2,
        "THIS": 3,
        "THAT": 4
            }

    # add registers to the symbol table
    for x in range(16):
        registerName = "R" + str(x)
        symbol_table[registerName] = x


    # first pass:
    # The first pass reading through the assembly code is used to mark the values
    # of labels encountered in the code. Labels are used as markers in the set of
    # instructions that can be returned to using jump statements. All labels and
    # their program counter values are recorded into the symbol table.

    # open the assembly file
    assemblyFile = open(filename, "r")


    # the variable x represents the value of the program counter for the given
    # instruction.
    x = 0

    # for each line in the assembly file
    for line in assemblyFile:

        # the string representing each line is passed to a parser object
        inst = Parser(line)

        # if the instruction is a label type, the label is added to the
        # symbol_table as a key and the current program counter value is added
        # as the dictionary's value
        if inst.inst_type == "label":
            symbol_table[inst.label] = x

        # if the instruction is not an A or C type instruction, the variable x
        # is incremented.
        if inst.inst_type == "A" or inst.inst_type == "C":
            x+=1




    # second pass:
    # The second pass is where we actually start translating assembly code.

    # reopen the input file, and open the output file
    assemblyFile = open(filename, "r")
    hackFile = open(filename_HACK, "w")

    # initialize a Code() object
    encoder = Code()


    # n represents the next usable value in RAM after the 16 registers. It is
    # used when an A instruction is used that doesn't refer to a label or
    # predefined symbol. The programmer could write an A instruction such as
    # @my_value to store a value to an arbitrary place refered to in ram,
    # then call @my_value again later and recall the value previously stored in
    # memory.
    n = 16


    for line in assemblyFile:

        # this represents the instruction code to be written to the machine
        # language file
        encoded_Inst = 0

        # the string representing each line is passed to a parser object
        inst = Parser(line)

        # if the instruction type is a C instruction
        if inst.inst_type == "C":

            # get the destination, computation, and jump values and pass them
            # to the encoder to get a value for encoded_Inst
            d = inst.dest
            c = inst.comp
            j = inst.jump
            encoded_Inst = encoder.create_Cinst(d,c,j)

        # if the instruction type is an A instruction
        if inst.inst_type == "A":

            # if the A instruction refers to a label instead of a literal
            if inst.label != "":

                # get the value of the label from the symbol_table
                address = symbol_table.get(inst.label)

                # if the value is not in the symbol table, add the label as the
                # key and the current value of n to the symbol_table
                if address == None:
                    inst.addr = n
                    symbol_table[inst.label] = n
                    n += 1

                # if the value is in the symbol table, write the address to the
                # parser
                else:
                    inst.addr = address

            # use the Code object to create a binary A instruction
            encoded_Inst = encoder.create_Ainst(inst.addr)


        # if the instruction type is A or C write the instruction out to the
        # hack file. The tools to test your code on the course webpage were expecting
        # ascii '1's and '0's not binary data. So the integer valued instruction
        # need turned into a string of 1s and 0s
        if inst.inst_type == "A" or inst.inst_type == "C":

            # take the value and add the binary value 1 0000 0000 0000 0000
            # before calling bin() to turn the value into a string
            leading0s = bin(encoded_Inst + (1<<16))

            # concatinate "0b1" from the front of the instruction
            leading0s = leading0s[3:]

            # write the string to a file with a newline character
            hackFile.write(leading0s)
            hackFile.write("\n")


    # close the files
    hackFile.close()
    assemblyFile.close()

if __name__ == '__main__':
    main()
