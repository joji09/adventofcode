
def read_file_str(filename, strip=False):
    string_list = []
    with open(filename, "r") as f:
        for line in f:
            l = line
            if strip:
                l = line.strip()
                string_list.append(l)
    return string_list

def in_grid(point, grid):
    return 0 <= point[0] < len(grid[0]) and 0 <= point[1] <len(grid)

direction = [
    (0,1),
    (0,-1),
    (1,0),
    (-1,0),
    (1,1),
    (1,-1),
    (-1,1),
    (-1, -1),
]


def find_xmas(content): # PART 1
    result = 0
    find = "XMAS"

    for r, row in enumerate(content):
        for c, curr_val in enumerate(row):
            for p in direction:
                found = True
                current_position = (r,c)
                for letter in find:
                    if not in_grid(current_position, content) or content[current_position[0]][current_position[1]] != letter:
                        found = False
                        break
                    current_position = (current_position[0] + p[0], current_position[1] + p[1])
                if found:
                    result += 1
    return result

def find_mas(content):  #PART 2
    result = 0
    find = "MS"

    def is_diagonal(char1, char2):
        return char1 in find and char2 in find and char1 != char2
    
    for r, row in enumerate(content):
        for c, curr_val in enumerate(row):
            if row[c] == "A":
                corners = [(r-1, c-1), (r-1, c+1), (r+1, c-1), (r+1, c+1)]

                if all(in_grid(position, content) for position in corners):
                    corner_letter = [content[i][e] for i, e in corners]
                    if is_diagonal(corner_letter[0], corner_letter[3]) and is_diagonal(corner_letter[1], corner_letter[2]):
                        result += 1
    
    return result

        

def main():
    content = read_file_str("4.txt", True)
    print(find_xmas(content))
    print(find_mas(content))

if __name__ == '__main__':
    main()