def run_instructions(instructions, offset, f_during, f_after):
    cycle = 0
    register = 1
    for instr in instructions:
        if instr.startswith("noop"):
            f_during(cycle, register)
            cycle += 1
            if (cycle - offset) % 40 == 0:
                f_after(cycle, register)
        elif instr.startswith("addx"):
            f_during(cycle, register)
            cycle += 1
            if (cycle - offset) % 40 == 0:
                f_after(cycle, register)
            f_during(cycle, register)
            cycle += 1
            if (cycle - offset) % 40 == 0:
                f_after(cycle, register)
            register += int(instr.split()[1])


def get_input():
    with open("input.txt") as f:
        return [l.strip() for l in f.readlines()]
