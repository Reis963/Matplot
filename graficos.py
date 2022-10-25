from itertools import count
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import lines
from matplotlib import patches
from matplotlib.patheffects import withStroke

counts = [1, 3, 21, 4, 25]
names = ["Recursos(Cotistas)", "Recursos", "Inaptos", "Aptos", "Aprovados"]

# The positions for the bars
# This allows us to determine exactly where each bar is located
y = [i * 0.9 for i in range(len(names))]

# The colors
BLUE = "#076fa2"
RED = "#E3120B"
BLACK = "#202020"
GREY = "#a2a2a2"

fig, ax = plt.subplots(figsize=(12, 7))

ax.barh(y, counts, height=0.65, align="edge", color=BLUE)

ax.xaxis.set_ticks([i * 5 for i in range(0, 14)])
ax.xaxis.set_ticklabels([i * 5 for i in range(0, 14)], size=16, fontfamily="DejaVu Sans", fontweight=100)
ax.xaxis.set_tick_params(labelbottom=False, labeltop=True, length=0)

ax.set_xlim((0, 70))
ax.set_ylim((0, len(names) * 0.9 - 0.2))

# Set whether axis ticks and gridlines are above or below most artists.
ax.set_axisbelow(True)
ax.grid(axis="x", color="#A8BAC4", lw=1.2)
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["left"].set_lw(1.5)
# This capstyle determines the lines don't go beyond the limit we specified
# see: https://matplotlib.org/stable/api/_enums_api.html?highlight=capstyle#matplotlib._enums.CapStyle
ax.spines["left"].set_capstyle("round")

# Hide y labels
ax.yaxis.set_visible(False)

fig

PAD = 0.3
for name, count, y_pos in zip(names, counts, y):
    x = 0
    color = "white"
    path_effects = None
    if count < 8:
        x = count
        color = BLUE
        path_effects = [withStroke(linewidth=6, foreground="white")]

    ax.text(
        x + PAD, y_pos + 0.6 / 2, name,
        color=color, fontfamily="DejaVu Sans", fontsize=18, va="center",
        path_effects=path_effects
    )
fig

# Make room on top and bottom
# Note there's no room on the left and right sides
fig.subplots_adjust(left=0.005, right=1, top=0.8, bottom=0.1)

# Add title
fig.text(
    0, 0.925, "UNEB",
    fontsize=22, fontweight="bold", fontfamily="DejaVu Sans"
)
# Add subtitle
fig.text(
    0, 0.875, "2ª Chamada - SISU 2022.1",
    fontsize=20, fontfamily="DejaVu Sans"
)

# Add caption
source = "Sources: http://www.sisu.uneb.br/index.php/sisu-edicoes-anteriores/#2021.2"
fig.text(
    0, 0.06, source, color=GREY,
    fontsize=14, fontfamily="DejaVu Sans"
)

# Add authorship
fig.text(
    0, 0.005, "Diego Reis", color=GREY,
    fontsize=16, fontfamily="DejaVu Sans"
)

# Add line and rectangle on top.
#fig.add_artist(lines.Line2D([0, 1], [1, 1], lw=3, color=RED, solid_capstyle="butt"))
#fig.add_artist(patches.Rectangle((0, 0.975), 0.05, 0.025, color=RED))

# Set facecolor, useful when saving as .png
fig.set_facecolor("white")
fig

fig.savefig("plot.png", dpi=300)

################################################################################################
# dataset
#height = [65, 22, 43, 12, 5]
#bars = ('Aprovados','Aptos','Inaptos','Recursos','Recursos(Cotistas)',)
#y_pos = np.arange(len(bars))


# horizontal bars
#plt.barh(y_pos, height)

# names x-axis
#plt.yticks(y_pos, bars)

# title
#plt.title('UNEB - SISU 2022.1')

# show graphic
# plt.show()
