symbol_table = {
    "R0": 0,
    "R1": 1,
    "R2": 2,
    "R3": 3,
    "R4": 4,
    "R5": 5,
    "R6": 6,
    "R7": 7,
    "R8": 8,
    "R9": 9,
    "R10": 10,
    "R11": 11,
    "R12": 12,
    "R13": 13,
    "R14": 14,
    "R15": 15,
    "SCREEN": 16384,
    "KBD": 24576,
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4
}

dest_jump_table = {
    "": 0,
    "M": 1,
    "D": 2,
    "MD": 3,
    "A": 4,
    "AM": 5,
    "AD": 6,
    "AMD": 7,

    "JGT": 1,
    "JEQ": 2,
    "JGE": 3,
    "JLT": 4,
    "JNE": 5,
    "JLE": 6,
    "JMP": 7,
}

comp_table = {
    "0": 42,
    "1": 63,
    "-1": 58,
    "D": 12,
    "A": 48,
    "M": 48,
    "!D": 13,
    "!A": 49,
    "!M": 49,
    "-D": 15,
    "-A": 51,
    "-M": 51,
    "D+1": 31,
    "A+1": 55,
    "M+1": 55,
    "D-1": 14,
    "A-1": 50,
    "M-1": 50,
    "D+A": 2,
    "D+M": 2,
    "D-A": 19,
    "D-M": 19,
    "A-D": 7,
    "M-D": 7,
    "D&A": 0,
    "D&M": 0,
    "D|A": 21,
    "D|M": 21
}

read_file = open("source_program.asm", "r")

count = 0
variable_count = 16

for x in read_file:
    if x.strip():
        if x[0] == '(':
            if x[1:len(x[1:].strip())].strip() not in symbol_table:
                symbol_table[x[1:len(x[1:].strip())].strip()] = count
                count -= 1
        count += 1

read_file.close()
read_file = open("source_program.asm", "r")

write_file = open("binary_program.hack", "a") 

for x in read_file:
    if x.strip():
        if x[0] != "/":

            line = ""
            if x[0] == '@':
                try:
                    val = int(x[1:])
                    line = f'{val:016b}'
                except Exception as e:
                    if (x[1:]).strip() in symbol_table:
                        val = symbol_table.get(x[1:].strip())
                        line = f'{val:016b}'
                    else:
                        symbol_table[x[1:].strip()] = variable_count
                        line = f'{variable_count:016b}'
                        variable_count += 1
            else:
                if x[0] != "(":
                    line = "111"

                    list = x.strip().split("=")
                    dest = "000"
                    if "=" in x.strip():
                        dest = f'{dest_jump_table.get(list[0]):03b}'
                        list.pop(0)
                    list = list[0].strip().split(";")
                    if "M" in list[0]:
                        line += "1"
                    else:
                        line += "0"
                    line += f'{comp_table.get(str(list[0])):06b}'
                    line += dest
                    list.pop(0)
                    if ";" in x.strip():
                        line += f'{dest_jump_table.get(str(list[0])):03b}'
                    else:
                        line += "000"
            if (line != ""):
                print(x)
                print(line)
                write_file.write(line + "\n")
                count += 1

print(symbol_table)

read_file.close()
write_file.close()