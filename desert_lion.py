start = 1
end = 1000
middle = (start+end)//2
guess = 40
while middle!=guess:
    print("start = ", start, "middle = ", middle, "end = ", end)
    if guess>start and guess<middle:
        end = middle
        middle = (start+end)//2
    else:
        start = middle
        middle = (start+end)//2
print("found the guess:)")



