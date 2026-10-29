def formingMagicSquare(s):
    n = len(s)
    magic_number = int((n * ((n**2) + 1)) * 0.5)

    original_magic_square = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    possible_magic_squares = []

    rotated_90 = rotate_90(original_magic_square)
    rotated_180 = rotate_90(rotated_90)
    rotated_270 = rotate_90(rotated_180)
    horizontally_reflected = horizontal_reflection(original_magic_square)
    vertically_reflected = vertical_reflection(original_magic_square)
    main_diagonal_reflected = main_diagonal_reflection(original_magic_square)
    # anti_diagonal_reflected = anti_diagonal_reflection(original_magic_square)

    print(
        "original_magic_square",
        original_magic_square,
    )

    possible_magic_squares.append(rotated_90)
    possible_magic_squares.append(rotated_180)
    possible_magic_squares.append(rotated_270)
    possible_magic_squares.append(horizontally_reflected)
    possible_magic_squares.append(vertically_reflected)
    possible_magic_squares.append(main_diagonal_reflected)
    # possible_magic_squares.append(anti_diagonal_reflected)
    # print("possible_magic_squares", possible_magic_squares)


def horizontal_reflection(grid):
    reflected_grid = []
    for row in grid[::-1]:
        reflected_grid.append(row)
    return reflected_grid


def vertical_reflection(grid):
    reflected_grid = deepcopy(grid)
    j = -1
    k = 0
    for i in range(len(reflected_grid)):
        row = reflected_grid[i]
        row[k], row[j] = row[j], row[k]
    return reflected_grid


def main_diagonal_reflection(grid):
    reflected_grid = deepcopy(grid)
    i = 0
    j = 0
    k = 0
    while k < (len(reflected_grid) * 2):
        if j >= len(reflected_grid):
            i += 1
            j = 0
        if i != j and j > i:
            print("i,j", i, j)
            reflected_grid[i][j], reflected_grid[j][i] = (
                reflected_grid[j][i],
                reflected_grid[i][j],
            )

        j += 1
        k += 1
    print("reflected_grid", reflected_grid)
    return reflected_grid


def anti_diagonal_reflection():
    pass


def rotate_90(grid):
    reverse_grid = grid[::-1]
    rotated_grid = []
    k = 0
    i = 0
    j = 0
    row = []

    while k < (len(reverse_grid) ** 2):
        row.append(reverse_grid[i][j])
        i += 1
        if i >= len(grid):
            rotated_grid.append(row)
            row = []
            i = 0
            j += 1
        k += 1
    return rotated_grid
