from avlTree import AVLTree

print("initializing tests")

a = AVLTree()
lista = [3,2,4,1,5]
print("inserting a list:", lista)
for i in lista:
    a.insert(i)

a.print()
print("left: rotate:")
print("insert:",0)
a.insert(0)
a.print()
print("right rotate:")
print("insert:",7)
a.insert(7)
a.print()
print("deleting root:", 3)
a.delete(3)
a.print()
print("deleting: ", 5)
a.delete(5)
a.print()
print("Input: ", lista)
for i in lista:
    a.insert(i)
a.print()
print("deleting: ", 3)
print("deleting: ", 4)
a.delete(3)
a.delete(4)
a.print()
print("is balanced:",a.check_balanced())