import simple_draw as sd

sd.resolution = (1500, 600)


def wall():
    for y in range(25, 225, 100):
        for x in range(400, 550, 100):
            point_1 = sd.get_point(x, y)
            point_2 = sd.get_point(x, y + 50)
            sd.line(start_point=point_1, end_point=point_2, color=sd.COLOR_GREEN, width=1)
            sd.sleep(0.1)
    for y in range(25, 225, 100):
        for x in range(550, 700, 100):
            point_1 = sd.get_point(x, y)
            point_2 = sd.get_point(x, y + 50)
            sd.line(start_point=point_1, end_point=point_2, color=sd.COLOR_GREEN, width=1)
            sd.sleep(0.1)
    for y in range(75, 225, 100):
        for x in range(450, 700, 100):
            point_1 = sd.get_point(x, y)
            point_2 = sd.get_point(x, y + 50)
            sd.line(start_point=point_1, end_point=point_2, color=sd.COLOR_GREEN, width=1)
            sd.sleep(0.1)

    for x in range(400, 550, 50):
        for y in range(25, 226, 50):
            point_1 = sd.get_point(x, y)
            point_2 = sd.get_point(x + 50, y)
            sd.line(start_point=point_1, end_point=point_2, color=sd.COLOR_GREEN, width=1)
            sd.sleep(0.1)
    for x in range(650, 700, 50):
        for y in range(25, 226, 50):
            point_1 = sd.get_point(x, y)
            point_2 = sd.get_point(x + 50, y)
            sd.line(start_point=point_1, end_point=point_2, color=sd.COLOR_GREEN, width=1)
            sd.sleep(0.1)

    for y in range(225, 325, 100):
        for x in range(400, 700, 100):
            point_1 = sd.get_point(x, y)
            point_2 = sd.get_point(x, y + 50)
            sd.line(start_point=point_1, end_point=point_2, color=sd.COLOR_GREEN, width=1)
            sd.sleep(0.1)
    for y in range(275, 325, 100):
        for x in range(450, 700, 100):
            point_1 = sd.get_point(x, y)
            point_2 = sd.get_point(x, y + 50)
            sd.line(start_point=point_1, end_point=point_2, color=sd.COLOR_GREEN, width=1)
            sd.sleep(0.1)
    for x in range(400, 700, 50):
        for y in range(225, 326, 50):
            point_1 = sd.get_point(x, y)
            point_2 = sd.get_point(x + 50, y)
            sd.line(start_point=point_1, end_point=point_2, color=sd.COLOR_GREEN, width=1)
            sd.sleep(0.1)