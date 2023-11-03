# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 17:35:46 2023

@author: Ethan
"""
digits = [1, 8, 2, 8]
print("\nSection 2.3.5:")
print("I am string!")
print("I've got an apostrophe")

city = "Berkeley"
print("len(city) =", len(city))
print("city[3] =", city[3])
print("'Shabu ' * 2 = " + "Shabu " * 2)
print("'here' in 'Where's Waldo?' =", "here" in "Where's Waldo?")

print("str(2) + ' is an element of ' + str(digits) =", str(2) + 
      ' is an element of ' + str(digits))

print("/nSection 2.3.6:")
def tree(root_label, branches = []):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root_label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

t = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
print("t =", t)
print("label(t) =", label(t))
print("branches(t) =", branches(t))
print("label(branches(t)[1]) =", label(branches(t)[1]))
print("is_leaf(t) =", is_leaf(t))
print("is_leaf(branches(t)[0]) =", is_leaf(branches(t)[0]))

def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left, right = fib_tree(n - 2), fib_tree(n - 1)
        fib_n = label(left) + label(right)
        return tree(fib_n, [left, right])

print("fib_tree(5) =", fib_tree(5))

def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        branch_counts = [count_leaves(b) for b in branches(tree)]
        return sum(branch_counts)
print("count_leaves(fib_tree(5)) =", count_leaves(fib_tree(5)))

def partition_tree(n, m):
    if n == 0:
        return tree(True)
    elif n < 0 or m == 0:
        return tree(False)
    else:
        left = partition_tree(n - m, m)
        right = partition_tree(n, m - 1)
        return tree(m, [left, right])

print("partition_tree(2, 2) =", partition_tree(2, 2))

def print_parts(tree, partition = []):
    if is_leaf(tree):
        if label(tree):
            print(" + ".join(partition))
    else:
        left, right = branches(tree)
        m = str(label(tree))
        print_parts(left, partition + [m])
        print_parts(right, partition)

print("print_parts(partition_tree(6, 4)) =", print_parts(partition_tree(6, 4)))

# This is broken code
# def right_binarize(tree):
#     if is_leaf(tree):
#         return tree
#     if len(tree) > 2:
#         tree = tree(tree[0], tree[1:]]
#     return [right_binarize(b) for b in tree]

# print("right_binarize([1, 2, 3, 4, 5, 6, 7]) =", 
#       right_binarize([1, 2, 3, 4, 5, 6, 7]))

print("\nSection 2.3.7:")
empty = "empty"
def is_link(s):
    return s == empty or (len(s) == 2 and is_link(s[1]))

def link(first, rest):
    assert is_link(rest)
    return [first, rest]

def first(s):
    assert is_link(s), "first only applies to linked lists."
    assert s != empty, "empty linked list has no first element."
    return s[0]

def rest(s):
    assert is_link(s), "rest only applies to linked lists."
    assert s != empty, "empty linked list has no first element."
    return s[1]

four = link(1 ,link(2, link(3, link(4, empty))))
print("first(four) =", first(four))
print("rest(four) =", rest(four))

def len_link(s):
    length = 0
    while s != empty:
        s, length = rest(s), length + 1
    return length

def getitem_link(s, i):
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)

print("len_link(four) =", len_link(four))
print("getitem_link(four, 1) =", getitem_link(four, 1))

def len_link_recursive(s):
    """Return the length of a linked list s."""
    if s == empty:
        return 0
    return 1 + len_link_recursive(rest(s))

def getitem_link_recursive(s, i):
    """Return the element at index i of linked list s."""
    if i == 0:
        return first(s)
    return getitem_link_recursive(rest(s), i - 1)

print("len_link_recursive(four) =", len_link_recursive(four))
print("getitem_link_recursive(four, 1) =", getitem_link_recursive(four, 1))

def extend_link(s, t):
    """Return a list with the elements of s followed by those of t."""
    assert is_link(s) and is_link(t)
    if s == empty:
        return t
    else:
        return link(first(s), extend_link(rest(s), t))

print("extend_link(four, four) =", extend_link(four, four))

def apply_to_all_link(f, s):
    """Apply f to each element of s."""
    assert is_link(s)
    if s == empty:
        return s
    else:
        return link(f(first(s)), apply_to_all_link(f, rest(s)))

print("extend_link(four, four) =", extend_link(four, four))

def keep_if_link(f, s):
    """Return a list with elements of s for which f(e) is true."""
    assert is_link(s)
    if s == empty:
        return s
    else:
        kept = keep_if_link(f, rest(s))
        if f(first(s)):
            return link(first(s), kept)
        else:
            return kept
        
print("keep_if_link(lambda x: x%2 == 0, four) =", keep_if_link(lambda x: x%2 == 0, four))

def join_link(s, separator):
    """Return a string of all elements in s separated by separator."""
    if s == empty:
        return ""
    elif rest(s) == empty:
        return str(first(s))
    else:
        return str(first(s)) + separator + join_link(rest(s), separator)
    
print("join_link(four, ", ") =", join_link(four, ", "))

def partitions(n, m):
    """Return a linked list of partitions of n using parts of up to m.
    Each partition is represented as a linked list.
    """
    if n == 0:
        return link(empty, empty) # A list containing the empty partition
    elif n < 0 or m == 0:
        return empty
    else:
        using_m = partitions(n-m, m)
        with_m = apply_to_all_link(lambda s: link(m, s), using_m)
        without_m = partitions(n, m-1)
        return extend_link(with_m, without_m)

def print_partitions(n, m):
    lists = partitions(n, m)
    strings = apply_to_all_link(lambda s: join_link(s, " + "), lists)
    print(join_link(strings, "\n"))
    
print("print_partitions(6, 4) =", print_partitions(6, 4))