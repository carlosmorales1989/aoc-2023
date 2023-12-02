import re
from functools import reduce # Valid in Python 2.6+, required in Python 3
import operator

pattern = r"Game (?P<game>[0-9]+):(?P<content>[0-9a-z ,;]+)"
show_pattern = r"([0-9]+) (blue|red|green)"

max_nums = {
    "red": 12,
    "green": 13,
    "blue": 14
}


result = 0
result_2 = 0
with open('data/day2') as day2:    
    for line in day2:
        m = re.match(pattern, line)
        shows = m.group("content").split(";")
        possible = True
        min_nums = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for show in shows:
            draws = re.findall(show_pattern, show)
            for draw in draws:
                if int(draw[0]) > max_nums[draw[1]]:
                    possible = False
                min_nums[draw[1]] = max(int(draw[0]),min_nums[draw[1]])
        if possible:
            result += int(m.group("game"))
        result_2 += reduce(operator.mul, [min_nums[color] for color in min_nums], 1)
print(result)
print(result_2)
