import operator
from pathlib import Path

def read(file: str | Path) -> None:
    with open(file, "rt") as infile:
        out: list[tuple[int, list[int]]] = []
        for line in infile:
            val, l = line.strip().split(":")
            val = int(val)
            out.append((int(val), list(map(int, l.split()))))
    return out

def is_valid(val: int, nums: list[int]) -> bool:
    if len(nums) == 1:
        return val == nums[0]
    if val % nums[-1] == 0 and is_valid(val // nums[-1], nums[:-1]):
        return True
    if val % nums[-1] >= 0 and is_valid(val - nums[-1], nums[:-1]):
        return True
    return False

def valid_second(val: int, nums: list[int]) -> bool:
    if len(nums) == 1:
        return val == nums[0]
    if val % nums[-1] == 0 and valid_second(val // nums[-1], nums[:-1]):
        return True
    if val % nums[-1] >= 0 and valid_second(val - nums[-1], nums[:-1]):
        return True
    
    str_num = str(nums[-1])
    str_val = str(val)
    if len(str_val) > len(str_num) and str_val[-len(str_num) :] == str_num:
        str_val = str_val[: -len(str_num)]
        return valid_second(int(str_val), nums[:-1])
    return False

def result(file: str | Path) -> int | str:
    data = read(file)
    total = 0
    for val, nums in data:
        if is_valid(val, nums):
            total += val
    return total

def result2(file:str | Path) -> int | str:
    data = read(file)
    total = 0
    for val, nums in data:
        if valid_second(val, nums):
            total += val
    return total

print(result("7.txt")) # FIRST RESULT
print(result2("7.txt")) # SECOND RESULT