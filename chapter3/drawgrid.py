'Draw grid given the rows and columns'

def draw_border(columns):
    'Draws the top border'
    for i in range(columns):
        print('+ - - - - ', end='')
    print('+')

def draw_row(columns):
    for i in range(columns):
        print('|' + ' ' * 9, end='')
    print('|')

def draw_lines(columns):
    'Draws the squares given the columns'
    for i in range(4):
        draw_row(columns)

def draw_grid(rows, columns):
    'Draws the grid given the rows and columns'
    if (rows <= 0)  or (columns <= 0):
        return
    for i in range(rows):
        draw_border(columns)
        draw_lines(columns)
    draw_border(columns)


if (__name__ == '__main__'):
    draw_grid(2, 2)
    draw_grid(5, 4)
