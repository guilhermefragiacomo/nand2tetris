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

read_file = open("source_program.asm", "r")

count = 0
for x in read_file:
    if x.strip():
        
        print(x)
        line = ""
        if x[0] == '@':
            try:
                val = int(x[1:])
                line = f'{val:016b}'
            except Exception as e:
                if (x[1:]).strip() in symbol_table:
                    val = symbol_table.get(x[1:].strip())
                    line = f'{val:016b}'
        print(line)
        count += 1

write_file = open("binary_program.hack", "a") 

read_file.close()
write_file.close()