# palette

`palette` is a tiny library for choosing nice-looking colors for Python plots that are are also color-blind friendly.

### Usage

`palette` exports one function, `pc()`, which returns a color name. If called with no arguments, it will cycle through eight different colors:

```Python
from palette import pc

plt.plot(x1, y1, pc(), lw=2)
plt.plot(x2, y2, pc(), lw=2)
plt.plot(x3, y3, pc(), lw=2)
plt.plot(x4, y4, pc(), lw=2)
plt.plot(x5, y5, pc(), lw=2)
plt.plot(x6, y6, pc(), lw=2)
plt.plot(x7, y7, pc(), lw=2)
plt.plot(x8, y8, pc(), lw=2)
```

If you supply a color name (`black`, `red`, `blue`, `green`, `orange`, `purple`, `brown`, or `gray`) it will return a hand-picked variant of that color.

```Python
from palette import pc

plt.plot(x1, y1, pc("r"), lw=3)
```

Abbreivations for these colors will also work (`k`, `r`, `b`, `g`, `o`, `p`, `n`, or `a`).

If you supply both a color name and a float between 0 and 1, it will return a gradation of that color with 0 being the darkest and 1 being the lightest.

```Python
from palette import pc

for a in np.linspace(0, 1, 10):
    plt.plot(x1, f(x1, a), pc("b"))
```

A value of 0.5 will always return the default gradation of that color.
