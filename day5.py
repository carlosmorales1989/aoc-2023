import re

seed_pattern = re.compile(r"seeds:([0-9 ]+)")
map_pattern = re.compile(r"(?P<source>[a-z]+)-to-(?P<destination>[a-z]+) map:")

class Interval:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
    
    def __str__(self) -> str:
        return f"{self.start}-{self.end}"

    def __repr__(self) -> str:
        return str(self)

class DestinationRanges:
    def __init__(self, destination) -> None:
        self.destination = destination
        self.ranges = []    
    
    def __str__(self) -> str:
        return f"{self.destination}=>{self.ranges}"
    
    def __repr__(self) -> str:
        return str(self)

class Range:
    def __init__(self, source, destination, length) -> None:
        self.source = source
        self.destination = destination
        self.length = length
    
    def __str__(self) -> str:
        return f"{self.source}-{self.destination}({self.length})"
    
    def __repr__(self) -> str:
        return str(self)
    
    def intersect(self, interval):
        initial = self.source
        final = self.source + self.length

        interval_start = interval.start
        interval_end = interval.end

        unprocessed_intervals = []
        processed_intervals = []


        if interval_start < initial and interval_end >= initial:
            unprocessed_intervals.append(Interval(interval_start, initial-1))
            interval_start = initial

        if interval_end > final and interval_start <= final:
            unprocessed_intervals.append(Interval(final+1,interval_end))
            interval_end = final

        if interval_start <= final and interval_end >= initial:            
            delta = self.destination-self.source
            processed_intervals.append(Interval(delta + interval_start, delta+ interval_end))

        print(f"Range:{self}, Interval:{interval}, p:{processed_intervals}, unp:{unprocessed_intervals}")
        return (processed_intervals, unprocessed_intervals)

def part1(values, ranges):
    new_values = []
    for value in values:
        new_value = None
        for range in ranges:
            if value >= range.source and value <= range.source+ range.length:
                new_value = range.destination + (value - range.source)
                #print(f"Mapping {value} to {new_value}")
                break
        if not new_value:
            #print(f"Mapping {value} to itself")
            new_value = value
        new_values.append(new_value)
    return new_values

def part2(intervals_list, ranges):
    part2_result = []    

    for interval_qu in intervals_list:                

        new_intervals = []        
        while len(interval_qu)>0:            
            interval = interval_qu.pop()
            processed = False
            for range in ranges:
                [processed_is, remaining_is] = range.intersect(interval)

                if len(processed_is) > 0:
                    interval_qu += remaining_is
                    new_intervals += processed_is
                    processed = True
                    break
            if not processed:
                new_intervals.append(interval)

        part2_result.append(new_intervals)
    return part2_result

with open('data/day5') as day5:
    line = day5.readline()
    day5.readline()    

    seeds = [int(seed.strip()) for seed in seed_pattern.match(line).group(1).split()]

    categories = {}    

    line = day5.readline()
    source_cat = None
    destination_cat = None
    while line:
        line = line.strip()
        category_match = map_pattern.match(line)

        if category_match:
            source_cat = category_match.group("source")
            destination_cat = category_match.group("destination")

            if source_cat not in categories:
                categories[source_cat] = DestinationRanges(destination_cat)           
            
        elif len(line)>0:
            destination,source,length = (int(cat.strip()) for cat in line.split(" "))
            
            categories[source_cat].ranges.append(Range(source, destination, length))

        line = day5.readline()

    print(categories)

    last_category = "seed"
    
    values = seeds
    intervals = []
    for i in range(0,len(seeds),2):
        intervals.append([Interval(seeds[i], seeds[i]+seeds[i+1])])


    while last_category in categories:
        ranges = categories[last_category].ranges
            
        values = part1(values, ranges)

        intervals = part2(intervals, ranges)

        last_category = categories[last_category].destination
        print(f"{last_category}=>{values}")
        print(f"{last_category}=>{intervals}")
    
    print(min(values))
    print(min(min(subinterval.start for subinterval in interval) for interval in intervals))

