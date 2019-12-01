from typing import List


def main():
    width = 5
    height = 5
    globe: List[List[int]] = create_globe(width=width, height=height)
    (tower, gates) = create_tower(2, 2, width)

    globe = add_pos(globe, tower, 5)

    for gate in gates:
        globe = add_pos(globe, gate, 2)

    draw_map = {0: "   ", 2: " * ", 5: "{ }"}
    pure_render(globe, draw_map)
    # render(globe=globe, tower=tower, gates=gates)
    # pure_render(globe=globe)


def create_tower(pos_x: int, pos_y: int, globe_size: int):
    # return [ [ if_tower(pos_x, pos_y, x, y)  for y in range(globe_size) ] for x in range(globe_size) ]
    return (pos_x, pos_y), [(pos_x - x, pos_y - y) for x in range(-1, 2) for y in range(-1, 2)]


def add_pos(globe, pos, type):
    (x, y) = pos
    at_pos = globe[x][y]

    if at_pos < type:
        globe[x][y] = type

    return globe


def if_tower(pos_x, pos_y, x, y):
    if pos_x == x and pos_y == y:
        return 1
    else:
        return 0


def create_globe(width, height):
    return [[0 for _ in range(width)] for _ in range(height)]


def render(globe, tower, gates):
    number_of_rows = len(globe)
    for x in range(number_of_rows):
        number_of_columns = len(globe[x])
        for y in range(number_of_columns):
            element_row = globe[x]
            element = element_row[y]
            position = (x, y)

            if position in gates:
                element = "*"

            if tower[0] == x and tower[1] == y:
                element = 1

            print(str(element) + ' ', end='')
        print()
    print()


def pure_render(globe, draw_map):
    number_of_rows = len(globe)
    for x in range(number_of_rows):
        number_of_columns = len(globe[x])
        for y in range(number_of_columns):
            element_row = globe[x]
            element = element_row[y]
            print(draw_map[element] + ' ', end='')
        print()
    print()


if __name__ == '__main__':
    main()

# 0 0 0 0 0
# 0 * * * 0
# 0 * 1 * 0
# 0 * * * 0
# 0 0 0 0 0

# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0

# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 0 0

# 0 0 0 0 0
# 0 * * * 0
# 0 * * * 0
# 0 * * * 0
# 0 0 0 0 0
