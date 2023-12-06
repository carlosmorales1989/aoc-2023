
def calc_distance(button_time, total_time):
    return button_time*(total_time - button_time)

with open('data/day6_2') as day6:
    times = [int(time.strip()) for time in day6.readline().split(" ")[1:] if len(time)>0]
    distances = [int(time.strip()) for time in day6.readline().split(" ")[1:] if len(time)>0]

    result = 1
    for i in range(len(times)):
        possibilities = []
        ub = times[i]
        lb = int(times[i]/2)
        while True:
            next_i = int((lb+ub)/2)
            if calc_distance(next_i,times[i]) > distances[i]:
                lb = next_i
            else:
                ub = next_i
            if ub-lb <=1:
                break
        p_result = 2*(lb-int(times[i]/2))
        if times[i]%2 ==0:
            p_result+=1
        print(f"Num possibilities:{p_result}")
        print("--------------")
        result*=p_result
    print(result)