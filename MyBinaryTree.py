from UserPrintData import UserData

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def children(self):
        if self.left is None and self.right is None:
            return 0
        elif not (self.right is None) and not (self.left is None):
            return 2
        else:
            return 1


class MyBinaryTree:

    def __init__(self):
        self.root = None

    def __recursive_insertion(self, current_node, data):

        if data < current_node.data:
            if current_node.left == None:
                current_node.left = Node(data)
                return True
            else:
                return self.__recursive_insertion(current_node.left, data)
        elif data > current_node.data:
            if current_node.right == None:
                current_node.right = Node(data)
                return True
            else:
                return self.__recursive_insertion(current_node.right, data)

        elif current_node.data == data:
            return False

    def __recursive_search(self, current_node, to_find):
        if current_node.data == to_find:
            return True
        elif to_find < current_node.data:
            return self.__recursive_search(current_node.left, to_find)
        elif to_find > current_node.data:
            return self.__recursive_search(current_node.right, to_find)
        else:
            return False

    def _single_child_deletion(self, parent_node, node_to_remove):
        if parent_node.left.data == node_to_remove.data:
            parent_node.left = node_to_remove.right if node_to_remove.left is None else node_to_remove.left
            return True
        elif parent_node.right.data == node_to_remove.data:
            parent_node.right = node_to_remove.right if node_to_remove.left is None else node_to_remove.left
            return True

    def _two_children_removing(self, node_to_remove):
        if node_to_remove.right.children() == 0:
            node_to_remove.data = node_to_remove.right.data
            node_to_remove.right = None
            return True


        current_el = node_to_remove.right
        while (not (current_el.left is None)) and (not (current_el.left.left is None)):
            current_el = current_el.left

        node_to_remove.data = current_el.left.data
        current_el.left = None

    def __recursive_deletion(self, current_node, to_remove):

        if (not (current_node.left is None)) and current_node.left.data == to_remove:
            local_children = current_node.left.children()

            if local_children == 0:
                current_node.left = None
                return True
            elif local_children == 1:
                return self.__single_child_deletion(current_node, current_node.left)
            elif local_children == 2:
                return self.__two_children_removing(current_node.left)


        elif (not (current_node.right is None)) and current_node.right.data == to_remove:
            local_children = current_node.right.children()

            if local_children == 0:
                current_node.right = None
                return True
            elif local_children == 1:
                return self.__single_child_deletion(current_node, current_node.right)
            elif local_children == 2:
                return self.__two_children_removing(current_node.right)

        elif to_remove < current_node.data:
            return self.__recursive_deletion(current_node.left, to_remove)
        elif to_remove > current_node.data:
            return self.__recursive_deletion(current_node.right, to_remove)

    def __recursion_up_down_print(self, starter, user_data):
        if starter.data == self.root.data:
            user_data.tree_string = f"{starter.data}"

        if not (starter.left is None):
            user_data.tree_string = f"{user_data.tree_string} {starter.left.data}"
            self.__recursion_up_down_print(starter.left, user_data)

        if not (starter.right is None):
            user_data.tree_string = f"{user_data.tree_string} {starter.right.data}"
            self.__recursion_up_down_print(starter.right, user_data)

        return user_data.tree_string

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return

        return self.__recursive_insertion(self.root, data)

    def contains(self, to_find):
        if self.root is None:
            return False
        else:
            return self.__recursive_search(self.root, to_find)

    def delete(self, to_remove):
        if self.root is None:
            return

        return self.__recursive_deletion(self.root, to_remove)

    def up_down_print(self):
        if self.root is None:
            return

        return self.__recursion_up_down_print(self.root, UserData())