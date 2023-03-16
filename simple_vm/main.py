from stack_machine import StackMachine


def main():
    # Multiplying 1 through 10
    program = [
        'PUSH 1',
        'PUSH 1',
        'LOOP:',
        'DUP',
        'PUSH 10',
        'CMP',
        'JG END_LOOP',
        'MOV AX',
        'MUL',
        'PUSH AX',
        'PUSH 1',
        'ADD',
        'JMP LOOP',
        'END_LOOP:',
        'POP',
        'HALT'
    ]

    stack_machine = StackMachine()
    stack_machine.load_program(program)
    stack_machine.run()
    print("Result:", stack_machine.stack[-1])


if __name__ == '__main__':
    main()