import matplotlib.pyplot as plt
import numpy as np
import math

def plot_slotted_ALOHA(g):   
    s = g*(math.e**-g)
    plt.plot(g, s, label = "Slotted ALOHA", color = "red")

def plot_pure_ALOHA(g):   
    s = g*(math.e**(-2*g))
    plt.plot(g, s, label = "Pure ALOHA", color = "green")

def plot_non_persistent_CSMA(a, g):
    numerator = g*(math.e**(-a*g))
    denominator = g*(1 + 2*a) + math.e**(-a*g)
    s = numerator/denominator
    plt.plot(g, s, label = "Non-persistent CSMA", color = "blue")

def plot_1_persistent_CSMA(a, g):   
    numerator = g*(1 + g + a*g*(1 + g + a*g/2))*math.e**(-g*(1 + 2*a))
    denominator = g*(1 + 2*a) - (1 - math.e**(-a*g)) + (1 + a*g)*math.e**(-g*(1 + a))
    s = numerator/denominator
    plt.plot(g, s, label = "1-persistent CSMA", color = "yellow")

def plot_p_persistent_CSMA(a, p, g):
    pi0 = math.e**(-g*(1+a))
    t = (pi0**p - pi0)/(1 - pi0 - (pi0**p-pi0)*math.e**(-p*a*g))
    t1 = (math.e**(-a*g*p) - math.e**(-a*g))/(1 - math.e**(-a*g) - (math.e**(-a*g*p) - math.e**(-a*g)) * math.e**(-a*p*g))
    q = 1 - p
    Ps =  (pi0**p - pi0)/(q*(1-pi0)) - (1 - math.e**(-a*g*p))*(pi0**(1-q**2) - pi0)/(q*(1 - pi0) - q*math.e**(-2*a*g*p)*(pi0**p - pi0))
    Ps1 = (math.e**(-g*a*p) - math.e**(-a*g))/(q*(1-math.e**(-a*g))) - (1 - math.e**(-a*g*p))*(math.e**(-a*g*(1-q**2)) - math.e**(-g*a))/(q*(1 - math.e**(-g*a)) - q*math.e**(-2*g*a*p)*(math.e**(-g*a*p) - math.e**(-g*a)))

    numerator = (1 - math.e**(-a*g))*(Ps1*pi0 + Ps*(1 - pi0))
    denominator = (1 - math.e**(-a*g))*(a*t1*pi0 + a*t*(1 - pi0) + 1 + a) + a*pi0
    s = numerator/denominator
    plt.plot(g, s, label = "p-persistent CSMA", color = "purple")

a = 0.5
p = 0.01
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