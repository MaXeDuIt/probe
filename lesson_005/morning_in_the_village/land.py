import simple_draw as sd

sd.resolution = (1500, 600)


def land():
    sd.rectangle(left_bottom=sd.get_point(0, 0), right_top=sd.get_point(1500, 25),
                 color=sd.COLOR_DARK_YELLOW, width=0)


