import os


def binary_search(array, el):
    left = 0
    right = len(array) - 1
    while right - left > 1:
        mid = (left + right) // 2
        if array[mid] == el:
            return mid
        elif array[mid] > el:
            right = mid
        else:
            left = mid
    if array[left] == el:
        return left
    elif array[right] == el:
        return right
    return -1

real_res = {}
my_res = {}
for path in sorted(os.listdir("../")):
    if ".in" not in path and ".out" not in path:
        continue
    print(path)

    number = int(path.split(".")[0])
    line_count = 0
    if "out" in path:
        with open(path, "r") as file:
            for line in file:
                if real_res.get(number):
                    real_res[number].append(int(line))
                else:
                    real_res[number] = [int(line)]
    else:
        with open(path, "r") as file:
            array = []
            for line in file:
                if line_count == 0:
                    arr_len = int(line)
                elif line_count == 1:
                    array = list(map(lambda x: int(x), line.split(" ")))
                elif line_count == 2:
                    line_count += 1
                    continue
                else:
                    if my_res.get(number):
                        my_res[number].append(binary_search(array, int(line)))
                    else:
                        my_res[number] = [binary_search(array, int(line))]
                line_count += 1

for key in real_res.keys():
    for i, el in enumerate(real_res[key]):
        try:
            assert el == my_res[key][i]
        except:
            print(f"Key:{key}, Id: {i}, True:{el}, My:{my_res[key][i]}")

