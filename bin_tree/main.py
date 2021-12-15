import os


class Node:
    def __init__(self, key, parent):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent

    def __str__(self):
        return f"{self.key}"


class Tree:
    def __init__(self):
        self.root = None
        self.last = None

    def insert(self, key):
        curr = self.root
        last = self.last
        if last:
            if key == last.key - 1 or key == last.key + 1:
                curr = last
        while curr:
            if key > curr.key:
                if curr.right is not None:
                    curr = curr.right
                else:
                    curr.right = Node(key, curr)
                    self.last = curr.right
                    return False
            elif key < curr.key:
                if curr.left is not None:
                    curr = curr.left
                else:
                    curr.left = Node(key, curr)
                    self.last = curr.left
                    return False
            else:
                self.last = curr
                return True
        if self.root is None:
            self.root = Node(key, None)
            self.last = self.root
        return False

    def find_next(self):
        if self.last.right:
            next = self.last.right
            while next and next.left:
                next = next.left
        else:
            next = self.last.parent
            while next and next.key < self.last.key:
                next = next.parent
        return next.key if next else '-'

    def print(self):
        level = 0
        res = ["-" for _ in range(level+1)]
        res =''.join(res)
        if self.root is None:
            print(res + "None")
            print()
            return
        print(res + str(self.root))
        self.__print(self.root.left, level + 1)
        self.__print(self.root.right, level + 1)
        print()

    def __print(self, node, level):
        res = ["-" for _ in range(level + 1)]
        res = ''.join(res)
        if node is None:
            print(res + "None")
            return
        print(res + str(node))
        self.__print(node.left, level+1)
        self.__print(node.right, level+1)


real_res_contains = {}
real_res_min_after = {}
my_res_contains = {}
my_res_min_after = {}
for path in sorted(os.listdir("./")):
    if ".in" not in path and ".out" not in path:
        continue

    number = int(path.split(".")[0])
    line_count = 0
    if "out" in path:
        with open(path, "r") as file:
            if "contains" in path:
                for line in file:
                    if real_res_contains.get(number):
                        real_res_contains[number].append(line[0])
                    else:
                        real_res_contains[number] = [line[0]]
            if "min-after" in path:
                for line in file:
                    if real_res_min_after.get(number):
                        real_res_min_after[number].append(line[:-1])
                    else:
                        real_res_min_after[number] = [line[:-1]]
    else:
        tree = Tree()
        print(number)
        with open(path, "r") as file:
            array = []
            for line in file:
                if line_count != 0:
                    key = int(line)
                    exists = tree.insert(key)
                    symbol_exist = '+' if exists else '-'
                    if my_res_contains.get(number):
                        my_res_contains[number].append(symbol_exist)
                    else:
                        my_res_contains[number] = [symbol_exist]
                    next = tree.find_next()
                    res = symbol_exist + ' ' + str(next)
                    if my_res_min_after.get(number):
                        my_res_min_after[number].append(res)
                    else:
                        my_res_min_after[number] = [res]
                line_count += 1

for key in real_res_contains.keys():
    try:
        assert real_res_contains[key] == my_res_contains[key]
        assert real_res_min_after[key] == my_res_min_after[key]
    except:
        print(f"Key:{key}, True:{real_res_contains[key]}, My:{my_res_contains[key]}")
        print(f"Key:{key}, True:{real_res_min_after[key]}, My:{my_res_min_after[key]}")
        exit()

