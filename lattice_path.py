def count_lattice_paths(n, m):
    # define n x m 2d array
    grid = [[0 for i in range(m)] for j in range(n)]
    grid[0][0] = 1
    
    for i in range(n):
        for j in range(m):
            if i > 0:
                grid[i][j] += grid[i - 1][j]
            if j > 0:
                grid[i][j] += grid[i][j - 1]
                
    return grid[n-1][m-1]

if __name__ == '__main__':
    print(count_lattice_paths(21, 21))
