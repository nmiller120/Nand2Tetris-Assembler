# Parser.py

# used to parse the .asm file instructions.

class Parser:
    inst_type = "" #A, C, label, or whitespace
    dest = "" # string representing where a value is stored
    comp = "" # computation to be performed
    jump = "" # jump statement
    label = "" # label used in instruction for A and label statements
    addr = 0 # value of address used in A type instruction

    def __init__(self, inst):

        # truncate comments on end of the instruction (eg. M=D+5 // comment)
        nlDetect = inst.find("/")
        if nlDetect > 0 and inst[nlDetect+1] == "/":
            inst = inst[0:nlDetect-1]

        # remove extra whitespace and newline characters
        striped_inst = inst.strip()

        # if there is nothing left define the type as "whitespace"
        if  inst == "":
            self.inst_type == "whitespace"


        # double check for comments and newline characters, they are "whitespace"
        elif (inst[0] == "/") or (inst[0] == "\n"):
            self.inst_type = "whitespace"


        # if the instruction begins with '@', the instruction is an A type
        # instruction
        elif striped_inst[0] == "@":
            self.inst_type = "A"

        # if the instruction begins with an "(" than it is a label
        elif striped_inst[0] == "(":
            self.inst_type = "label"


        # if it doesn't begin with any of the above it is a c type instruction
        else:
            self.inst_type = "C"


        # Atype inst handling
        if self.inst_type == "A":

            # if the next character in the instruction is not a number, store
            # that string value as self.label
            if ((ord(striped_inst[1]) < 48) or
            (ord(striped_inst[1]) > 57)):
                self.label = striped_inst[1:]


            # If the next character is a number store that number in self.addr as
            # as an integer
            else:
                self.addr = int(striped_inst[1:])

        # ctype inst handling
        if self.inst_type == "C":

            # if an equals sign exist in the instruction, assign the value to the
            # left as the destination, and assign the value to the right as the
            # computation
            if inst.find("=") != -1:
                self.dest, self.comp = inst.split("=")

            # if there is no equals sign, the entire instruction is assigned as
            # a computation
            else:
                self.comp = inst

            # if a semicolon is found in the value assigned to self.comp, the
            # value to the left of the instruction is assigned to self.comp and
            # the value of to the right is stored as the jump statement
            if self.comp.find(";") != -1:
                self.comp, self.jump = self.comp.split(";")

        # label handling

        # if the instruciton is a label find the terminating paranthesis and store
        # the string between the two as the label
        if self.inst_type == "label":
            endP = inst.find(")")
            self.label = inst[1:endP]


        # clean up whitespace
        self.label = self.label.strip()
        self.dest = self.dest.strip()
        self.comp = self.comp.strip()
        self.jump = self.jump.strip()


