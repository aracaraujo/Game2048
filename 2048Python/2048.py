from audioop import add
import random
from pynput.keyboard import Key, Listener
import os

def createBoard():
    """Generates a 4x4 board with two initial values randonly chosen between 2 and 4"""
    a = [0,0,0,0]
    b = [0,0,0,0]
    c = [0,0,0,0]
    d = [0,0,0,0]
    boardList = [a,b,c,d]
    
    addNumber(boardList)
    addNumber(boardList)
    
    return boardList

def displayBoard(boardlist):
    """Receives the board in form of a list of lists and displays it"""
    for i in boardlist:
        print(i)

def addNumber(boardlist):
    """Choose a random spot in the grid and if it's 0 adds a number"""
    status = True
    while status:
        randomL = random.choice(boardlist)
        randomI = random.randint(0,3)
        if randomL[randomI] == 0:
            randomN = random.randint(1,4)
            if randomN == 3:
                randomN = 2
            elif randomN == 1:
                randomN = 2
            randomL[randomI] = randomN
            status = False
        else:
            pass

def moveDown(boardlist):
    """Move numbers down and combine equal numbers"""
    previousList = []
    previousRow = []
    for row in boardlist:
        for value in row:
            previousRow.append(value)
        previousList.append(previousRow)
        previousRow = []
    a = boardlist[0]
    b = boardlist[1]
    c = boardlist[2]
    d = boardlist[3]
    index = 0
    moveChecker = False
    global totalScore
    while index < 4:
        #Push numbers down for the first time
        if b[index] == 0:
            b[index] = a[index]
            a[index] = 0
        if c[index] == 0:
            c[index] = b[index]
            b[index] = 0
        if d[index] == 0:
            d[index] = c[index]
            c[index] = 0
        #Push numbers down for the second time
        if b[index] == 0:
            b[index] = a[index]
            a[index] = 0
        if c[index] == 0:
            c[index] = b[index]
            b[index] = 0
        if d[index] == 0:
            d[index] = c[index]
            c[index] = 0
        #Sum numbers
        check = True
        if d[index] == c[index] and check:
            d[index] += c[index]
            totalScore+=d[index]
            c[index] = 0
            check = False
        if c[index] == b[index] and check:
            c[index] += b[index]
            totalScore+=c[index]
            b[index] = 0
            check = False
        else:
            check = True
        if b[index] == a[index] and check:
            b[index] += a[index]
            totalScore+=b[index]
            a[index] = 0
            check = False
        #Push numbers down for the last time
        if b[index] == 0:
            b[index] = a[index]
            a[index] = 0
        if c[index] == 0:
            c[index] = b[index]
            b[index] = 0
        if d[index] == 0:
            d[index] = c[index]
            c[index] = 0
        index += 1
    if a != previousList[0]:
        moveChecker = True
    if b != previousList[1]:
        moveChecker = True
    if c != previousList[2]:
        moveChecker = True
    if d != previousList[3]:
        moveChecker = True
    boardlist = [a,b,c,d]
    return moveChecker

def moveUp(boardlist):
    """Move numbers up and combine equal numbers"""
    previousList = []
    previousRow = []
    for row in boardlist:
        for value in row:
            previousRow.append(value)
        previousList.append(previousRow)
        previousRow = []
    moveChecker = False
    a = boardlist[0]
    b = boardlist[1]
    c = boardlist[2]
    d = boardlist[3]
    index = 0
    global totalScore
    while index < 4:
        #Push numbers up for the first time
        if c[index] == 0:
            c[index] = d[index]
            d[index] = 0
        if b[index] == 0:
            b[index] = c[index]
            c[index] = 0
        if a[index] == 0:
            a[index] = b[index]
            b[index] = 0
        #Push numbers up for the second time
        if c[index] == 0:
            c[index] = d[index]
            d[index] = 0
        if b[index] == 0:
            b[index] = c[index]
            c[index] = 0
        if a[index] == 0:
            a[index] = b[index]
            b[index] = 0
        #Sum numbers
        check = True
        if a[index] == b[index] and check:
            a[index] += b[index]
            totalScore += a[index]
            b[index] = 0
            check = False
        if b[index] == c[index] and check:
            b[index] += c[index]
            totalScore += b[index]
            c[index] = 0
            check = False
        else:
            check = True
        if c[index] == d[index] and check:
            c[index] += d[index]
            totalScore += c[index]
            d[index] = 0
        #Push numbers up for the last time
        if c[index] == 0:
            c[index] = d[index]
            d[index] = 0
        if b[index] == 0:
            b[index] = c[index]
            c[index] = 0
        if a[index] == 0:
            a[index] = b[index]
            b[index] = 0
        index += 1
    if a != previousList[0]:
        moveChecker = True
    if b != previousList[1]:
        moveChecker = True
    if c != previousList[2]:
        moveChecker = True
    if d != previousList[3]:
        moveChecker = True
    boardlist = [a,b,c,d]
    return moveChecker

