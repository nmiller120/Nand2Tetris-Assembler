# Code.py

class Code:
    def __init__(self):
        pass

    def create_Ainst(self, address):
        return address

    def create_Cinst(self, destStr, compStr, jumpStr):
        dest = self.dest(destStr)
        comp = self.comp(compStr)
        jump = self.jump(jumpStr)
        inst = 0b111 << 13
        inst += comp << 6
        inst += dest << 3
        inst += jump
        return inst
    
    def comp(self, expression):
        if expression == "":
            return 0
        
        a = 0
        c = 0
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

        if expression.find("M") != -1:
            a = 1
            expression = expression.replace("M", "A")

        opcode = opcode_lookup[expression] + (a<<6)
        return opcode

    def dest(self, expression):
        if expression == "":
            return 0
        
        opcode_lookup = {
            "M"     :0b001,
            "D"     :0b010,
            "MD"    :0b011,
            "A"     :0b100,
            "AM"    :0b101,
            "AD"    :0b110,
            "AMD"   :0b111,
            }

        return opcode_lookup[expression]

    def jump(self, expression):
        if expression == "":
            return 0
        
        opcode_lookup = {
            "JGT"     :0b001,
            "JEQ"     :0b010,
            "JGE"    :0b011,
            "JLT"     :0b100,
            "JNE"    :0b101,
            "JLE"    :0b110,
            "JMP"   :0b111,
            }
        
        return opcode_lookup[expression]
