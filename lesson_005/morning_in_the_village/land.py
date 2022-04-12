import simple_draw as sd

sd.resolution = (1500, 600)

def land(point_left, point_right):
    sd.rectangle(left_bottom=point_left, right_top=point_right, color=sd.COLOR_DARK_YELLOW, width=0)

land(sd.get_point(0, 0), sd.get_point(1500, 25))










sd.pause()