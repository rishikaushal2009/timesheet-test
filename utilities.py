from random import choice
from random import randint

def rand_timesheet():
    content = []
    
    for _ in range(randint(1, 10)):
        line = []
        time = 0
        
        for _ in range(randint(1, 3)):
            a = rand_time(time, time + 3)
            b = rand_time(time + 4, time + 7)
            line.append(f"{a}-{b}")
            time += 8
            
        content.append(", ".join(line))
            
    return "\n".join(content)

def rand_time(start, end):
    time = f"{randint(start, end)}"
    
    if randint(0, 1):
        time += f":{choice(['00', '15', '30', '45'])}"
        
    return time
#print rand_time(11:30,1)
