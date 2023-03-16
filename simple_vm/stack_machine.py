from enum import Enum


class Command(Enum):
    PUSH = 'PUSH'
    POP = 'POP'
    ADD = 'ADD'
    SUB = 'SUB'
    MUL = 'MUL'
    DIV = 'DIV'
    MOD = 'MOD'
    DUP = 'DUP'
    SWAP = 'SWAP'
    JMP = 'JMP'
    JG = 'JG'
    JL = 'JL'
    JZ = 'JZ'
    JNZ = 'JNZ'
    CMP = 'CMP'
    MOV = 'MOV'
    NOP = 'NOP'
    HALT = 'HALT'
    LABEL = 'LABEL'


class StackMachine:
    """
    PUSH <value>: Push a value onto the stack. e.g., PUSH 10
    POP: Remove and return the top value from the stack.
    ADD: Remove the top two values from the stack, calculate their sum, and push the result onto the stack.
    SUB: Remove the top two values from the stack, calculate their difference, and push the result onto the stack.
    MUL: Remove the top two values from the stack, calculate their product, and push the result onto the stack.
    DIV: Remove the top two values from the stack, calculate their division, and push the result onto the stack.
    MOD: Remove the top two values from the stack, calculate their remainder, and push the result onto the stack.
    DUP: Copy the top value from the stack and push it onto the stack.
    SWAP: Swap the top two values on the stack.
    JMP <label>: Move program execution to the given label. e.g., JMP LOOP
    JG <label>: If the top value on the stack is greater than 0, move program execution to the given label.
    JL <label>: If the top value on the stack is less than 0, move program execution to the given label.
    JZ <label>: If the top value on the stack is 0, move program execution to the given label.
    JNZ <label>: If the top value on the stack is not 0, move program execution to the given label.
    CMP: Compare the top two values on the stack and push the result onto the stack.
    (-1: First value is smaller, 0: Both values are equal, 1: First value is larger)
    MOV <register>: Move the top value from the stack to the specified register (AX, BX, CX, or DX).
    NOP: Perform no operation. This command is ignored in the program.
    HALT: Stop program execution.
    """

    def __init__(self):
        self.stack = []
        self.program = []
        self.labels = {}
        self.registers = {'AX': 0, 'BX': 0, 'CX': 0, 'DX': 0}
        self.command_list = {}
        self.instruction_pointer = 0
        self._init_command_list()

    def _init_command_list(self):
        self.command_list[Command.PUSH] = self.command_push
        self.command_list[Command.POP] = self.command_pop
        self.command_list[Command.ADD] = self.command_add
        self.command_list[Command.SUB] = self.command_sub
        self.command_list[Command.MUL] = self.command_mul
        self.command_list[Command.DIV] = self.command_div
        self.command_list[Command.MOD] = self.command_mod
        self.command_list[Command.DUP] = self.command_dup
        self.command_list[Command.SWAP] = self.command_swap
        self.command_list[Command.JMP] = self.command_jmp
        self.command_list[Command.JG] = self.command_jg
        self.command_list[Command.JL] = self.command_jl
        self.command_list[Command.JZ] = self.command_jz
        self.command_list[Command.JNZ] = self.command_jnz
        self.command_list[Command.CMP] = self.command_cmp
        self.command_list[Command.MOV] = self.command_mov
        self.command_list[Command.NOP] = self.command_nop
        self.command_list[Command.HALT] = self.command_halt
        self.command_list[Command.LABEL] = self.command_label

    def load_program(self, program):
        self.program = program
        self.labels = {line[:-1]: i for i, line in enumerate(program) if line.endswith(':')}

    def parse_command(self, command_string):
        command, *args = command_string.split()
        if command not in Command.__members__:
            if ':' in command:
                return Command['LABEL'], args
            else:
                raise ValueError(f"Unknown command: {command}")
        return Command[command], args

    def execute_command(self, command, args):
        if command in self.command_list:
            self.command_list[command](args)
        else:
            raise ValueError(f"Unknown command: {command}")

        self.instruction_pointer += 1

    def command_push(self, args):
        value = int(args[0]) if 'X' not in args[0] else self.registers[args[0]]
        self.stack.append(value)

    def command_pop(self, args):
        self.stack.pop()

    def command_add(self, args):
        self.stack.append(self.stack.pop() + self.stack.pop())

    def command_sub(self, args):
        b, a = self.stack.pop(), self.stack.pop()
        self.stack.append(a - b)

    def command_mul(self, args):
        self.stack.append(self.stack.pop() * self.stack.pop())

    def command_div(self, args):
        b, a = self.stack.pop(), self.stack.pop()
        self.stack.append(a // b)

    def command_mod(self, args):
        b, a = self.stack.pop(), self.stack.pop()
        self.stack.append(a % b)

    def command_dup(self, args):
        self.stack.append(self.stack[-1])

    def command_swap(self, args):
        self.stack[-1], self.stack[-2] = self.stack[-2], self.stack[-1]

    def command_jmp(self, args):
        self.instruction_pointer = self.labels[args[0]]

    def command_jg(self, args):
        if self.stack.pop() == 1:
            self.instruction_pointer = self.labels[args[0]]

    def command_jl(self, args):
        if self.stack.pop() == -1:
            self.instruction_pointer = self.labels[args[0]]

    def command_jz(self, args):
        if self.stack.pop() == 0:
            self.instruction_pointer = self.labels[args[0]]

    def command_jnz(self, args):
        if self.stack.pop() != 0:
            self.instruction_pointer = self.labels[args[0]]

    def command_cmp(self, args):
        b, a = self.stack.pop(), self.stack.pop()
        self.stack.append((a > b) - (a < b))

    def command_mov(self, args):
        self.registers[args[0]] = self.stack[-1]

    def command_nop(self, args):
        pass

    def command_halt(self, args):
        pass

    def command_label(self, args):
        pass

    def run(self):
        for cycle in range(20000):
            if self.instruction_pointer >= len(self.program):
                print(f"Cycle: {cycle}")
                break
            command_string = self.program[self.instruction_pointer]
            command, args = self.parse_command(command_string)
            self.execute_command(command, args)