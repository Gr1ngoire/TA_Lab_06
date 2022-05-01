from UserPrintData import UserData


class BalancedNode:

    def __init__(self, data, parent):
        self.parent = parent
        self.data = data
        self.left = None
        self.right = None
        self.color = "Red"

    def set_parent(self, new_p):
        self.parent = new_p

    def children(self):
        if self.left is None and self.right is None:
            return 0
        elif not (self.right is None) and not (self.left is None):
            return 2
        else:
            return 1


class MyRedBlackTree:

    def __init__(self):
        self.root = None

    def __recursion_up_down_print(self, starter, user_data):
        if starter.data == self.root.data:
            user_data.tree_string = f"{f'|{starter.data}|' if starter.color == 'Black' else starter.data}"

        if not (starter.left is None):
            user_data.tree_string = f"{user_data.tree_string} {f'|{starter.left.data}|' if starter.left.color == 'Black' else starter.left.data}"
            self.__recursion_up_down_print(starter.left, user_data)

        if not (starter.right is None):
            user_data.tree_string = f"{user_data.tree_string} {f'|{starter.right.data}|' if starter.right.color == 'Black' else starter.right.data}"
            self.__recursion_up_down_print(starter.right, user_data)

    def __left_rotation(self, node):
        p = node.parent
        temp = node.right
        node.right = temp.left
        if not (temp.left is None):
            temp.left.set_parent(node)
        temp.left = node
        node.set_parent(temp)
        temp.set_parent(p)
        if node.data == self.root.data:
            self.root = temp
        if not (p is None):
            if not (p.right is None) and p.right.data == node.data:
                p.right = temp
            else:
                p.left = temp
        temp.color = "Black"
        if not (temp.right is None):
            temp.right.color = "Red"
        if not (temp.left is None):
            temp.left.color = "Red"
        return temp

    def __right_rotation(self, node):
        p = node.parent
        temp = node.left
        node.left = temp.right
        if not (temp.right is None):
            temp.right.set_parent(node)
        temp.right = node
        node.set_parent(temp)
        temp.set_parent(p)

        if node.data == self.root.data:
            self.root = temp
        if not (p is None):
            if not (p.left is None) and p.left.data == node.data:
                p.left = temp
            else:
                p.right = temp
        temp.color = "Black"
        if not (temp.right is None):
            temp.right.color = "Red"
        if not (temp.left is None):
            temp.left.color = "Red"
        return temp

    def __left_left_case(self, node):
        return self.__right_rotation(node)

    def __left_right_case(self, node):
        node.left = self.__left_rotation(node.left)
        return self.__left_left_case(node)

    def __right_right_case(self, node):
        return self.__left_rotation(node)

    def __right_left_case(self, node):
        node.right = self.__right_rotation(node.right)
        return self.__right_right_case(node)

    def __balance(self, node):
        if node.color == "Black":
            return

        if node.color == "Red" and node.parent.color == "Red":

            if not (node.parent.parent is None) and node.parent.parent.children() == 2:

                if node.parent.parent.left.data == node.parent.data and node.parent.parent.right.color == "Black":
                    if not (node.parent.left is None) and node.parent.left.data == node.data:
                        self.__left_left_case(node.parent.parent)
                    elif not (node.parent.right is None) and node.parent.right.data == node.data:
                        self.__left_right_case(node.parent.parent)

                elif node.parent.parent.right.data == node.parent.data and node.parent.parent.left.color == "Black":
                    if not (node.parent.left is None) and node.parent.left.data == node.data:
                        self.__right_left_case(node.parent.parent)
                    elif not (node.parent.right is None) and node.parent.right.data == node.data:
                        self.__right_right_case(node.parent.parent)

                elif (node.parent.parent.left.data == node.parent.data and node.parent.parent.right.color == "Red") or (
                        node.parent.parent.right.data == node.parent.data and node.parent.parent.left.color == "Red"):
                    node.parent.parent.left.color = "Black"
                    node.parent.parent.right.color = "Black"
                    if node.parent.parent.data == self.root.data:
                        return
                    else:
                        node.parent.parent.color = "Red"
                        self.__balance(node.parent.parent)

            elif (not (node.parent.parent is None)) and node.parent.parent.children() == 1:

                if not (node.parent.parent.left is None) and node.parent.parent.left.data == node.parent.data:

                    if not (node.parent.left is None) and node.parent.left.data == node.data:
                        self.__left_left_case(node.parent.parent)
                    elif not (node.parent.right is None) and node.parent.right.data == node.data:
                        self.__left_right_case(node.parent.parent)

                elif not (node.parent.parent.right is None) and node.parent.parent.right.data == node.parent.data:
                    if not (node.parent.left is None) and node.parent.left.data == node.data:
                        self.__right_left_case(node.parent.parent)
                    elif not (node.parent.right is None) and node.parent.right.data == node.data:
                        self.__right_right_case(node.parent.parent)


    def __recursive_insertion(self, starter, data):
        if starter.data == data:
            raise Exception("Can not insert already existing value")
        elif data < starter.data and starter.left is None:
            starter.left = BalancedNode(data, starter)
            self.__balance(starter.left)
        elif data > starter.data and starter.right is None:
            starter.right = BalancedNode(data, starter)
            self.__balance(starter.right)

        elif data < starter.data and not (starter.left is None):
            self.__recursive_insertion(starter.left, data)
        elif data > starter.data and not (starter.right is None):
            self.__recursive_insertion(starter.right, data)

    def __recursive_search(self, starter, data):
        if data == starter.data:
            return True
        elif data < starter.data:
            self.__recursive_search(starter.left, data)
        elif data > starter.data:
            self.__recursive_search(starter.right, data)

    def contains(self, data):
        if self.root is None:
            return False

        self.__recursive_search(self.root, data)

    def insert(self, data):
        if self.root is None:
            self.root = BalancedNode(data, None)
            self.root.color = "Black"
            return

        self.__recursive_insertion(self.root, data)

    def up_down_print(self):
        if self.root is None:
            return

        result = UserData()
        self.__recursion_up_down_print(self.root, result)
        return result.tree_string
