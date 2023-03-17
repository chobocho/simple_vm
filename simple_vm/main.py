from stack_machine import StackMachine


def main():
    # Multiplying 1 through 10
    program_10_factorial = [
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
        'INC',
        'JMP LOOP',
        'END_LOOP:',
        'POP',
        'STR RESULT: ',
        'PRINT ,',
        'PRINT',
        'HALT'
    ]

    program_sqrt_144 = [
        'PUSH 144',
        'SQRT',
        'STR RESULT: ',
        'PRINT ,',
        'PRINT',
        'HALT'
    ]

    program_900 = [
        "PUSH 10",
        "PUSH 20",
        "ADD",
        "PUSH 30",
        "MUL",
        'STR RESULT: ',
        'PRINT ,',
        "PRINT",
        "HALT"
    ]

    program_sum_1000 = [
        "start:",
        "PUSH 0",  # Push the initial sum (0) onto the stack
        "PUSH 1",  # Push the start number (1) onto the stack
        "LOOP:",
        "DUP",
        "PUSH 1000",
        "CMP",  # Compare the current number with the end number
        "JG end_loop",  # If the current number is greater than the end number, jump to the loop label
        "MOV AX",
        "ADD",
        "PUSH AX",
        "INC",
        "JMP LOOP",
        "end_loop:",
        'POP',
        'STR RESULT: ',
        'PRINT ,',
        'PRINT',
        'STR Cycle: ',
        'PRINT ,',
        'CYCLE',
        'PRINT',
        "HALT",  # Stop the program
    ]

    stack_machine = StackMachine()
    stack_machine.load_program(program_10_factorial)
    stack_machine.run()

    stack_machine.load_program(program_sqrt_144)
    stack_machine.run()

    stack_machine.load_program(program_900)
    stack_machine.run()

    stack_machine.load_program(program_sum_1000)
    stack_machine.run()


if __name__ == '__main__':
    main()