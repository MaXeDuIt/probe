import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

def rainbow(point, step):
    radius = 900
    for _ in range(7):
        radius += step
        sd.circle(center_position=point, radius=radius, color=rainbow_colors[_], width=20)



