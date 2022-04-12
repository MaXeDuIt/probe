import simple_draw as sd

def base(point, side):
    sd.square(left_bottom=point, side=side, color=sd.COLOR_DARK_YELLOW, width=1)

def door(point_left, point_right):
    sd.rectangle(left_bottom=point_left, right_top=point_right, color=sd.COLOR_ORANGE, width=1)

def roof(point):
    v1 = sd.get_vector(start_point=point, angle=0, length=200, width=2)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=135, length=150, width=2)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=225, length=150, width=2)
    v3.draw()

def pipe(x, y):
    start_point = sd.get_point(x, y)
    end_point = sd.get_point(x, y+50)
    sd.line(start_point=start_point, end_point=end_point, width=1)
    start_point = end_point
    end_point = sd.get_point(x+50, y+50)
    sd.line(start_point=start_point, end_point=end_point, width=1)
    start_point = sd.get_point(x+50, y+50)
    end_point = sd.get_point(x+50, y-100)
    sd.line(start_point=start_point, end_point=end_point, width=1)

def window(point, radius):
    sd.circle(center_position=point, radius=radius, width=2)

def grid(x, y):
    start_point = sd.get_point(x, y)
    end_point = sd.get_point(x+100, y)
    sd.line(start_point=start_point, end_point=end_point, width=1)
    start_point = sd.get_point(x+50, y+50)
    end_point = sd.get_point(x+50, y-50)
    sd.line(start_point=start_point, end_point=end_point, width=1)

base(sd.get_point(250, 250), 300)
door(sd.get_point(100, 100), sd.get_point(200, 200))
roof(sd.get_point(200, 300))
window(sd.get_point(300, 300), 50)
pipe(150, 500)
grid(450, 500)



sd.pause()