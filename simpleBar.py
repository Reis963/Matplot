import matplotlib.pyplot as plt
import numpy as np

from matplotlib import lines
from matplotlib import patches

plt.style.use('_mpl-gallery-nogrid')

# The colors
BLUE = "#076fa2"
RED = "#E3120B"
BLACK = "#202020"
GREY = "#a2a2a2"

# data
sizes = [148, 179, 208, 295, 424, 500, 605, 738, 1010, 1155, 1326, 1467, 1620]
names = ["1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010"]
#bar_labels = ['red', 'blue', '_red', 'orange']
#bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']
colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(sizes)))

# plot
fig, ax = plt.subplots()
ax.bar(names, sizes, color=colors)
#ax.bar(names, sizes, label=bar_labels, color=colors)


ax.set_ylabel('CAPS')
#ax.set_title('Fruit supply by kind and color')
#ax.legend(title='Fruit color')

# Add title
fig.text(
    0, 0.925, "PIASC MED",
    fontsize=22, fontweight="bold", fontfamily="DejaVu Sans"
)
# Add subtitle
fig.text(
    0, 0.875, "Série histórica da espansão dos CAPS (1988 a 2010)",
    fontsize=20, fontfamily="DejaVu Sans"
)
#fig.text(
#    0.005, 0.835, "Utilização de Preservativo",
#    fontsize=15, fontfamily="DejaVu Sans"
#)

# Add caption
source = "Fonte: Coordenação de Saúde Mental, Álcool e Outras Drogas/DAPES/SAS/MS. Antes de 2001: Levantamento CAPS Disque-Saúde 2001."
fig.text(
    0, 0.04, source, color=GREY,
    fontsize=14, fontfamily="DejaVu Sans"
)

# Add authorship
fig.text(
    0, 0.005, "Diego Reis", color=GREY,
    fontsize=16, fontfamily="DejaVu Sans"
)

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