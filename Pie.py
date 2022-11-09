import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Data

labels = 'Sim', 'Não', 'Às vezes'
fracs = [45.6, 45.6, 8.9]

explode = 0.03, 0.01, 0.04

patches, texts, autotexts = plt.pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, radius=0.7)

# Make the labels on the small plot easier to read.
for t in texts:
    t.set_size('smaller')
for t in autotexts:
    t.set_size('x-small')
autotexts[0].set_color('y')

plt.show()
