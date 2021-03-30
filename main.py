"""
Variable


name = "Your Man"
artist = "Jose Tuner"
genre = "Pop"
duration = 340
released = 2002
publicDate = "2002-05-10"

print(name)
print(artist)
print(genre)
print(duration)
print(released)
print(publicDate)

"""

"""
Function


def getName():
    return name

def getArtist():
    return artist

def getGenre():
    return genre

def isReleased(released):
    return bool(released)

print(getName())
print(getArtist())
print(getGenre())
print(isReleased(released))

"""

"""
If statement


def checkIsEqual(one,two,three):
    numOne = int(one)
    numTwo = int(two)
    numThree = int(three)
    if (numOne == numTwo):
        return True
    elif (numOne == numThree):
        return True
    elif (numTwo == numThree):
        return True
    else:
        return False

print(checkIsEqual("1",3,2))
"""

"""
List


myUniqueList = []
myLeftOver = []

def rejectedValue(value):
    myLeftOver.append(value)

def addList(value):
    if (value in myUniqueList):
        rejectedValue(value)
        return True
    
    myUniqueList.append(value)
    return False

print(addList(1))
print(addList(2))
print(addList(3))
print(addList(1))
print(addList(2))
print("added value", myUniqueList)
print("rejected value",myLeftOver)

"""
"""
Loop

for num in range(1,101,1):
    if(num % 3 == 0 and num % 5 == 0):
        print("FizzBuzz")
    elif(num % 3 == 0):
        isPrime = True
        for i in range(1,num,1):
            if(num % i == 0 and i != 1):
                isPrime = False
                break
        if(isPrime):
            print("Fizz Prime")
        else:
            print("Fizz")
    elif(num % 5 == 0):
        isPrime = True
        for i in range(1,num,1):
            if(num % i == 0 and i != 1):
                isPrime = False
                break
        if(isPrime):
            print("Buzz Prime")
        else:
            print("Buzz")
    else:
        isPrime = True
        for i in range(1,num,1):
            if(num % i == 0 and i != 1):
                isPrime = False
                break
        if(isPrime):
            print(num,"Prime")
        else:
            print(num)

"""
"""
Nested Loop
"""
for row in range(5):
    if(row % 2 == 0):
        for col in range(1,6):
            if(col % 2 == 1):
                if(col != 5):
                    print(" ",end="")
                else:
                    print(" ")
            else:
                print("|",end="")
    else:
        for col in range(1,6):
            if col != 5:
                print("-",end="")
            else:
                print("-")

