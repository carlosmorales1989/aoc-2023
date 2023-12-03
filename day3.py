import re

engine = []

width = 0
height = 0

class PartNumber:
    def __init__(self, match) -> None:
        self.number = int(match.group(0))
        self.start = match.start(0)
        self.end = match.end(0)

    def __str__(self) -> str:
        return f"Part {self.number}: [{self.start}-{self.end}]"

def bound_x(x):
    return max(min(x,width),0)

def bound_y(y):
    return max(min(y,height),0)

number_pattern = re.compile(r"([0-9]+)")
symbol_pattern = re.compile(r"([^0-9.])")
anti_dot_pattern = re.compile(r"([^.])")
result = 0

gears = {}

def add_part_to_symbol(part, symbol, symbol_row, symbol_col):
    if symbol != "*":
        return
    pos_str = f"{symbol_row},{symbol_col}"
    if not pos_str in gears:
        gears[pos_str] = []
    gears[pos_str].append(part)


with open('data/day3') as day3:
    engine = [line.strip() for line in day3]
    height = len(engine)
    width = len(engine[0])
    parts = []
    for row in range(len(engine)):
        line = engine[row]
        partMatch = number_pattern.search(line)
        
        while partMatch:
            part = PartNumber(partMatch)
            print(f"Analyzing {part}")
            parts.append(part)
            partMatch = number_pattern.search(line, part.end)
            valid = False

            if row > 0:
                found_symbol = symbol_pattern.search(engine[row-1][bound_x(part.start-1):bound_x(part.end+1)])
                if found_symbol:
                    print(f"Matched previous row: {found_symbol.group(0)}:{found_symbol.start(0)}-{found_symbol.end(0)}")
                    valid = True
                    add_part_to_symbol(part, found_symbol.group(0), row-1, bound_x(part.start-1) + found_symbol.start())

            if row < height-1:
                found_symbol = symbol_pattern.search(engine[row+1][bound_x(part.start-1):bound_x(part.end+1)])
                if found_symbol:
                    print(f"Matched next row: {found_symbol.group(0)}:{found_symbol.start(0)}-{found_symbol.end(0)}")
                    valid = True
                    add_part_to_symbol(part, found_symbol.group(0), row+1, bound_x(part.start-1) + found_symbol.start())

            found_symbol = symbol_pattern.search(engine[row][bound_x(part.start-1):bound_x(part.start)])                
            if found_symbol:
                print(f"Matched same row (before): {found_symbol.group(0)}")
                valid = True
                add_part_to_symbol(part, found_symbol.group(0), row, part.start-1)

            found_symbol = symbol_pattern.search(engine[row][bound_x(part.end):bound_x(part.end+1)])                
            if found_symbol:
                print(f"Matched same row (after): {found_symbol.group(0)}")
                valid = True
                add_part_to_symbol(part, found_symbol.group(0), row, part.end)

            if valid:
                result += part.number
            else:
                print(f"Not valid {part.number}")
print(gears)
print(sum([gear[0].number*gear[1].number for gear in gears.values() if len(gear)==2]))

print(result)