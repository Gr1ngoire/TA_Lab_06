from MyBinaryTree import MyBinaryTree
from MyRedBlackTree import MyRedBlackTree

# tree = MyBinaryTree()
#
# tree.insert(10)
# tree.insert(20)
# tree.insert(5)
# tree.insert(100)
# tree.insert(50)
# tree.insert(200)
#
# print(tree.contains(10))
#
# print(tree.up_down_print())
#
# tree.delete(100)
# print()
# print("AFTER")
# print()
# print(tree.up_down_print())
#
# tree.insert(4)
# tree.insert(6)
# tree.insert(8)
# tree.insert(7)
# tree.insert(9)
#
# print(tree.up_down_print())
#
# print(tree.delete(8))
#
# print(tree.up_down_print())
#
# print(tree.insert(200))
# print(tree.up_down_print())

my_red_black_tree = MyRedBlackTree()

my_red_black_tree.insert(10)
my_red_black_tree.insert(5)
my_red_black_tree.insert(20)

print(my_red_black_tree.up_down_print())

my_red_black_tree.insert(30)

print(my_red_black_tree.up_down_print())

my_red_black_tree.insert(40)

print(my_red_black_tree.up_down_print())

my_red_black_tree.insert(35)

print(my_red_black_tree.up_down_print())

my_red_black_tree.insert(37)

print(my_red_black_tree.up_down_print())

my_red_black_tree.insert(7)

print(my_red_black_tree.up_down_print())

my_red_black_tree.insert(6)

print(my_red_black_tree.up_down_print())