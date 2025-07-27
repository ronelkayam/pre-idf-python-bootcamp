#get and return function
def getAndReturn(name):
    print("hello from getAndReturn func")
    return "hello "+name

print(f"out of function\n{getAndReturn('Ron')}")

#returnAndNotGet
def returnAndNotGet():
    print("hello from returnAndNotGet func")
    return "return from returnAndNotGet func"

returnFromFunc = returnAndNotGet()
print(returnFromFunc)

#getAndNotReturn func

def getAndNotReturnFunc(nameForFunc):
    print("hello from getAndNotReturn func")

nameFromMain = input("please enter your name")
getAndNotReturnFunc(nameFromMain)


#notGetAndNotReturn
def notGetAndNotReturnFunc():
    print("hello from notGetAndNotReturn func")

notGetAndNotReturnFunc()

