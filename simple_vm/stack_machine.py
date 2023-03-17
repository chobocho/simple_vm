import math

from command import Command


class StackMachine:
    """
    The StackMachine class implements a simple stack-based virtual machine.

    Available commands:
    ADD: Remove the top two values from the stack, calculate their sum, and push the result onto the stack.
    CMP: Compare the top two values on the stack and push the result onto the stack (-1, 0, or 1).
    DEC: Decrement the top value on the stack by 1 and push the result onto the stack.
    DIV: Remove the top two values from the stack, calculate their integer division, and push the result onto the stack.
    DUP: Duplicate the top value on the stack.
    HALT: Stop program execution.
    INC: Increment the top value on the stack by 1 and push the result onto the stack.
    JMP <label>: Unconditionally jump to the specified label in the program.
    JG <label>: Jump to the specified label if the top value on the stack is greater than 0.
    JL <label>: Jump to the specified label if the top value on the stack is less than 0.
    JNZ <label>: Jump to the specified label if the top value on the stack is not 0.
    JZ <label>: Jump to the specified label if the top value on the stack is 0.
    LABEL: Define a label in the program for use with jump commands.
    MOD: Remove the top two values from the stack, calculate their remainder, and push the result onto the stack.
    MOV <register>: Move the top value from the stack to the specified register (AX, BX, CX, or DX).
    MUL: Remove the top two values from the stack, calculate their product, and push the result onto the stack.
    NOP: Perform no operation. This command is ignored in the program.
    POP: Remove and discard the top value from the stack.
    PRINT <separator>: Print the top value of the stack, optionally followed by a separator character.
    PUSH <value>: Push a value or the content of a register onto the stack. e.g., PUSH 10 or PUSH AX
    SQRT: Remove the top value from the stack, calculate its square root, and push the result onto the stack.
    STR <value>: Push a string onto the stack.
    SUB: Remove the top two values from the stack, calculate their difference, and push the result onto the stack.
    SWAP: Swap the top two values on the stack.

    The StackMachine class provides methods for loading a program, parsing commands,
    executing commands, and running the program. It also maintains a stack, a set of registers,
    and a list of labels defined in the program.
    """

    def __init__(self):
        self.stack = []
        self.program = []
        self.labels = {}
        self.registers = {'AX': 0, 'BX': 0, 'CX': 0, 'DX': 0}
        self.command_list = {}
        self.instruction_pointer = 0
        self.cycle = 0
        self._init_command_list()

    def _init_command_list(self):
        self.command_list = {
            Command.ADD: self.command_add,
            Command.CMP: self.command_cmp,
            Command.CYCLE: self.command_cycle,
            Command.DEC: self.command_dec,
            Command.DIV: self.command_div,
            Command.DUP: self.command_dup,
            Command.HALT: self.command_halt,
            Command.INC: self.command_inc,
            Command.JMP: self.command_jmp,
            Command.JG: self.command_jg,
            Command.JL: self.command_jl,
            Command.JNZ: self.command_jnz,
            Command.JZ: self.command_jz,
            Command.LABEL: self.command_label,
            Command.MOD: self.command_mod,
            Command.MOV: self.command_mov,
            Command.MUL: self.command_mul,
            Command.NOP: self.command_nop,
            Command.POP: self.command_pop,
            Command.PRINT: self.command_print,
            Command.PUSH: self.command_push,
            Command.SQRT: self.command_sqrt,
            Command.STR: self.command_string,
            Command.SUB: self.command_sub,
            Command.SWAP: self.command_swap
        }

    def load_program(self, program):
        self.stack.clear()
        self.program = program
        self.labels = {line[:-1]: i for i, line in enumerate(program) if line.endswith(':')}
        self.instruction_pointer = 0
        self.cycle = 0

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

    def command_inc(self, args):
        self.stack.append(self.stack.pop() + 1)

    def command_dec(self, args):
        self.stack.append(self.stack.pop() - 1)

    def command_sqrt(self, args):
        self.stack.append(math.sqrt(self.stack.pop()))

    def command_dup(self, args):
        self.stack.append(self.stack[-1])

    def command_cycle(self, args):
        self.stack.append(self.cycle)

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

    def command_print(self, args):
        if ';' in args:
            print(self.stack.pop(), end='')
        elif ',' in args:
            print(self.stack.pop(), end=' ')
        else:
            print(self.stack.pop())

    def command_string(self, args):
        self.stack.append(' '.join(args))

    def run(self):
        for cycle in range(20000):
            self.cycle = cycle
            if self.instruction_pointer >= len(self.program):
                #print(f"Cycle: {cycle}")
                break
            command_string = self.program[self.instruction_pointer]
            command, args = self.parse_command(command_string)
            self.execute_command(command, args)
