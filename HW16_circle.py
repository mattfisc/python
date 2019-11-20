import random
import math
import matplotlib.pyplot as plt
import operator

def tuples():
    x = []
    y = []
    for i in range(1000):
        r1 = round(random.uniform(-1, 1), 3)
        r2 = round(random.uniform(-1, 1), 3)
        distance_from_origin = math.sqrt((0 - r1) ** 2 + (0 - r2) ** 2)

        if distance_from_origin < 1.0: 
            x.append(r1)
            y.append(r2)
    a = list(zip(x, y))
    return a


def circles():
    my_tuple = tuples()
    plt.scatter(*zip(*my_tuple))  

    plt.title("Plot")
    plt.xlabel('x :')
    plt.ylabel('y :')

    plt.show()


circles()