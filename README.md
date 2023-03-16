# simple_vm

## stack based simple stack machine

### ChatGPT를 활용해서 만든 간단한 Stack 베이스의 VM 입니다.    

### 구조  
* Stack 1개
* AX,BX,CX,DX 4개의 레지스터

### 명령어 소개  
* PUSH <value>: Push a value onto the stack. e.g., PUSH 10
* POP: Remove and return the top value from the stack.
* ADD: Remove the top two values from the stack, calculate their sum, and push the result onto the stack.
* SUB: Remove the top two values from the stack, calculate their difference, and push the result onto the stack.
* MUL: Remove the top two values from the stack, calculate their product, and push the result onto the stack.
* DIV: Remove the top two values from the stack, calculate their division, and push the result onto the stack.
* MOD: Remove the top two values from the stack, calculate their remainder, and push the result onto the stack.
* DUP: Copy the top value from the stack and push it onto the stack.
* SWAP: Swap the top two values on the stack.
* JMP <label>: Move program execution to the given label. e.g., JMP LOOP
* JG <label>: If the top value on the stack is greater than 0, move program execution to the given label.
* JL <label>: If the top value on the stack is less than 0, move program execution to the given label.
* JZ <label>: If the top value on the stack is 0, move program execution to the given label.
* JNZ <label>: If the top value on the stack is not 0, move program execution to the given label.
* CMP: Compare the top two values on the stack and push the result onto the stack.  
  (-1: First value is smaller, 0: Both values are equal, 1: First value is larger)
* MOV <register>: Move the top value from the stack to the specified register (AX, BX, CX, or DX).
* NOP: Perform no operation. This command is ignored in the program.
* HALT: Stop program execution.  


#### 10!을 구하는 프로그램의 예제 입니다.  
~~~
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
~~~