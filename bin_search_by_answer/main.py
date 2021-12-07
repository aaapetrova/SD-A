import os


def check(array, len, k):
    max_last_point = array[0] + len
    interval_count = 1
    for point in array:
        if point <= max_last_point:
            continue
        else:
            interval_count += 1
            if interval_count > k:
                return False
            max_last_point = point + len
    return True


def binary_search_by_answer(array, k):
    min_length = array[-1]-array[0]
    results = range(0, min_length)
    left = 0
    right = len(results) - 1
    while right - left > 1:
        mid = (left + right) // 2
        if check(array, results[mid], k):
            min_length = results[mid]
            right = mid
        else:
            left = mid
    return min_length

real_res = {}
my_res = {}
for path in sorted(os.listdir("./")):
    if ".in" not in path and ".out" not in path:
        continue
    print(path)

    number = int(path.split(".")[0])
    line_count = 0
    if "out" in path:
        with open(path, "r") as file:
            for line in file:
                real_res[number] = int(line)
    else:
        with open(path, "r") as file:
            array = []
            for line in file:
                if line_count == 0:
                    N = int(line)
                elif line_count == 1:
                    K = int(line)
                else:
                    array.append(int(line))
                line_count += 1
            my_res[number] = binary_search_by_answer(array, K)


for key in real_res.keys():
    try:
        assert real_res[key] == my_res[key]
        print(f"Key:{key}, True:{real_res[key]}, My:{my_res[key]}")
    except:
        print(f"Key:{key}, True:{real_res[key]}, My:{my_res[key]}")

