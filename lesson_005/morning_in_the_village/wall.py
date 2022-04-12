import simple_draw as sd

sd.resolution = (1500, 600)


def wall():
    for y in range(25, 225, 100):
        for x in range(400, 550, 100):
            point_1 = sd.get_point(x, y)
            point_2 = sd.get_point(x, y + 50)
            sd.line(start_point=point_1, end_point=point_2, color=sd.COLOR_GREEN, width=1)

    # for y in range(50, 700, 100):
    #     for x in range(50, 700, 100):
    #         point_1 = sd.get_point(x, y)
    #         point_2 = sd.get_point(x, y + 50)
    #         sd.line(start_point=point_1, end_point=point_2, color=sd.COLOR_GREEN, width=1)
    #
    # for x in range(0, 700, 100):
    #     for y in range(0, 700, 50):
    #         point_1 = sd.get_point(x, y)
    #         point_2 = sd.get_point(x + 100, y)
    #         sd.line(start_point=point_1, end_point=point_2, color=sd.COLOR_GREEN, width=1)

