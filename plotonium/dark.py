from .utility import theme, colors

import matplotlib.pyplot as plt

theme_dark = {
    "background" : "#292c33",
    "background_accent" : "#666677",
    "content" : "#eeeeee"
}

colors_neon = ["#00aaff", "#ffaa00", "#00dd33", "#aa00ff", "#ff00aa", "#aaff00"]

theme(theme_dark)
colors(colors_neon)
