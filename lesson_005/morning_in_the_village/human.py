import simple_draw as sd

def human(x, y):
    start_point = sd.get_point(x, y)

    sd.circle(start_point, 25, color=sd.COLOR_CYAN)
    sd.sleep(0.1)

    sd.circle(sd.get_point(x + 10, y + 10), 3, color=sd.COLOR_CYAN)
    sd.sleep(0.1)

    sd.circle(sd.get_point(x - 10, y + 10), 3, color=sd.COLOR_CYAN)
    sd.sleep(0.1)

    sd.line(sd.get_point(x, y + 3), sd.get_point(x, y - 3), color=sd.COLOR_CYAN)
    sd.sleep(0.1)

    sd.line(sd.get_point(x, y + 30), sd.get_point(x, y + 50), color=sd.COLOR_CYAN)
    sd.sleep(0.1)

    sd.line(sd.get_point(x - 15, y + 30), sd.get_point(x - 25, y + 50), color=sd.COLOR_CYAN)
    sd.sleep(0.1)

    sd.line(sd.get_point(x + 15, y + 30), sd.get_point(x + 25, y + 50), color=sd.COLOR_CYAN)
    sd.sleep(0.1)

    sd.line(sd.get_point(x - 5, y - 10), sd.get_point(x + 5, y - 10), color=sd.COLOR_CYAN)
    sd.sleep(0.1)

    sd.line(sd.get_point(x - 5, y - 10), sd.get_point(x - 10, y - 7), color=sd.COLOR_CYAN)
    sd.sleep(0.1)

    sd.line(sd.get_point(x + 5, y - 10), sd.get_point(x + 10, y - 7), color=sd.COLOR_CYAN)
    sd.sleep(0.1)

    sd.line(sd.get_point(x, y - 25), sd.get_point(x, y - 75), color=sd.COLOR_CYAN)
    sd.sleep(0.1)

    sd.line(sd.get_point(x, y - 50), sd.get_point(x + 25, y - 35), color=sd.COLOR_CYAN)
    sd.sleep(0.1)

    sd.line(sd.get_point(x, y - 50), sd.get_point(x - 25, y - 35), color=sd.COLOR_CYAN)
    sd.sleep(0.1)

    sd.line(sd.get_point(x, y - 75), sd.get_point(x + 15, y - 100), color=sd.COLOR_CYAN)
    sd.sleep(0.1)

    sd.line(sd.get_point(x, y - 75), sd.get_point(x - 15, y - 100), color=sd.COLOR_CYAN)
    sd.sleep(0.1)