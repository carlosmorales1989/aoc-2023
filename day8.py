part2 = True

with open('data/day8') as day8:
    instructions = day8.readline().strip()
    day8.readline()
    line = day8.readline()
    network = {}
    while line:
        line = line.replace("(","").replace(")","")
        info = line.split("=")
        children = [node.strip() for node in info[1].split(",")]
        network[info[0].strip()] = {'L': children[0], 'R': children[1]}
        line = day8.readline()

    if not part2:

        step_count = 0
        node = 'AAA'
        while node!='ZZZ':        
            node = network[node][instructions[step_count%len(instructions)]]
            step_count+=1
        print(step_count)

    else:
        part2_nodes = [node for node in network if node[-1]=='A']    

        for start_node in part2_nodes:
            node = start_node
            step_count = 0
            while node[-1] !='Z':
                node = network[node][instructions[step_count%len(instructions)]]
                step_count+=1
            print(step_count)
        

