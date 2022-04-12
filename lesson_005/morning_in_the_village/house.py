import simple_draw as sd

sd.resolution = (1500, 600)

def base(point, side):
    sd.square(left_bottom=point, side=side, color=sd.COLOR_DARK_YELLOW, width=2)

def roof(point):
    v1 = sd.get_vector(start_point=point, angle=0, length=400, width=2)
    v1.draw(color=sd.COLOR_DARK_YELLOW)
    v2 = sd.get_vector(start_point=v1.start_point, angle=45, length=282, width=2)
    v2.draw(color=sd.COLOR_DARK_YELLOW)
    v3 = sd.get_vector(start_point=v1.end_point, angle=135, length=282, width=2)
    v3.draw(color=sd.COLOR_DARK_YELLOW)

def door(point_left, point_right):
    sd.rectangle(left_bottom=point_left, right_top=point_right, color=sd.COLOR_DARK_ORANGE, width=0)

def pipe(x, y):
    start_point = sd.get_point(x, y)
    end_point = sd.get_point(x, y+50)
    sd.line(start_point=start_point, end_point=end_point, color=sd.COLOR_DARK_ORANGE, width=1)
    start_point = end_point
    end_point = sd.get_point(x+50, y+50)
    sd.line(start_point=start_point, end_point=end_point, color=sd.COLOR_DARK_ORANGE, width=1)
    start_point = sd.get_point(x+50, y+50)
    end_point = sd.get_point(x+50, y-50)
    sd.line(start_point=start_point, end_point=end_point, color=sd.COLOR_DARK_ORANGE, width=1)

def window(point, radius):
    sd.circle(center_position=point, radius=radius, color=sd.COLOR_YELLOW, width=0)

def grid(x, y):
    start_point = sd.get_point(x, y)
    end_point = sd.get_point(x+100, y)
    sd.line(start_point=start_point, end_point=end_point, color=sd.COLOR_BLACK, width=1)
    start_point = sd.get_point(x+50, y+50)
    end_point = sd.get_point(x+50, y-50)
    sd.line(start_point=start_point, end_point=end_point, color=sd.COLOR_BLACK, width=1)

def house():
    base(sd.get_point(400, 25), 300)
    roof(sd.get_point(350, 325))
    door(sd.get_point(550, 25), sd.get_point(650, 225))
    window(sd.get_point(625, 125), 7)
    pipe(650, 425)
    window(sd.get_point(550, 400), 50)
    grid(500, 400)

house()

sd.pause()