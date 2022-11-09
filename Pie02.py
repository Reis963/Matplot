import matplotlib.pyplot as plt
import numpy as np

from matplotlib import lines
from matplotlib import patches

plt.style.use('_mpl-gallery-nogrid')


# make data
labels = 'Sim', 'Não', 'Às vezes'
sizes = [45.6, 45.6, 8.9]
#explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Não')
colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(sizes)))

# plot
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, radius=3, center=(4, 4), wedgeprops={"linewidth": 2, "edgecolor": "white"}, frame=False)

ax.set(xlim=(0, 8), xticks=np.arange(0, 0), ylim=(0, 8), yticks=np.arange(0, 0))

# The colors
BLUE = "#076fa2"
RED = "#E3120B"
BLACK = "#202020"
GREY = "#a2a2a2"

# Hide y labels
#ax.yaxis.set_visible(False)

#fig

# Make room on top and bottom
# Note there's no room on the left and right sides
#fig.subplots_adjust(left=0.005, right=1, top=0.8, bottom=0.1)

# Add title
fig.text(
    0, 0.925, "PIASC III",
    fontsize=22, fontweight="bold", fontfamily="DejaVu Sans"
)
# Add subtitle
fig.text(
    0, 0.875, "Infecções Sexualmente Transmíssiveis (IST)",
    fontsize=20, fontfamily="DejaVu Sans"
)
fig.text(
    0.005, 0.835, "Utilização de Preservativo",
    fontsize=15, fontfamily="DejaVu Sans"
)

# Add caption
source = "Fonte: Relatório PIASC III 2022.1"
fig.text(
    0, 0.04, source, color=GREY,
    fontsize=14, fontfamily="DejaVu Sans"
)

# Add authorship
#fig.text(
#    0, 0.005, "Diego Reis", color=GREY,
#    fontsize=16, fontfamily="DejaVu Sans"
#)

# This capstyle determines the lines don't go beyond the limit we specified
# see: https://matplotlib.org/stable/api/_enums_api.html?highlight=capstyle#matplotlib._enums.CapStyle
ax.spines["left"].set_capstyle("round")

# Add line and rectangle on top.
fig.add_artist(lines.Line2D([0, 1], [1, 1], lw=3, color=RED, solid_capstyle="butt"))
fig.add_artist(patches.Rectangle((0, 0.975), 0.05, 0.025, color=RED))

# Set facecolor, useful when saving as .png
fig.set_facecolor("white")

#fig.savefig("plot.png", dpi=300)

plt.show()