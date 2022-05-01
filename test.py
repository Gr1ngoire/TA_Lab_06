from MyRedBlackTree import *
from UnbalancedTree import *
import random
import time

rb_tree = MyRedBlackTree()
unbalanced_tree = UnbalancedTree()

#filling with 1000
print("#Insertion(1000)")
print("random")
print("balanced")
random_vals = [random.randrange(10**5, 10**9) for i in range(1000)]
start = time.perf_counter()
for val in random_vals:
    rb_tree.insert(val)
print((time.perf_counter() - start) * 1000)
print("unbalanced")
start = time.perf_counter()
for val in random_vals:
    unbalanced_tree.insert(val)
print((time.perf_counter() - start) * 1000)
print("consecutive")
print("balanced")
rb_tree = MyRedBlackTree()
unbalanced_tree = UnbalancedTree()
start = time.perf_counter()
for val in range(1000):
    rb_tree.insert(val)
print((time.perf_counter() - start) * 1000)
print("unbalanced")
start = time.perf_counter()
for val in range(1000):
    unbalanced_tree.insert(val)
print((time.perf_counter() - start) * 1000)
#Search
print("#Search")
print("balanced")
start = time.perf_counter()
rb_tree.contains(500)
print((time.perf_counter() - start) * 1000)
print("unbalanced")
start = time.perf_counter()
unbalanced_tree.insert(500)
print((time.perf_counter() - start) * 1000)
