# Nand2Tetris-Assembler

This program translates assembly code to machine instructions for the Hack computer architecture. This project was completed as part of the Nand2Tetris course. This is a free online project based course where the student starts with a fundamental element, the Nand gate, and uses the Nand gate to build a computer architecture. Once the computer itself is built the student then goes on to design an assembler, VM translator, compiler, and operating system for the machine. This project is completed in Chapter 7 of the course. To better understand the source code for this project, some explaination of the hack computer and the assembly language used to program it is provided below.  

## Computer Architecture

The Hack CPU is a 16 bit CPU which contains only 3 data registers named D, A, and PC. The D register is the data register and acts as the CPU's general purpose register. It is used to store the results of calculations or to act as a container for data. The A register is the address register and can be used just as the D register with the one caveat being that the value of the A register changes the currently selected memory address, so for example if A = 100 then the only memory address that can be accessed is the contents of RAM[100]. The last register is the PC register. This register is the program counter and represents the currently selected element in the computer's program memory. 

## Assembly Language 

The Hack assembly language features 2 types of instructions, A-instructions and C-instructions. A-instructions take the form `@value`, where value can refer to an integer literal or a label. The A-insruction writes specifically to the A register in the CPU. A C-instruction is a computation instruction. The C-instruction is of the form `dest = comp; jump`, where dest represents the destination register(s), comp represents the computation to be performed, and jump represents a conditional jump statement. The C-instruction can include a dest and a comp, a comp and a jump, or all three. 

Another feature of the language is the label, this takes the form `(myLabel)`. Where myLabel is a string of characters. These are markers to the assembler that we want to return to this instruction at some point in time. A jump can be performed using a label by following an A-instruction refering to a label with a jump statement. So for example the following code would perform a jump to the label `myLabel`.

`@myLabel // write the value of myLabel to register A`

`0; JMP // write contents of register A to PC and jump to label`

Lastly, RAM can be accessed via the M register. This register is the data stored in the RAM location pointed to by the A register. 

`RAM[A] = M`

This covers most of the basics needed to understand the source code written for the Hack Assembler, for more info regarding the the Hack CPU and Assembly Language refer to the course hompage: https://www.nand2tetris.org/

Thanks for reading!

