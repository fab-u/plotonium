import matplotlib.pyplot as plt

def theme(palette):
    """This function can be used to change the color palette of plots
        
    takes: palette (dict) colors in the form:
                my_palette = {
                    "background" : "white",
                    "background_accent" : "#aaffee",
                    "content" : "black" }"""
    global _current_theme 
    _current_theme = palette
                
    plt.rcParams.update({
        "lines.color": palette["content"],
        "patch.edgecolor": palette["content"],
        "text.color": palette["content"],
        "axes.facecolor": palette["background"],
        "axes.edgecolor": palette["content"],
        "axes.labelcolor": palette["content"],
        "xtick.color": palette["content"],
        "ytick.color": palette["content"],
        "grid.color": palette["background_accent"],
        "figure.facecolor": palette["background"],
        "figure.edgecolor": palette["background"],
        "savefig.facecolor": palette["content"],
        "savefig.edgecolor": palette["content"], 
        "savefig.facecolor": palette["background"],  # Adjust savefig settings
        "savefig.edgecolor": palette["background"],   # Adjust savefig settings})
    })
def colors(colors):
    """colors(colors)
    change default color cycle for line colors

    takes:  
        colors (list of strings)
            colots in the format:
            ["#4deeea", "blue", "#ffe700", "#f000ff", "#001eff"]"""
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=colors) 
