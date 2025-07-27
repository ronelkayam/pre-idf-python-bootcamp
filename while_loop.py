num = 5
count = 0
while num > 0:
    count += 1
    print(num)
    if count == 5:
        print(f"\nif condition")
        num = 0
    print(f"in while loop")
print(f"\nout of while loop")