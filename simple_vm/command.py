from enum import Enum


class Command(Enum):
    ADD = 'ADD'               # Add the top two values on the stack
    CMP = 'CMP'               # Compare the top two values on the stack
    DEC = 'DEC'               # Decrement the top value on the stack
    CYCLE = 'CYCLE'           # Print cycle
    DIV = 'DIV'               # Divide the top two values on the stack
    DUP = 'DUP'               # Duplicate the top value on the stack
    HALT = 'HALT'             # Halt program execution
    INC = 'INC'               # Increment the top value on the stack
    JMP = 'JMP'               # Unconditionally jump to a label
    JG = 'JG'                 # Jump to a label if the top value on the stack is greater than 0
    JL = 'JL'                 # Jump to a label if the top value on the stack is less than 0
    JNZ = 'JNZ'               # Jump to a label if the top value on the stack is not zero
    JZ = 'JZ'                 # Jump to a label if the top value on the stack is zero
    LABEL = 'LABEL'           # Define a label in the program
    MOD = 'MOD'               # Calculate the remainder of the top two values on the stack
    MOV = 'MOV'               # Move the top value on the stack to a register
    MUL = 'MUL'               # Multiply the top two values on the stack
    NOP = 'NOP'               # Do nothing
    POP = 'POP'               # Remove the top value from the stack
    PRINT = 'PRN'             # Print the top value from the stack
    PUSH = 'PUSH'             # Push a value or register onto the stack
    SQRT = 'SQRT'             # Calculate the square root of the top value on the stack
    STR = 'STR'               # Push a string onto the stack
    SUB = 'SUB'               # Subtract the top two values on the stack
    SWAP = 'SWAP'             # Swap the top two values on the stack
