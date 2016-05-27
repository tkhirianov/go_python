from collections import namedtuple

__author__ = 'Тимофей Фёдорович Хирьянов и Дмитрий Пестов'
# license: GPLv3

Vector2d = namedtuple('Vector2d', ['x', 'y'])


class Snake:
    """ змейка -- это класс, содержащий список частей тела с их координатами и аватарками. """
    def __init__(self, head_x, head_y, tail_x, tail_y):
        """ змейка создаётся либо строго горизонтальной, либо строго вертикальной, длина не менее 2 """
        if head_x == tail_x:  # змейка вертикальная
            self.direction = Vector2d(0, -1 if head_y < tail_y else 1)
            self.length = abs(head_y - tail_y) + 1
        elif head_y == tail_y:  # змейка горизонтальная
            self.direction = Vector2d(-1 if head_x < tail_x else 1, 0)
            self.length = abs(head_x - tail_x) + 1
        else:
            raise AssertionError()

        self.body = []  # список координат частей тела
        for i in range(self.length):
            body_part = Vector2d(head_x - self.direction.x*i, head_y - self.direction.y*i)
            self.body.append(body_part)

    def go(self):
        """ функция, которая пердиодически вызывается и двигает змейку, т.е. все части тела """
        # FIXME
        pass

# сами бонусы, корм и стены -- это строки из некоторого набора
objects = {'#': 'wall', '.': 'food', 'b': 'bonus', 'h': 'head', 't': 'tail'}


class Field:
    """ поле -- это класс, содержащий стены в некоторых клетках, а также бонусы и корм."""

    def __init__(self, filename):
        """ Поле считывается из файла """
        # FIXME
        pass
    
    def tick(self):
        #FIXME:
        pass


def game_cycle():
    """ игровой цикл -- функция, которая перезапускается и запускает обработку змейкой своего положения,
        генерацию бонусов на поле (метод поля),
        а также проверяет, не наступил ли game over
    """
    # FIXME
    field.tick()
    snake.go()
    pass

if __name__ == "__main__":
    # FIXME инициализировать всё: поле, змейку и т.д.
    game_cycle()

