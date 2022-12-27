def minimum_island(grid):
    visited = set()
    min_count = len(grid) * len(grid[0])
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            count = explore(grid, r, c, visited)
            if count != 0:
                # print(f"island count {count}")
                min_count = min(min_count, count)

    return min_count

def explore(grid, r, c, visited):
    # print(f"visited {visited}")
    rowInBounds, colInBounds = False, False
    if 0 <= r and r < len(grid): rowInBounds = True
    if 0 <= c and c < len(grid[0]): colInBounds = True

    if (not rowInBounds or not colInBounds): return 0

    if grid[r][c] == 'W': return 0 # if it is water return False, because we need only land 'L'

    pos = str(r) + "," + str(c)
    if pos in visited: return 0
    visited.add(pos)

    count = 1

    count += explore(grid, r-1, c, visited) # up
    count += explore(grid, r+1, c, visited) # down
    count += explore(grid, r, c-1, visited) # left
    count += explore(grid, r, c+1, visited) # right

    return count

grid = [['W', 'L', 'W', 'W', 'W'],
        ['W', 'L', 'W', 'L', 'W'],
        ['W', 'W', 'L', 'L', 'W'],
        ['L', 'W', 'W', 'L', 'L'],
        ['L', 'L', 'W', 'W', 'W']]

count = minimum_island(grid)
print(f"minimum_island {count}")