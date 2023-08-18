from random import randint


class MineSweeper:
    dim_size: int

    def __init__(self, dim_size: int):
        self.dim_size = dim_size
        self.grid = [[0 for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        self.add_mines()

    def add_mines(self):
        previous_Values = []
        for _ in range(30):
            row = randint(0, self.dim_size - 1)
            col = randint(0, self.dim_size - 1)
            new_values = [row, col]
            if not new_values == previous_Values:
                self.grid[row][col] = 1

            previous_Values = new_values

        self.print_map()

    def reveal(self, user_input: tuple[int, int]):
        x, y = user_input
        self.grid[x][y] = 2
        self.print_map()

    def print_map(self):
        print(" ", " | ".join(str(i) for i in range(self.dim_size)))
        for row_idx, row in enumerate(self.grid):
            print("  " + "-" * (self.dim_size * 4 - 1))
            print(row_idx, " | ".join(str(cell) for cell in row))


def fixInput(x: str, y: str):
    try:
        x_int = int(x)
        y_int = int(y)

        return x_int, y_int

    except ValueError:
        print("Invalid input. Please enter valid integer values.")
        return


def run():
    a = MineSweeper(10)
    while True:
        x_str = input("x: ")
        y_str = input("y: ")
        input_result = fixInput(x_str, y_str)

        if input_result is not None:
            x_int, y_int = input_result
            a.reveal((x_int, y_int))


if __name__ == "__main__":
    run()
