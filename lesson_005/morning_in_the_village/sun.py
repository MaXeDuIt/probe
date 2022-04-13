import simple_draw as sd

def sun(x, y):
    start_point = sd.get_point(x, y)

    sd.circle(start_point, 50, color=sd.COLOR_YELLOW, width=0)

    sd.line(sd.get_point(x, y + 50), sd.get_point(x, y + 125), color=sd.COLOR_YELLOW, width=2)
    sd.line(sd.get_point(x, y - 50), sd.get_point(x, y - 125), color=sd.COLOR_YELLOW, width=2)
    sd.line(sd.get_point(x + 50, y), sd.get_point(x + 125, y), color=sd.COLOR_YELLOW, width=2)
    sd.line(sd.get_point(x - 50, y), sd.get_point(x - 125, y), color=sd.COLOR_YELLOW, width=2)

    sd.line(sd.get_point(x + 34, y + 34), sd.get_point(x + 84, y + 94), color=sd.COLOR_YELLOW, width=2)
    sd.line(sd.get_point(x - 35, y - 35), sd.get_point(x - 85, y - 95), color=sd.COLOR_YELLOW, width=2)
    sd.line(sd.get_point(x - 35, y + 35), sd.get_point(x - 85, y + 95), color=sd.COLOR_YELLOW, width=2)
    sd.line(sd.get_point(x + 34, y - 34), sd.get_point(x + 84, y - 94), color=sd.COLOR_YELLOW, width=2)


