instructions = [{"(":1, ")": -1}[i] for i in input()]
floor = 0
for i, instruction in enumerate(instructions):
    floor += instruction
    if floor < 0:
        print(i+1)
        exit()