// Turn the entire screen into black when the keyboard is pressed, otherwise it stays white
// Checks if the keyboard memory address is different than zero, if so, turns the color that the program is going to use to draw to black and starts drawing, otherwise, turns into white and begin to draw
// At the DRAW section the program simply stores the color and send it to the current pixel address. Than it checks if the current pixel is the last one, if so, the program loop into CHECK_KEYBOARD


(BEGIN)
	@24576
	D=A
	@keyboard
	M=D

(CHECK_KEYBOARD)
	@24575
	D=A
	@current
	M=D

	@keyboard
	A=M
	D=M
	@fill_color
	M=-1
	@DRAW
	D;JNE

	@fill_color
	M=0

(DRAW)
	@fill_color
	D=M
	@current
	A=M
	M=D

	@current
	D=M
	@16384
	D=D-A
	@CHECK_KEYBOARD
    // if it was the last pixel to be drawn, than get back to check the keyboard
	D;JLE

	@current
	M=M-1
    
    // otherwise, just continue drawing
	@DRAW
	0;JMP