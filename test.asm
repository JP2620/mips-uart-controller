ANDI R31, R31, 0      ; reg[31] = 0
ADDI R0, R31, 2       ; fib(n-1)
ADDI R1, R31, 3       ; fib(n)
ADDI R2, R31, 2       ; n
ADDI R3, R31, 1       ; reg[3] = 1
XOR  R0, R0, R1        ; SWAP reg[0] and reg[1] using XOR
XOR  R1, R0, R1        ; SWAP reg[0] and reg[1] using XOR
XOR  R0, R0, R1        ; SWAP reg[0] and reg[1] using XOR
ADDU R1, R1, R0        ; fib(n) = fib(n-1) + fib(n)
SUBU R2, R2, R3        ; n = n - 1
BNE  R2, R31, -6      ; if n != 0 goto -6
SB R1, 0(R31)
ANDI R1, R1, 0
J 16
ADDI R1, R1, 9
NOP
LB R1, 0(R31)
ADDU R1, R1, R1
NOP
NOP
NOP
NOP
HALT