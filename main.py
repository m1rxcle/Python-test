# 🌳 🔥 🟩 🌊 🏥 🧡 ⚡️ 🏆 🏦 ☁️ 🚁 🪣
from map import Map
from clouds import Clouds
import time
import os
import json
from helicopter import Helicopter as Helico
from pynput import keyboard

TICK_SLEEP = 0.05
TREE_UPDATE = 50
FIRE_UPDATE = 75
CLOUD_UPDATE = 100

MAP_W, MAP_H = 20, 10
tick = 1


field = Map(MAP_W, MAP_H)
clouds = Clouds(MAP_W, MAP_H)

helico = Helico(MAP_W, MAP_H)
MOVES = {"w": (-1, 0), "d": (0, 1), "s": (1, 0), "a": (0, -1)}
# f - save , g - load


def process_key(key):
    global helico, tick, clouds, field
    c = key.char.lower()

    # обработка движений вертолета
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helico.move(dx, dy)
    # сохранение
    elif c == "f":
        data = {
            "helicopter": helico.export_data(),
            "clouds": clouds.export_data(),
            "field": field.export_data(),
            "tick": tick,
        }
        with open("level.json", "w") as lvl:
            json.dump(data, lvl)
    # загрузка
    elif c == "g":
        with open("level.json", "r") as lvl:
            data = json.load(lvl)
            helico.import_data(data["helicopter"])
            tick = data["tick"]
            clouds.import_data(data["clouds"])
            field.import_data(data["field"])


listener = keyboard.Listener(on_press=None, on_release=process_key)
listener.start()


while True:
    os.system("cls")

    field.proccess_helicopter(helico, clouds)
    helico.print_stats()
    field.print_map(helico, clouds)
    print("tick", tick)
    tick += 1
    time.sleep(TICK_SLEEP)
    if tick % TREE_UPDATE == 0:
        field.generate_tree()
    if tick % FIRE_UPDATE == 0:
        field.update_fires()
    if tick % CLOUD_UPDATE == 0:
        clouds.update()
