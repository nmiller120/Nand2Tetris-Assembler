# Parser.py

class Parser:
    inst_type = "" #A, C, label, or whitespace
    dest = ""
    comp = ""
    jump = ""
    label = ""
    addr = 0

    def __init__(self, inst):
        nlDetect = inst.find("/")
        if nlDetect > 0 and inst[nlDetect+1] == "/":
            inst = inst[0:nlDetect-1]

        striped_inst = inst.strip()
        # identify inst type
        if  inst == "":
            self.inst_type == "whitespace"
        elif (inst[0] == "/") or (inst[0] == "\n"):
            self.inst_type = "whitespace"
        elif striped_inst[0] == "@":
            self.inst_type = "A"
        elif striped_inst[0] == "(":
            self.inst_type = "label"
        else:
            self.inst_type = "C"


        # Atype inst handling
        if self.inst_type == "A":
            if ((ord(striped_inst[1]) < 48) or
            (ord(striped_inst[1]) > 57)):
                self.label = striped_inst[1:]
            elif self.inst_type == "A":
                self.addr = int(striped_inst[1:])

        # ctype inst handling
        if self.inst_type == "C":
            if inst.find("=") != -1:
                self.dest, self.comp = inst.split("=")

            else:
                self.comp = inst

            if self.comp.find(";") != -1:
                self.comp, self.jump = self.comp.split(";")

        # label handling
        if self.inst_type == "label":
            endP = inst.find(")")
            self.label = inst[1:endP]


        self.label = self.label.strip()
        self.dest = self.dest.strip()
        self.comp = self.comp.strip()
        self.jump = self.jump.strip()
            
            
