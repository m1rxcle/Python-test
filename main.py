"""# Задание № 1


class Kassa:
    def __init__(self, amount):
        self.amount = amount

    def top_up(self, x):
        self.amount += x
        return self.amount

    def count_1000(self):
        return self.amount // 1000

    def take_away(self, x):
        if x > self.amount:
            return "Недостаточно средств"
        else:
            self.amount -= x
            return self.amount


kassa = Kassa(10000)

print(kassa.top_up(1000))
print(kassa.count_1000())
print(kassa.take_away(1000))"""

# Задание № 2


class Turtle:
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s
        return self.y

    def go_down(self):
        self.y -= self.s
        return self.y

    def go_right(self):
        self.x += self.s
        return self.x

    def go_left(self):
        self.x -= self.s
        return self.x

    def evolve(self):
        self.s += 1
        return self.s

    def degrade(self):
        if self.s > 1:
            self.s -= 1
            return self.s
        raise Exception("Дальше двигаться нельзя.")

    def count_moves(self, x2, y2):
        return abs(x2 - self.x) // self.s + abs(y2 - self.y) // self.s


turtle = Turtle(0, 0, 1)
print(turtle.go_up())
print(turtle.go_right())
print(turtle.go_down())
print(turtle.go_left())
print(turtle.evolve())
print(turtle.degrade())
print(turtle.count_moves(2, 2))
