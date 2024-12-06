from .plotonium import dark, report, animate

import matplotlib.pyplot as plt

_cm = 1/2.54
plt.rcParams.update({
    "axes.grid" : True,
    "figure.dpi" : 120,
    "figure.figsize" : (15*_cm,10*_cm),
    "grid.linestyle" : "-",
    "grid.linewidth" : .3,
    #"xtick.bottom" : False,
    #"ytick.left" : False,
    #"xtick.major.pad" : 0,     
    #"xtick.minor.pad" : 0,
    #"ytick.major.pad" : 0,     
    #"ytick.minor.pad" : 0,
    "figure.autolayout": True, # Automatically adjust subplots to fit into the figure area
    "savefig.bbox": "tight"   # Save figures with minimal whitespace})
})