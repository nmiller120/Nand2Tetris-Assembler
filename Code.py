# Code.py

# used to convert parsed instructions to binary machine instructions

class Code:
    def __init__(self):
        pass

    def create_Ainst(self, address):
        # just created for consistent formatting really. Doesn't do anything,
        # A instruction is literally just an address. It is indicated by the MSB
        # being a 0 instead of a 1
        return address

    def create_Cinst(self, destStr, compStr, jumpStr):
        # returns the code for the c instruciton

        # passes the string values the comp, dest, and jump functions. Returns
        # the corresponding opcodes in binary
        dest = self.dest(destStr)
        comp = self.comp(compStr)
        jump = self.jump(jumpStr)

        # all C instruction begin with 3 bits, these are shifted to the end
        inst = 0b111 << 13

        # then the computation bits are shifted to their designated position
        inst += comp << 6

        # then the destination bits
        inst += dest << 3

        # then the jump bits
        inst += jump

        # and the instruction code is returned
        return inst

    def comp(self, expression):
        # returns the 7 bit binary code related to the instruction

        # if we were given no value for comp return 0
        if expression == "":
            return 0

        # bit used to indicate if M is used in the instruction or if A is to be
        # used in the instruction
        a = 0

        # A comp statement can only have 36 possible values, the ones below
        # or the ones below sub M for A since there are only 3 data registers
        # and 4 possible operators (+,-,&, and |)
        opcode_lookup = {
            "0"     :0b101010,
            "1"     :0b111111,
            "-1"    :0b111010,
            "D"     :0b001100,
            "A"     :0b110000,
            "!D"    :0b001101,
            "!A"    :0b110001,
            "-D"    :0b001111,
            "-A"    :0b110011,
            "D+1"   :0b011111,
            "A+1"   :0b110111,
            "D-1"   :0b001110,
            "A-1"   :0b110010,
            "D+A"   :0b000010,
            "D-A"   :0b010011,
            "A-D"   :0b000111,
            "D&A"   :0b000000,
            "D|A"   :0b010101
            }

        # if the value of M is not seen in the instruction the a bit is set high
        # indicating that A is subbed for M when it reaches the CPU. To use our
        # lookup table we also  replace A for M in the expression.
        if expression.find("M") != -1:
            a = 1
            expression = expression.replace("M", "A")

        # we then return the opcode_lookup value with the value of the a bit tacked
        # at the end of the instruction
        opcode = opcode_lookup[expression] + (a<<6)
        return opcode

    def dest(self, expression):
        # returns the destination register of the computation

        # if no destionation was provided return 0
        if expression == "":
            return 0

        # the only possible destinations
        opcode_lookup = {
            "M"     :0b001,
            "D"     :0b010,
            "MD"    :0b011,
            "A"     :0b100,
            "AM"    :0b101,
            "AD"    :0b110,
            "AMD"   :0b111,
            }

        # take the assembly language command and correspond it to a value in binary
        # return the value
        return opcode_lookup[expression]

    def jump(self, expression):
        # returns the binary code of the jump statement

        # if no jump statement was given return 0
        if expression == "":
            return 0

        # binary codes for each jump statement
        opcode_lookup = {
            "JGT"     :0b001,
            "JEQ"     :0b010,
            "JGE"    :0b011,
            "JLT"     :0b100,
            "JNE"    :0b101,
            "JLE"    :0b110,
            "JMP"   :0b111,
            }

        # return the binary value corresponding the the given jump statement
        return opcode_lookup[expression]
