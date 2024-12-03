from itertools import pairwise

with open("2.txt") as f:
    reports = [[int(x) for x in l.split()] for l in f.readlines()]
    # print(reports)

def is_safe(list):
    diff = set(y - x for x, y in pairwise(list))
    return (diff <= {1, 2, 3,}) or (diff <= {-1, -2, -3}) # ascending or descending diff

print(sum(is_safe(r) for r in reports))

def dampner(list):
    for i in range(len(list)):
        if is_safe(list[:i] + list[i+1:]):
            return True
    return False

print(sum(is_safe(r) or dampner(r) for r in reports))