# board= [
#     [0,0,1,5,0,9,4,0,2],
#     [0,9,0,1,0,4,5,0,0],
#     [3,5,0,0,0,8,0,9,0],
#     [0,8,3,2,5,1,0,7,0],
#     [0,2,9,7,0,0,3,4,0],
#     [5,0,0,9,0,0,0,0,8],
#     [0,0,0,0,6,0,0,5,0],
#     [0,0,0,0,9,0,2,0,6],
#     [0,4,2,8,0,0,0,0,7]
# ]
board= [
    [8,0,0,0,0,0,0,0,0],
    [0,0,3,6,0,0,0,0,0],
    [0,7,0,0,9,0,2,0,0],
    [0,5,0,0,0,7,0,0,0],
    [0,0,0,0,4,5,7,0,0],
    [0,0,0,1,0,0,0,3,0],
    [0,0,1,0,0,0,0,6,8],
    [0,0,8,5,0,0,0,1,0],
    [0,9,0,0,0,0,4,0,0]
]

def printBoard(b):
    for rowi in range(len(b)):
        if rowi % 3 == 0 and not rowi == 0:
            print("-----------------------")
        for coli in range(len(b[rowi])):
            if coli % 3 == 0 and not coli == 0:
                print(" | ", end="")
            if coli % 8 == 0 and not coli == 0:
                print(str(b[rowi][coli]))
            else:
                print(str(b[rowi][coli])+ " ", end="")

def getNextEmpty(b):
    for rowi in range(len(b)):
        for coli in range(len(b[rowi])):
            if b[rowi][coli] == 0:
                return (rowi, coli)
    return False

def solve(b):
    #get next empty space or done if none
    nextEmpty = getNextEmpty(b)
    if not nextEmpty:
        return True
    #try 0 to 9, if valid, enter it
    for num in range(1,10):
        if isValidMove(b, nextEmpty, num):
            b[nextEmpty[0]][nextEmpty[1]] = num
            #recursive call (try advancing with set number)
            if solve(b):
                return True
            #if cant be solved, set changed pos back to 0
            b[nextEmpty[0]][nextEmpty[1]] = 0

def isValidMove(b, pos, num):
    #check row
    for coli in range(len(b[pos[0]])):
        if b[pos[0]][coli] == num:
            return False
    #check col
    for rowi in range(len(b[pos[0]])):
        if b[rowi][pos[1]] == num:
            return False
    #check field
    v_field = pos[0] // 3
    h_field = pos[1] // 3
    for rowi in range(3):
        for coli in range(3):
            if b[rowi+v_field*3][coli+h_field*3] == num:
                return False
    return True

print("Input Board: ")
printBoard(board)
solve(board)
print()
print("Solution: ")
printBoard(board)