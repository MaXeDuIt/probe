import simple_draw as sd

coordinates = {}
colors = {'1': sd.COLOR_RED, '2': sd.COLOR_ORANGE, '3': sd.COLOR_YELLOW, '4': sd.COLOR_GREEN,
               '5': sd.COLOR_CYAN, '6': sd.COLOR_BLUE, '7': sd.COLOR_PURPLE}

def create_snowfall(N):
    global coordinates
    for i in range(N):
        coordinates[i] = {}
        coordinates[i]['x'] = sd.random_number(0, 600)
        coordinates[i]['y'] = 500
        coordinates[i]['length'] = sd.random_number(3, 15)
        coordinates[i]['f_a'] = sd.random_number(1, 8) / 10
        coordinates[i]['f_b'] = sd.random_number(1, 7) / 10
        coordinates[i]['f_c'] = sd.random_number(35, 65)


def draw_snowfall(color):
    for i in range(len(coordinates)):
        sd.start_drawing()
        point = sd.get_point(coordinates[i]['x'], coordinates[i]['y'])
        sd.snowflake(center=point, length=coordinates[i]['length'], color=color, factor_a=coordinates[i]['f_a'],
                     factor_b=coordinates[i]['f_b'], factor_c=coordinates[i]['f_c'])
        sd.finish_drawing()


def move_snowfall():
    global coordinates
    for i in range(len(coordinates)):
        coordinates[i]['x'] += sd.random_number(-15, 15)
        coordinates[i]['y'] -= sd.random_number(3, 17)
        coordinates[i].update({'x': coordinates[i]['x'], 'y': coordinates[i]['y']})



def number_of_snowfall():
    pass




def delete_snowfall(numbers):
    pass


