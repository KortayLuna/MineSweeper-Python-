from dataclasses import dataclass


@dataclass
class MineSweeper:

    dim_size: int
    def __init__(self, dim_size):
        self.dim_size = dim_size


    def print_map(self):
        grid = [[0 for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        grid_x = 0
        print(" "," | ".join(str(i) for i in range(self.dim_size)))
        
        for row in grid:
            print("  " + "-" * (self.dim_size * 4 - 1))
            print(grid_x, " | ".join(str(cell) for cell in row))
            grid_x += 1

a = MineSweeper(10)
a.print_map()





    
    
    

    
    
