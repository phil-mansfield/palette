import matplotlib.pyplot as plt

# Colors picked by hand using http://colorbrewer2.org/ as a base and then
# micromanaged using coolors.co.

###########################
## Functions and Globals ##
###########################

color_index = 0

def pc(*args):
    if len(args) == 0:
        global color_index
        color = colors[color_index % 8]
        color_index += 1
        return pc(color, 0.5)

    elif len(args) == 1:
        return pc(args[0], 0.5)

    elif len(args) == 2:
        return interpolators[args[0]].hex_string(args[1])

    else:
        raise ValueError("pc() takes 2 arguements at most, %d given" %len(args))

#####################
## Pyplot Wrappers ##
#####################

def figure(**kwargs):
    pass

##################################
## Helper Classes and Functions ##
##################################

class Interpolator(object):

    def __init__(self, palette):
        self.r, self.g, self.b = split_palette(palette)
        self.x = [i / float(len(palette) - 1) for i in xrange(len(palette))]

    def hex_string(self, x0):
        if x0 < 0 or x0 > 1: 
            raise ValueError("Value outside of the range [0, 1] given to pc().")

        x, r, g, b = self.x, self.r, self.g, self.b

        for i in xrange(len(self.x)):
            if x[i] >= x0:
                if x0 == 1.0: i -= 1

                dx, run = x0 - x[i], float(x[i + 1] - x[i])
                
                r0 = int(r[i] + (r[i+1] - r[i])/run*dx)
                g0 = int(g[i] + (g[i+1] - g[i])/run*dx)
                b0 = int(b[i] + (b[i+1] - b[i])/run*dx)

                return "#%s%s%s" % (
                    hex_string(r0), hex_string(g0), hex_string(b0)
                )

        assert(0)

def split_palette(palette):
    r, g, b = [], [], []
    for color in palette:
        r.append(int(color[1:3], 16))
        g.append(int(color[3:5], 16))
        b.append(int(color[5:7], 16))
    return r, g, b

def hex_string(n):
    hs = hex(n)[2:]
    if len(hs) == 1: hs = "0%s" % hs
    return hs

##########
## Data ##
##########

palette = [
    "#171717", # black ("eerie black")
    "#e41a1c", # red ("lust")
    "#377eb8", # blue ("tufts blue")
    "#4daf4a", # green ("may green")
    "#ff9021", # orange ("carrot orange")
    "#984ea3", # purple ("purpureus")
    "#a65628", # brown ("ruddy brown")
    "#7F7F7F", # gray ("trolley grey")
]

black_palette = [
    "#171717",
    "#171717",
    "#171717",
    "#171717",
    "#171717",
    "#171717",
    "#171717",
    "#171717",
    "#171717", ###
    "#2C2C2C",
    "#414141",
    "#565656",
    "#6B6B6B",
    "#808080",
    "#959595",
    "#AAAAAA",
    "#BFBFBF",
]

red_palette = [
    "#3F0808",
    "#530A0B",
    "#680C0D",
    "#7D0F10",
    "#921112",
    "#A61315",
    "#BB1617",
    "#D0181A",
    "#E41A1C", ###
    "#E62E30",
    "#E84345",
    "#EB5859",
    "#ED6D6E",
    "#F08283",
    "#F29697",
    "#F5ABAC",
    "#F7C0C1",
]

blue_palette = [
    "#0F2333",
    "#142E43",
    "#193A54",
    "#1E4565",
    "#235176",
    "#295C86",
    "#2E6897",
    "#3273A8",
    "#377EB8", ###
    "#4989BE",
    "#5B95C4",
    "#6DA1CB",
    "#7FACD1",
    "#91B8D8",
    "#A4C4DE",
    "#B6D0E5",
    "#C8DBEB",
]

green_palette = [
    "#153015",
    "#1C401B",
    "#235022",
    "#2A6029",
    "#327030",
    "#398036",
    "#40903D",
    "#46A044",
    "#4DAF4A", ###
    "#5DB65A",
    "#6DBD6A",
    "#7DC47B",
    "#8DCC8B",
    "#9DD39C",
    "#AEDAAC",
    "#BEE1BD",
    "#CEE9CD",
]

orange_palette = [
    "#462809",
    "#5D350C",
    "#74420F",
    "#8C4F12",
    "#A35C15",
    "#BA6919",
    "#D1761C",
    "#E8831E",
    "#FF9021", ###
    "#FF9A35",
    "#FFA449",
    "#FFAE5D",
    "#FFB871",
    "#FFC285",
    "#FFCC9A",
    "#FFD6AE",
    "#FFE0C2",
]

brown_palette = [
    "#2E180B",
    "#3D200F",
    "#4C2813",
    "#5B2F16",
    "#6A371A",
    "#793F1E",
    "#884721",
    "#974F25",
    "#A65628", ###
    "#AE653B",
    "#B6744F",
    "#BE8462",
    "#C69376",
    "#CEA289",
    "#D6B29D",
    "#DEC1B0",
    "#E6D0C4",
]

purple_palette = [
    "#2A162D",
    "#381D3C",
    "#46244B",
    "#532B59",
    "#613268",
    "#6F3977",
    "#7D4086",
    "#8B4795",
    "#984EA3", ###
    "#A15EAB",
    "#AA6EB3",
    "#B47EBC",
    "#BD8EC4",
    "#C69ECC",
    "#D0AED5",
    "#D9BEDD",
    "#E2CEE5"
]

gray_palette = [
    "#232323",
    "#2F2F2F",
    "#3A3A3A",
    "#464646",
    "#515151",
    "#5D5D5D",
    "#686868",
    "#747474",
    "#7F7F7F", ###
    "#8A8A8A",
    "#969696",
    "#A1A1A1",
    "#ADADAD",
    "#B9B9B9",
    "#C4C4C4",
    "#D0D0D0",
    "#DCDCDC",
]

colors = ["black", "red", "blue", "green",
          "orange", "purple", "brown", "gray"]
short_colors = ["k", "r", "b", "g", "o", "p", "n", "a"]
palettes = [black_palette, red_palette, blue_palette, green_palette,
            orange_palette, purple_palette, brown_palette, gray_palette]
_interpolators = [Interpolator(palettes[i]) for i in xrange(len(colors))]
interpolators = dict(
    {colors[i]: _interpolators[i] for i in xrange(len(colors))},
    **{short_colors[i]: _interpolators[i] for i in xrange(len(colors))}
)
