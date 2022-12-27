def island_count(grid):
    visited = set()
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (explore(grid, r, c, visited) == True):
                count += 1

    return count

def explore(grid, r, c, visited):
    # print(f"visited {visited}")
    rowInBounds, colInBounds = False, False
    if 0 <= r and r < len(grid): rowInBounds = True
    if 0 <= c and c < len(grid[0]): colInBounds = True

    if (not rowInBounds or not colInBounds): return False

    if grid[r][c] == 'W': return False # if it is water return False, because we need only land 'L'

    pos = str(r) + "," + str(c)
    if pos in visited: return False
    visited.add(pos)

    explore(grid, r-1, c, visited) # up
    explore(grid, r+1, c, visited) # down
    explore(grid, r, c-1, visited) # left
    explore(grid, r, c+1, visited) # right

    return True

grid = [['W', 'L', 'W', 'W', 'W'],
        ['W', 'L', 'W', 'L', 'W'],
        ['W', 'W', 'L', 'L', 'W'],
        ['L', 'W', 'W', 'L', 'L'],
        ['L', 'L', 'W', 'W', 'W']]

count = island_count(grid)
print(f"island_count {count}")