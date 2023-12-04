import re
from functools import reduce
from math import pow
import operator

card_pattern = re.compile(r"Card(?: +)(?P<card>[0-9]+):(?P<win>[0-9 ]*)\|(?P<number>[0-9 ]*)")
result = 0
winners=[]
with open('data/day4') as day4:
    for line in day4:
        match = card_pattern.match(line.strip())
        winning_nums = [int(num) for num in match.group("win").strip().split(" ") if len(num) > 0]
        numbers = [int(num) for num in match.group("number").strip().split(" ") if len(num) > 0]
        matching_numbers = [number for number in numbers if number in winning_nums]
        if len(matching_numbers) == 0:
            score = 0
        else:
            score = int(pow(2, len(matching_numbers)-1))
        result+=score
        winners.append(len(matching_numbers))

won_copies = [1]*len(winners)
for i in range(len(won_copies)):
    for j in range(i+1, min(i+1+winners[i], len(won_copies))):
        won_copies[j] += won_copies[i]
print(won_copies)
print(result)
print(sum(won_copies))