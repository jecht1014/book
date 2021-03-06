import random
import math
import numpy as np

def distance(coordinate1, coordinate2):
    result = 0
    for i in range(len(coordinate1)):
        result += math.pow(coordinate1[i]-coordinate2[i], 2)
    
    return math.sqrt(result)

# モンテカルロ法
monte_carlo_times = 1000000
count = 0
for i in range(monte_carlo_times):
    if (distance([random.random(), random.random()], [0, 0]) <= 1):
        count += 1
print('pi:{0} monte_carlo:{1}'.format(math.pi/4, count/monte_carlo_times))

# システマティック法
systematic_times = 1000
count = 0
suretsu = np.linspace(0, 1, systematic_times)
for x in suretsu.tolist():
    for y in suretsu.tolist():
        if (distance([x, y], [0, 0]) <= 1):
            count += 1
print('pi:{0} systematic:{1}'.format(math.pi/4, count/(systematic_times*systematic_times)))