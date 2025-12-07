l=[11,21,3,4]
# l.append(5)
# print(l)
# l.sort()
# print(l)
# l.reverse()
# print(l)
# l.insert(2,15)
# print(l)    
# l.remove(3)
# print(l)
m=l
m[0]=0

print(l)
m = l.copy()
m[0] = 99
print("After modifying m (copy):", m)
print("Original list l remains:", l)

