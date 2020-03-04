a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
print(len(a))

del a[2:4]
print(a)

del a[:]
print(a)

# del can also be used to delete entire variables
del a
print(a)
