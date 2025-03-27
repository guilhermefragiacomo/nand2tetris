// Multiplies two numbers
// Starts setting the result (R2) to 0
// R0 and R1 is going to be the number to be multiplied, R2 serving as a counter
// R0 is going to be added to R2 as R1 decrements
// The program will only stop when R1 is less or equal to 0.

(BEGIN)
	@R2
	M=0

(MULT)
	@R1
	D=M
	@END
	D;JLE

	@R0
	D=M
	@R2
	M=M+D

	@R1
	M=M-1

	@MULT
	0;JMP

(END)
	@END
	0;JMP