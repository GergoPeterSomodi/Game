

def main():
    width = 5
    height = 5
    globe = create_globe(width=width, height=height)
    tower = (2, 2)
    gates = (tower[0]-1, tower[1])
    render(globe=globe, tower=tower, gates=gates)

def create_globe(width, height):
    return [[0 for i in range(width)] for x in range(height)]









def render(globe, tower, gates):
    number_of_rows = len(globe)
    for x in range(number_of_rows):
        number_of_columns = len(globe[x])
        for y in range(number_of_columns):
            element_row = globe[x]
            element = element_row[y]

            if tower[0] == x and tower[1] == y:
                element = 1
            if gates[0] == x and gates[1] == y:
                element = "*"

            print(str(element) + ' ', end='')
        print()


if __name__ == '__main__':
    main()
