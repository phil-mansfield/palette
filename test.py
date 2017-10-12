import matplotlib.pyplot as plt
import numpy as np
import palette
from palette import pc
import string

ls="-"
lw=3

def gaussian(mu, sigma, x):
    return np.exp(-(x - mu)**2 / (2 * sigma**2)) / np.sqrt(2 *np.pi * sigma**2)

x = np.linspace(0, 1, 100)

for c in palette.colors[:0:-1]:
    plt.figure(figsize=(7, 7))

    plt.title("%s Range" % string.capwords(c), fontsize=17)

    for sigma in np.linspace(0.2, 1.0, 10):
        plt.plot(x, gaussian(sigma, sigma, x), ls, lw=lw, c=pc(c, sigma))

plt.figure(figsize=(7, 7))

plt.title("Color Families", fontsize=17)

x = np.linspace(-1, 1, 100)
plt.plot(x, gaussian(0, 0.5, x), ls, c=pc(), lw=lw)
plt.plot(x, gaussian(0.5, 0.5, x), ls, c=pc(), lw=lw)
plt.plot(x, gaussian(0.25, 0.4, x), ls, c=pc(), lw=lw)
plt.plot(x, gaussian(-0.3, 0.6, x), ls, c=pc(), lw=lw)
plt.plot(x, gaussian(-0.5, 0.3, x), ls, c=pc(), lw=lw)
plt.plot(x, gaussian(-0.75, 1.0, x), ls, c=pc(), lw=lw)
plt.plot(x, gaussian(0.75, 0.75, x), ls, c=pc(), lw=lw)
plt.plot(x, gaussian(0.1, 0.35, x), ls, c=pc(), lw=lw)

plt.show()
