#Pawan Patil - Tic Tac Toe

board = [' ' for  x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter
    
    
def spaceFree(pos):
    return board[pos]==' '
    
def printBoard(board):
    print('   |   |')
    print(' '+ board[1] + ' | ' + board[2] + ' | ' + board[3] )
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '+ board[4] + ' | ' + board[5] + ' | ' + board[6] )
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '+ board[7] + ' | ' + board[8] + ' | ' + board[9] )
    print('   |   |')
    
def isWinner(board, letter):
    return (board[1] == letter and board[2]==letter and board[3]==letter) or (board[4] == letter and board[5]==letter and board[6]==letter) or (board[7] == letter and board[8]==letter and board[9]==letter) or (board[1] == letter and board[4]==letter and board[7]==letter) or (board[2] == letter and board[5]==letter and board[8]==letter) or (board[3] == letter and board[6]==letter and board[9]==letter) or (board[1] == letter and board[5]==letter and board[9]==letter) or (board[3] == letter and board[5]==letter and board[7]==letter)


def playerMove():
    flag = True
    while flag:
        entry = int(input("Select a position to enter X (1-9) :"))
        #Error handling
        
        try:
            if entry>0 and entry<10:
                if spaceFree(entry):
                    flag = False
                    insertLetter('X', entry)
                else:
                    print("This Space is not free !")
            else:
                print("Enter a valid position !")
        except: 
            print("Please enter your position !")

def player1Move():
    flag = True
    while flag:
        entry = int(input("Player 1: Select a position to enter X (1-9) :"))
        #Error handling
        
        try:
            if entry>0 and entry<10:
                if spaceFree(entry):
                    flag = False
                    insertLetter('X', entry)
                else:
                    print("This Space is not free !")
            else:
                print("Enter a valid position !")
        except: 
            print("Please enter your position !")

def player2Move():
    flag = True
    while flag:
        entry = int(input("Player 2: Select a position to enter O (1-9) :"))
        #Error handling
        
        try:
            if entry>0 and entry<10:
                if spaceFree(entry):
                    flag = False
                    insertLetter('O', entry)
                else:
                    print("This Space is not free !")
            else:
                print("Enter a valid position !")
        except: 
            print("Please enter your position !")



def isBoardFull(board):

    if board.count(' ')>1:
        return False
    else:
        return True
    
def compMove():
    moves = [x for x, letter in enumerate(board) if letter == ' ' and x!=0]
    flag = 0
    
    for i in ['O', 'X']:
        for j in moves:
            copyBoard = board[:]
            copyBoard[j] = i
            if isWinner(copyBoard, i):
                flag =j
                return flag

    corners = []
    for i in moves:
        if i in [1,3,7,9]:
            corners.append(i)
    
    if len(corners) > 0:
        flag = selectRandom(corners)
        return flag     

    if 5 in moves:
        flag  = 5
        return flag

    edges = []
    for i in moves:
        if i in [2,4,6,8]:
            edges.append(i)
    
    if len(edges) > 0:
        flag = selectRandom(edges)
        return flag

def selectRandom(lis):
    import random

    n = len(lis)
    rnd = random.randrange(0,n)
    return lis[rnd]



def main():
    print("Tic Tac Toe")
    player = int(input("1 vs 1 [Enter 1] / 1 vs Comp [Enter 2] :"))
    print("Player 1 is 'X' and Player 2 is 'O'")
    print()
    printBoard(board)
    
    if player == 2:
        while not(isBoardFull(board)):
            if not(isWinner(board, 'O')):
                playerMove()
                printBoard(board)
            else:
                print('O is the winner !')
                break
            
            
            if not(isWinner(board, 'X')):
                move = compMove()
                if isBoardFull(board):
                    break
                else:
                    insertLetter('O', move)
                    print("Computer played the move O in position", move)
                    printBoard(board)
            else:
                print('X is the winner !') 
                break  
            
        
        
        if isBoardFull(board):
            print("The game is a tie !")
            
    if player == 1:
        while not(isBoardFull(board)):
            if not(isWinner(board, 'O')):
                player1Move()
                printBoard(board)
            else:
                print('O is the winner !')
                break
            
            
            if not(isWinner(board, 'X')):
                if isBoardFull(board):
                    break
                else:
                    player2Move()
                    printBoard(board)
            else:
                print('X is the winner !') 
                break             
        
        
        if isBoardFull(board):
            print("The game is a tie !")

while True:
    inp = input("Do you want to play? (Y/N)")
    if inp.lower() == 'y':
        board = [' ' for x in range(10)]
        print("---------------------------------------")
        main()
    else:
        print("Thank you for playing !")
        break
              
