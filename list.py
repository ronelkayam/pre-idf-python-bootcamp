ls1 = [1, 2, 3, 4, 5]
ls2 = [1, 3, True, "String"]
print(f"initialize list :{ls1}")

ls1.append(23)
ls1.append(56)
print(f"list after appending: {ls1}")

ls1.insert(0, "hello")
print(f"after insert order:{ls1}")

print(f"list length: {len(ls1)}")

print(f"first argument in ls1: {ls1[1]}")

# [start:stop:jump]
print(f"arguments 0-7 from list:{ls1[0:7]}")

print(f"arguments 0-6 with jump 2 from list:{ls1[0:6:2]}")

for i in range(5):
    print(i)

for i in ls1:
    print(i, end=",")
