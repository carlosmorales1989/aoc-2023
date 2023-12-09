with open('data/day9') as day9:
    part1 = 0
    part2 = 0
    for line in day9:
        nums = [int(num) for num in line.strip().split()]
        result = [nums]
        while not all((num is None or num == 0 for num in result[-1])):
            new_row = [None]
            for i in range(1,len(result[-1])):
                if result[-1][i] != None and result[-1][i-1] != None:
                    new_row.append(result[-1][i] - result[-1][i-1])
                else:
                    new_row.append(None)            
            result.append(new_row)        
        print(result)

        last_num = 0
        for i in range(1,len(result)+1):
            last_num+= result[len(result)-i][-1]
        print(last_num)
        part1 += last_num

        last_num = 0
        for i in range(1,len(result)):  
            print(f"Row:{len(result)-i-1} Col: {len(result)-i-1}")          
            last_num = result[len(result)-i-1][len(result)-i-1] - last_num
        print(last_num)
        part2 += last_num
    print(part1)
    print(part2)