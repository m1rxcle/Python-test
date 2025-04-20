from utils import randbool
from utils import randcell
from utils import randcell2

# 🌳 🌊 🟩 🏥 🏦 ⬛
# 0 - поле
# 1 - дерево
# 2 - река
# 3 - гоститаль
# 4 - апгрейд
# 5 - огонь


CELL_TYPES = "🟩🌳🌊🏦🏥🔥"
TREE_BONUS = 100
UPGRADE_COST = 5000
LIVE_COST = 10000


class Map:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[0 for i in range(width)] for j in range(height)]

        self.generate_forest(5, 10)
        self.generate_river(10)
        self.generate_river(10)
        self.generate_shop()
        self.generate_hospital()

    def check_bounds(self, x, y):
        if x < 0 or y < 0 or x >= self.height or y >= self.width:
            return False
        return True

    def print_map(self, helico, clouds):
        print("⬛" * (self.width + 2))
        for ri in range(self.height):
            print("⬛", end="")
            for ci in range(self.width):
                cell = self.cells[ri][ci]
                if clouds.cells[ri][ci] == 1:
                    print("⚪", end="")
                elif clouds.cells[ri][ci] == 2:
                    print("⚡", end="")
                elif helico.x == ri and helico.y == ci:
                    print("🚁", end="")
                elif cell >= 0 and cell < len(CELL_TYPES):
                    print(CELL_TYPES[cell], end="")
            print("⬛")
        print("⬛" * (self.width + 2))

    def generate_river(self, l):
        rc = randcell(self.width, self.height)
        rx, ry = rc[0], rc[1]
        self.cells[rx][ry] = 2
        while l > 0:
            rc2 = randcell2(rx, ry)
            rx2, ry2 = rc2[0], rc2[1]
            if self.check_bounds(rx2, ry2):
                self.cells[rx2][ry2] = 2
                rx, ry = rx2, ry2
                l -= 1

    def generate_forest(self, r, mxr):
        for ri in range(self.height):
            for ci in range(self.width):
                if randbool(r, mxr):
                    self.cells[ri][ci] = 1

    def generate_tree(self):
        c = randcell(self.width, self.height)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] == 0:
            self.cells[cx][cy] = 1

    def generate_shop(self):
        c = randcell(self.width, self.height)
        cx, cy = c[0], c[1]
        self.cells[cx][cy] = 3

    def generate_hospital(self):
        c = randcell(self.width, self.height)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] != 3:
            self.cells[cx][cy] = 4
        else:
            self.generate_hospital()

    def add_fire(self):
        c = randcell(self.width, self.height)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] == 1:
            self.cells[cx][cy] = 5

    def update_fires(self):
        for ri in range(self.height):
            for ci in range(self.width):
                cell = self.cells[ri][ci]
                if cell == 5:
                    self.cells[ri][ci] = 0
        for i in range(10):
            self.add_fire()

    def proccess_helicopter(self, helico, clouds):
        c = self.cells[helico.x][helico.y]
        d = clouds.cells[helico.x][helico.y]
        if c == 2:
            helico.tank = helico.mxtank
        if c == 5 and helico.tank > 0:
            helico.tank -= 1
            helico.score += TREE_BONUS
            self.cells[helico.x][helico.y] = 1

        if c == 3 and helico.score >= UPGRADE_COST:
            helico.score -= UPGRADE_COST
            helico.mxtank += 1

        if c == 4 and helico.score >= LIVE_COST:
            helico.score -= LIVE_COST
            helico.live += 10

        if d == 2:
            helico.lives -= 1
            if helico.lives == 0:
                helico.game_over()

    def export_data(self):
        return {"cells": self.cells}

    def impotr_data(self, data):
        self.cells = data["cells"] or [
            [0 for i in range(self.width)] for j in range(self.height)
        ]
