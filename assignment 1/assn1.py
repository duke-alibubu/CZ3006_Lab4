import matplotlib.pyplot as plt
import numpy as np
import math

def plot_slotted_ALOHA(g):   
    s = g*(math.e**-g)
    plt.plot(g, s, label = "Slotted ALOHA")

def plot_pure_ALOHA(g):   
    s = g*(math.e**(-2*g))
    plt.plot(g, s, label = "Pure ALOHA")

def plot_non_persistent_CSMA(a, g):
    numerator = g*(math.e**(-a*g))
    denominator = g*(1 + 2*a) + math.e**(-a*g)
    s = numerator/denominator
    plt.plot(g, s, label = "Non-persistent CSMA")

def plot_1_persistent_CSMA(a, g):   
    numerator = g*(1 + g + a*g*(1 + g + a*g/2))*math.e**(-g*(1 + 2*a))
    denominator = g*(1 + 2*a) - (1 - math.e**(-a*g)) + (1 + a*g)*math.e**(-g*(1 + a))
    s = numerator/denominator
    plt.plot(g, s, label = "1-persistent CSMA")

def plot_p_persistent_CSMA(a, p, g):   
    numerator = (a + p)*g*math.e**(-(a + p)*g) - p*g*math.e**(-(2*a + p)*g)
    denominator = (1 + a)*(1 - math.e**(-a*g)) + a*math.e**(-(a + p)*g)
    s = numerator/denominator
    plt.plot(g, s, label = "p-persistent CSMA")

a = 0.01
p = 0.1
start = 0
end = 100
num_sample = 10000
g = np.linspace(start, end, num_sample)


plot_slotted_ALOHA(g)
plot_pure_ALOHA(g)
plot_non_persistent_CSMA(a, g)
plot_1_persistent_CSMA(a, g)
plot_p_persistent_CSMA(a, p, g)

plt.xscale('log')
plt.legend()
plt.xlabel("Offered Channel Traffic")
plt.ylabel("Throughput")
plt.show()