def moveRight(boardlist):
    """Push numbers to the right"""
    global totalScore
    previousList = []
    previousRow = []
    for row in boardlist:
        for value in row:
            previousRow.append(value)
        previousList.append(previousRow)
        previousRow = []
    moveChecker = False
    for row in boardlist:
        #push numbers to the right for the first time
        for index in range(1,4):
            if row[index] == 0:
                row[index] = row[index-1]
                row[index-1] = 0
        #push numbers to the right for the seconde time
        for index in range(1,4):
            if row[index] == 0:
                row[index] = row[index-1]
                row[index-1] = 0
        #sum numbers
        check = True
        if row[3] == row[2] and check:
            row[3] += row[2]
            totalScore += row[3]
            row[2] = 0
            check = False
        if row[2] == row[1] and check:
            row[2] += row[1]
            totalScore += row[2]
            row[1] = 0
            check = False
        else:
            check = True
        if row[1] == row[0] and check:
            row[1] += row[0]
            totalScore += row[1]
            row[0] = 0
        #push numbers to the right for the last time
        for index in range(1,4):
            if row[index] == 0:
                row[index] = row[index-1]
                row[index-1] = 0
        if boardlist[0] != previousList[0]:
            moveChecker = True
        if boardlist[1] != previousList[1]:
            moveChecker = True
        if boardlist[2] != previousList[2]:
            moveChecker = True
        if boardlist[3] != previousList[3]:
            moveChecker = True
    return moveChecker

def moveLeft(boardlist):
    previousList = []
    previousRow = []
    for row in boardlist:
        for value in row:
            previousRow.append(value)
        previousList.append(previousRow)
        previousRow = []
    moveChecker = False
    positions = [2,1,0]
    global totalScore
    for row in boardlist:
        #push numbers to the left for the first time
        for index in positions:
            if row[index] == 0:
                row[index] = row[index+1]
                row[index+1] = 0
        #push numbers to the left for the second time
        for index in positions:
            if row[index] == 0:
                row[index] = row[index+1]
                row[index+1] = 0
        #sum numbers
        check = True
        if row[0] == row[1] and check:
            row[0] += row[1]
            totalScore += row[0]
            row[1] = 0
            check = False
        if row[1] == row[2] and check:
            row[1] += row[2]
            totalScore += row[1]
            row[2] = 0
            check = False
        else:
            check = True
        if row[2] == row[3] and check:
            row[2] += row[3]
            totalScore += row[2]
            row[3] = 0
        #push numbers to the left for the first time
        for index in positions:
            if row[index] == 0:
                row[index] = row[index+1]
                row[index+1] = 0
        if boardlist[0] != previousList[0]:
            moveChecker = True
        if boardlist[1] != previousList[1]:
            moveChecker = True
        if boardlist[2] != previousList[2]:
            moveChecker = True
        if boardlist[3] != previousList[3]:
            moveChecker = True
    return moveChecker

def gameChecker(boardlist):
    a = boardlist[0]
    b = boardlist[1]
    c = boardlist[2]
    d = boardlist[3]
    positionChecker = 0
    index = 0
    positionAvailability = True
    addAvailability = False
    for row in boardlist:
        for value in row:
            if value == 0:
                positionChecker = 1
        for i in range(3):
            if row[i] == row[i+1]:
                addAvailability = True
    while index < 4:
        if b[index] == a[index]:
            addAvailability = True
        if c[index] == b[index]:
            addAvailability = True
        if d[index] == c[index]:
            addAvailability = True
        index +=1
    if positionChecker == 0:
        positionAvailability = False
    if not positionAvailability and not addAvailability:
        return False
    else:
        return True

# Game loop
os.system("clear")
board = createBoard()
totalScore = 0
gameStatus = True
displayBoard(board)
print()
print(f"Your score is: {totalScore}")

def on_press(key):
    global totalScore
    global gameStatus
    if key == Key.down:
        os.system("clear")
        if moveDown(board):
            addNumber(board)
        if not gameChecker(board):
            gameStatus = False  
        displayBoard(board)
        print()
        print(f"Your score is: {totalScore}")
    if key == Key.up:
        os.system("clear")
        if moveUp(board):
            addNumber(board)
        if not gameChecker(board):
            gameStatus = False      
        displayBoard(board)
        print()
        print(f"Your score is: {totalScore}")
    if key == Key.right:
        os.system("clear")
        if moveRight(board):
            addNumber(board)
        if not gameChecker(board):
            gameStatus = False  
        displayBoard(board)
        print()
        print(f"Your score is: {totalScore}")
    if key == Key.left:
        os.system("clear")
        if moveLeft(board):
            addNumber(board)
        if not gameChecker(board):
            gameStatus = False   
        displayBoard(board)
        print()
        print(f"Your score is: {totalScore}")
    if not gameStatus:
        return False
    # if key == Key.esc:
    #     return False
def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
# Collect events until released``

os.system("clear")
displayBoard(board)
print(f"Your higher score is: {totalScore}")