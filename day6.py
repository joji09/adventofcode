with open("6.txt") as f:
    lines = [line.rstrip() for line in f]

obstruction_set = set()
visited = set()
x_bound = 0
y_bound = 0
start_x, start_y = None, None
directions = [(0,-1), (1,0), (0,1), (-1,0)]
direction_index = 0
obstruction = 0

for y, line in enumerate(lines):
    if not x_bound:
        x_bound = len(line)
    for x, this_char in enumerate(line):
        if this_char == '#':
            obstruction_set.add((x,y))
        elif this_char == '^':
            start_x, start_y = x,y
    y_bound += 1

curr_x, curr_y = start_x, start_y

while curr_x in range(0, x_bound) and curr_y in range(0, y_bound):
    dx, dy = directions[direction_index]
    visited.add((curr_x, curr_y))

    if(curr_x + dx, curr_y + dy) in obstruction_set:
        direction_index = (direction_index + 1) % 4
    else:
        curr_x += dx
        curr_y += dy

print(f"result: {len(visited)}")

for potential_obs in visited:
    temp_obstruction = obstruction_set.union({potential_obs})

    curr_x, curr_y = start_x, start_y
    direction_index = 0

    temp_visited = set()

    while curr_x in range(0, x_bound) and curr_y in range(0, y_bound):
        dx, dy = directions[direction_index]

        if(curr_x + dx, curr_y + dy) in temp_obstruction:
            if(curr_x, curr_y, dx, dy) in temp_visited:
                obstruction += 1
                break
            temp_visited.add((curr_x, curr_y, dx, dy))
            direction_index = (direction_index + 1) % 4
        else:
            curr_x += dx
            curr_y += dy

print(f"obstruction result: {obstruction}")

