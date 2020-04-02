import matplotlib.pyplot as plt
import numpy as np
import math

def plot_slotted_ALOHA(start, end, num_sample):
    g = np.linspace(start, end, num_sample)
    s = g*(math.e**-g)
    plt.plot(g, s, label = "Slotted ALOHA")

def plot_pure_ALOHA(start, end, num_sample):
    g = np.linspace(start, end, num_sample)
    s = g*(math.e**(-2*g))
    plt.plot(g, s, label = "Pure ALOHA")

def plot_nonpersistent_CSMA(start, end, a, num_sample):
    g = np.linspace(start, end, num_sample)
    numerator = g*(math.e**(-a*g))
    denominator = g*(1 + 2*a) + math.e**(-a*g)
    s = numerator/denominator
    plt.plot(g, s, label = "Non-persistent CSMA")

def plot_1_persistent_CSMA(start, end, a, num_sample):
    g = np.linspace(start, end, num_sample)
    numerator = g*(1 + g + a*g*(1 + g + a*g/2))*math.e**(-g*(1 + 2*a))
    denominator = g*(1 + 2*a) - (1 - math.e**(-a*g)) + (1 + a*g)*math.e**(-g*(1 + a))
    s = numerator/denominator
    plt.plot(g, s, label = "1-persistent CSMA")

def plot_p_persistent_CSMA(start, end, a, p, num_sample):
    g = np.linspace(start, end, num_sample)
    numerator = (a + p)*g*math.e**(-(a + p)*g) - p*g*math.e**(-(2*a + p)*g)
    denominator = (1 + a)*(1 - math.e**(-a*g)) + a*math.e**(-(a + p)*g)
    s = numerator/denominator
    plt.plot(g, s, label = "p-persistent CSMA")

a = 0.01
p = 0.1
num_sample = 10000

plot_slotted_ALOHA(0, 100, num_sample)
plot_pure_ALOHA(0, 100, num_sample)
plot_nonpersistent_CSMA(0, 100, a, num_sample)
plot_1_persistent_CSMA(0, 100, a, num_sample)
plot_p_persistent_CSMA(0, 100, a, p, num_sample)

plt.xscale('log')
plt.legend()
plt.xlabel("Offered Channel Traffic")
plt.ylabel("Throughput")
plt.show()