#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точносттю до долей минут

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]
# распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ минут
# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)

halo = violator_songs_list[3][1] * 60
enj_sil = violator_songs_list[-4][1] * 60
clean = violator_songs_list[-1][1] * 60
print("Три песни ('Halo', 'Enjoy the Silence', 'Clean') звучат", halo + enj_sil + clean, 'минут')

# Есть словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
#   А другие три песни звучат ХХХ минут

sweet = violator_songs_dict['Sweetest Perfection'] * 60
policy = violator_songs_dict['Policy of Truth'] * 60
blue = violator_songs_dict['Blue Dress'] * 60
print("Три песни ('Sweetest Perfection', 'Policy of Truth', 'Blue Dress') звучат",
      round((sweet + policy + blue), 1), 'минут')

world = violator_songs_dict['World in My Eyes'] * 60
jesus = violator_songs_dict['Personal Jesus'] * 60
waiting = violator_songs_dict['Waiting for the Night'] * 60
print("А другие три песни ('World in My Eyes', 'Personal Jesus', 'Waiting for the Night') звучат",
      round((world + jesus + waiting), 1), 'минут')