board={'1':' ','2':' ','3':' ',
        '4':' ','5':' ','6':' ',
        '7':' ','8':' ','9':' ' }
list=[1,2,3,4,5,6,7,8,9]

def printBoard(board):
    print("\n")
    print(board['1']+" | "+board['2']+" | "+board['3'])
    print("---------")
    print(board['4']+" | "+board['5']+" | "+board['6'])
    print("---------")
    print(board['7']+" | "+board['8']+" | "+board['9']) 

while(True):
    player1=input("\n what does player1 want to be 'X' or 'O' ")
    player1=player1.upper()
    if(player1=='X' or player1=='O'):
        break    

if(player1=='X'):
    player2='O'
else :
    player2='X'

printBoard(board)

print("player1 will take his chance first")

for i in range(5):
    while(True):
        position=input("\nwhat is the move of player 1 ")
        if(int(position) in list):
            break
        
    board[str(position)]=player1
    printBoard(board)
    list.remove(int(position))
     
    if(board['1']==board['2']==board['3']==player1 or board['4']==board['5']==board['6'] == player1 or
       board['1']==board['4']==board['7'] == player1 or board['1']==board['5']==board['9'] == player1 or
       board['3']==board['6']==board['9'] == player1 or board['3']==board['5']==board['7'] == player1 or
       board['2']==board['5']==board['8'] == player1 or board['7']==board['8']==board['9'] == player1 ):
       
        print("\n---------- the player1 has won ! player2 lose . -------------")
        break
    
    if(i==4):
        print("\n--------------------------- Draw -----------------------------")

    while(True):
        position=input("\nwhat is the move of player 2 ")
        if(int(position) in list):
            break
        
    board[str(position)]=player2
    printBoard(board)
    list.remove(int(position))
     
    if(board['1']==board['2']==board['3']==player2 or board['4']==board['5']==board['6'] == player2 or
       board['1']==board['4']==board['7'] == player2 or board['1']==board['5']==board['9'] == player2 or
       board['3']==board['6']==board['9'] == player2 or board['3']==board['5']==board['7'] == player2 or
       board['2']==board['5']==board['8'] == player2 or board['7']==board['8']==board['9'] == player2 ):
       
        print("\n---------- the player2 has won ! player1 lose . -------------")
        break
    