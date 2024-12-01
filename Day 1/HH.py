from collections import Counter

# PART ONE FUNC
def calculate_total_distance(left_list, right_list):
    left_list.sort()
    right_list.sort()

    total_distance = 0
    for left, right in zip(left_list, right_list):
        total_distance += abs(left - right)
    
    return total_distance

#PART TWO FUNC
def calculate_similarity(left_list, right_list):
    right_count = Counter(right_list)

    similarity = 0
    for num in left_list:
        similarity += num * right_count[num]

    return similarity

left_list = []
right_list = []

with open("1.txt", "r") as file:
    words = file.read().splitlines()

for word in words:
    left, right = word.split("  ")
    left_list.append(int(left))
    right_list.append(int(right))

total_distance = calculate_total_distance(left_list, right_list)
print("Solution 1 =", total_distance)

similarity = calculate_similarity(left_list, right_list)
print("Solution 2 =", similarity)

