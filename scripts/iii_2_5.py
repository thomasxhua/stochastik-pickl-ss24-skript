import numpy as np
import math
import matplotlib.pyplot as plt

def X():
    coin_heads = np.random.random() < (1/2)
    if coin_heads:
        return 1/2
    return math.sqrt(np.random.random())

def V_X(b):
    if b < (1/2):
        return (1/2) * b**2
    if b == (1/2):
        return 5/8
    if 1/2 < b:
        return (1/2) + (1/2) * b**2

N = 10000

randoms = [X() for _ in range(0,N)]

STEPS = 1000
xs    = [x/STEPS for x in list(range(0,STEPS+1))]

def smaller_than(x, lst):
    count = 0
    for e in lst:
        if e <= x:
            count += 1
    return count

counts = [smaller_than(x, randoms)/N for x in xs]

V_Xs = [V_X(x) for x in xs]

plt.plot(counts, linestyle='-', linewidth=3)
plt.plot(V_Xs, linestyle='--')

plt.grid(True)
ticks = np.linspace(0, STEPS, num=11)
tick_labels = np.linspace(0, 1, num=11)  
plt.xticks(ticks, [f'{label:.1f}' for label in tick_labels])
plt.ylim(0.0, 1.0) 

y_values = []

for y_val in y_values:
    plt.axhline(y=y_val, color='red', linestyle='--', label=f'y={y_val}')

plt.show()
