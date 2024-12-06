'''Creates plots suitable for documents

Changes the matplotlib default settings to:
- Grid by default
- Tight layout (reduce whitespace around plots)
- Latin Modern font (as default, can be changed)
- Adjust size to match font size of document
    - Font size and text width can be adjusted
    
--- How to use ---
Simply by: 
    from plotonium import report

Adjust text width:
    report.textwidth(width, unit='pt')
        unit can be 'in', 'cm', 'pt'
        default is 'pt', because that is what LaTeX will give you 

Adjust font size
    report.fontsize(size=11)'''

#import _initialize
import matplotlib.pyplot as plt

textwidth = 236.84843 #pt
textwidth_inches = textwidth/72.27 #convert pt -> inches
aspect_ratio = 4/3

_font_size = 10

def _apply():
    global _font_size
    plt.rcParams.update({
        "figure.figsize": (textwidth_inches,textwidth_inches/aspect_ratio),
        "figure.dpi": 1000,

        #"text.usetex": True,
        #"font.family": "lmodern",
        "font.size": _font_size,

        "lines.linewidth" : .8,
        "lines.markersize" : 3,

        "axes.grid" : True,
        "grid.color": "#cccccc",
        "grid.linestyle" : "-",
        "grid.linewidth" : .5, 

        "figure.autolayout": True, # Automatically adjust subplots to fit into the figure area
        "savefig.bbox": "tight",   # Save figures with minimal whitespace})

        "savefig.bbox" : "tight",
        "savefig.pad_inches":  0.02, 
        "savefig.dpi" : 1000,
        "savefig.format" : "pdf",
    })

def textwidth(textwidth, unit='pt'):
    global textwidth_inches
    if unit == 'pt':
        textwidth_inches = textwidth/72.27 #convert pt -> inches
    elif unit == 'cm':
        textwidth_inches = textwidth*2.54
    elif unit == 'in':
        textwidth_inches = textwidth
    _apply()

def font_size(size='11'):
    global _font_size
    _font_size = size
    _apply()

_cm = 1/2.54
plt.rcParams.update({
    "axes.grid" : True,
    "figure.dpi" : 300,
    "figure.figsize" : (15*_cm,10*_cm),
    "grid.linestyle" : "--",
    "grid.linewidth" : .5 })

_apply()

