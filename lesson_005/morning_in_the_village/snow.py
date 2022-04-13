import simple_draw as sd

def snow(N):
    coordinates = {}
    for i in range(N):
        coordinates[i] = {}
        coordinates[i]['x'] = sd.random_number(0, 325)
        coordinates[i]['y'] = 315
        coordinates[i]['length'] = sd.random_number(3, 10)
        coordinates[i]['f_a'] = sd.random_number(1, 8)/10
        coordinates[i]['f_b'] = sd.random_number(1, 7)/10
        coordinates[i]['f_c'] = sd.random_number(35, 65)
        coordinates[i]['wind'] = sd.random_number(3, 7)
    while True:
        sd.start_drawing()
        for i, coordinates_item in coordinates.items():
            point = sd.get_point(coordinates_item['x'], coordinates_item['y'])
            sd.snowflake(center=point, length=coordinates_item['length'], color=sd.background_color,
                         factor_a=coordinates_item['f_a'], factor_b=coordinates_item['f_b'],
                         factor_c=coordinates_item['f_c'])
            coordinates_item['y'] -= coordinates_item['wind']
            coordinates_item['x'] += sd.random_number(-3, 3)
            point = sd.get_point(coordinates_item['x'], coordinates_item['y'])
            sd.snowflake(center=point, length=coordinates_item['length'], color=sd.COLOR_WHITE,
                         factor_a=coordinates_item['f_a'], factor_b=coordinates_item['f_b'],
                         factor_c=coordinates_item['f_c'])
            if coordinates_item['y'] < 35:
                sd.snowflake(center=point, length=coordinates_item['length'], color=sd.COLOR_WHITE,
                             factor_a=coordinates_item['f_a'], factor_b=coordinates_item['f_b'],
                             factor_c=coordinates_item['f_c'])
                coordinates_item['y'] = 315
        sd.finish_drawing()
        sd.sleep(0.1)
        if sd.user_want_exit():
            break