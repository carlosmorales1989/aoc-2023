import re

num_map = {"one": "1",
           "two": "2",
           "three": "3",
           "four":"4",
           "five":"5",
           "six":"6",
           "seven":"7",
           "eight":"8",
           "nine":"9",}

def translate_num(num):
    if num in num_map:
        return num_map.get(num)
    else:
        return num

def get_result(pattern, line):
    nums = re.findall(pattern, line)
    translated_nums = [i for i in map(translate_num, nums)]
    return int(translated_nums[0]+translated_nums[-1])   

with open('data/day1') as day1:
    result_1 = 0
    result_2 = 0
    for line in day1:
        start = None
        end = None
        for i in range(len(line)):
            if not start and line[i] >= '0' and line[i] <= '9':
                start = line[i]
            if not end and line[-i-1] >= '0' and line[-i-1] <= '9':
                end = line[-i-1]        

        pattern_1 = r"(?=([0-9]))"
        pattern_2 = r"(?=(one|1|two|2|three|3|four|4|five|5|six|6|seven|7|eight|8|nine|9))"
        result_1 += get_result(pattern_1,line)
        result_2 += get_result(pattern_2,line)


    print(result_1)
    print(result_2)