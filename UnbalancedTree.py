class Node:
    def __init__(self, left, right, key):
        self.right = right
        self.left = left
        self.key = key


class UnbalancedTree:
    def __init__(self):
        self.leaf = Node(None, None, None)

    def insert(self, value):
        if self.leaf.key is None:
            self.leaf.key = value
        else:
            check = self.leaf
            while check.key is not None:
                if value == check.key:
                    break
                if value < check.key:
                    if check.left is None:
                        check.left = Node(None, None, value)
                        break
                    check = check.left
                    continue
                if value > check.key:
                    if check.right is None:
                        check.right = Node(None, None, value)
                        break
                    check = check.right
                    continue
        return

    def delete(self):
        if self.leaf.left is None and self.leaf.right is None:
            self.leaf.key = None
        elif self.leaf.left is None and self.leaf.right is not None:
            self.leaf = self.leaf.right
        elif self.leaf.right is None and self.leaf.left is not None:
            self.leaf = self.leaf.left
        else:
            if self.leaf.right.left is None:
                self.leaf = self.leaf.right
            else:
                helper = self.leaf.right
                h = 0
                check = self.leaf.right
                while check.left is not None:
                    if h >= 1:
                        helper = helper.left
                    h += 1
                    check = check.left
                self.leaf.key = check.key
                helper.left = None
        return

    def __recursion_up_down_print(self, starter, user_data):
        if starter.key == self.leaf.key:
            user_data.tree_string = f"{starter.key}"

        if not (starter.left is None):
            user_data.tree_string = f"{user_data.tree_string} {starter.left.key}"
            self.__recursion_up_down_print(starter.left, user_data)

        if not (starter.right is None):
            user_data.tree_string = f"{user_data.tree_string} {starter.right.key}"
            self.__recursion_up_down_print(starter.right, user_data)
    
    def search(self, element):
        it = 0
        check = self.leaf
        while check.key is not None:
            it += 1
            if check.key == element:
                return "Yeah,you got it!\n iterations: " + str(it)
            if element < check.key:
                if check.left is None:
                    break
                check = check.left
            if element > check.key:
                if check.right is None:
                    break
                check = check.right
        return "NoFound\n iterations: " + str(it)

